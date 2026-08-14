"""
Genetic Algorithm that tunes the Final Eligibility module's output
membership function boundaries against a hand-labeled sample dataset.

Standalone research/calibration tool. Does NOT modify config.py or affect
/api/evaluate — it only proposes improved boundaries for review.
"""
import random
import numpy as np

from app.fuzzy_engine.config import FINAL_ELIGIBILITY
from app.fuzzy_engine.optimization.dataset import SAMPLE_STUDENTS
from app.fuzzy_engine.optimization.fast_eval import (
    prepare_samples, decode_chromosome, evaluate_with_boundaries,
)

GENE_COUNT = 13
POPULATION_SIZE = 40
GENERATIONS = 30
MUTATION_RATE = 0.25
MUTATION_STRENGTH = 6.0
TOURNAMENT_SIZE = 3
ELITE_COUNT = 2


def _original_genes():
    cats = FINAL_ELIGIBILITY["categories"]
    return [
        cats["Not Eligible"][2], cats["Not Eligible"][3],
        *cats["Low Priority"],
        *cats["Medium Priority"],
        *cats["High Priority"],
        cats["Highly Recommended"][0], cats["Highly Recommended"][1],
    ]


def _random_genes():
    return [random.uniform(0, 100) for _ in range(GENE_COUNT)]


def _fitness(genes, prepared_samples):
    boundaries = decode_chromosome(genes)
    errors = [
        (evaluate_with_boundaries(s["rule_strengths"], boundaries) - s["ideal_score"]) ** 2
        for s in prepared_samples
    ]
    mse = float(np.mean(errors))
    return -mse, mse


def _tournament_select(population, fitnesses):
    contenders = random.sample(list(zip(population, fitnesses)), TOURNAMENT_SIZE)
    contenders.sort(key=lambda c: c[1], reverse=True)
    return contenders[0][0]


def _crossover(parent_a, parent_b):
    point = random.randint(1, GENE_COUNT - 1)
    return parent_a[:point] + parent_b[point:]


def _mutate(genes):
    return [
        g + random.uniform(-MUTATION_STRENGTH, MUTATION_STRENGTH) if random.random() < MUTATION_RATE else g
        for g in genes
    ]


def run_ga():
    prepared_samples = prepare_samples(SAMPLE_STUDENTS)
    population = [_original_genes()] + [_random_genes() for _ in range(POPULATION_SIZE - 1)]

    history = []
    best_genes, best_fitness, best_mse = None, float("-inf"), None

    for generation in range(GENERATIONS):
        scored = [(genes, *_fitness(genes, prepared_samples)) for genes in population]
        scored.sort(key=lambda x: x[1], reverse=True)

        gen_best_genes, gen_best_fitness, gen_best_mse = scored[0]
        if gen_best_fitness > best_fitness:
            best_genes, best_fitness, best_mse = gen_best_genes, gen_best_fitness, gen_best_mse

        history.append({"generation": generation + 1, "best_mse": round(gen_best_mse, 3)})

        next_population = [g for g, _, _ in scored[:ELITE_COUNT]]
        fitnesses = [f for _, f, _ in scored]
        while len(next_population) < POPULATION_SIZE:
            child = _mutate(_crossover(
                _tournament_select(population, fitnesses),
                _tournament_select(population, fitnesses),
            ))
            next_population.append(child)
        population = next_population

    original_genes = _original_genes()
    _, original_mse = _fitness(original_genes, prepared_samples)

    return {
        "original_boundaries": decode_chromosome(original_genes),
        "optimized_boundaries": decode_chromosome(best_genes),
        "original_mse": round(original_mse, 3),
        "optimized_mse": round(best_mse, 3),
        "improvement_pct": round((1 - best_mse / original_mse) * 100, 2) if original_mse > 0 else 0.0,
        "fitness_history": history,
        "sample_count": len(prepared_samples),
    }