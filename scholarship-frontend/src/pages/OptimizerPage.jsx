import { useState } from 'react'
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
} from 'recharts'
import { runOptimization } from '../services/api'
import './OptimizerPage.css'

function OptimizerPage({ onBack }) {
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleRun = async () => {
    setLoading(true)
    setError(null)
    try {
      const data = await runOptimization()
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="optimizer-page">
      <div className="report-header">
        <span className="eyebrow">Research tool</span>
        <button className="btn-ghost" onClick={onBack}>← Back</button>
      </div>

      <div className="optimizer-intro">
        <h2>Genetic Algorithm — Boundary Calibration</h2>
        <p>
          Runs a Genetic Algorithm against 12 expert-labeled sample students to tune
          the Final Eligibility module's output membership function boundaries. This is a
          standalone calibration tool — it does not modify the live assessment engine.
        </p>
        <button className="btn-primary" onClick={handleRun} disabled={loading}>
          {loading ? 'Running GA (30 generations)…' : 'Run Optimization'}
        </button>
        {error && <p className="status-line error">Error: {error}</p>}
      </div>

      {result && (
        <div className="optimizer-results">
          <div className="mse-strip">
            <MseStat label="Original MSE" value={result.original_mse} />
            <MseStat label="Optimized MSE" value={result.optimized_mse} highlight />
            <MseStat label="Improvement" value={`${result.improvement_pct}%`} isPercent />
            <MseStat label="Sample Size" value={result.sample_count} />
          </div>

          <section className="report-section">
            <h3 className="report-heading">Fitness convergence</h3>
            <div className="chart-card">
              <ResponsiveContainer width="100%" height={280}>
                <LineChart data={result.fitness_history}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#E2E4EA" />
                  <XAxis dataKey="generation" tick={{ fontSize: 11, fill: '#565D74' }} label={{ value: 'Generation', position: 'insideBottom', offset: -4, fontSize: 11 }} />
                  <YAxis tick={{ fontSize: 11, fill: '#565D74' }} label={{ value: 'MSE', angle: -90, position: 'insideLeft', fontSize: 11 }} />
                  <Tooltip contentStyle={{ fontFamily: 'IBM Plex Mono', fontSize: 12, borderRadius: 8, border: '1px solid #E2E4EA' }} />
                  <Line type="monotone" dataKey="best_mse" stroke="#B9872A" strokeWidth={2} dot={false} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </section>

          <section className="report-section">
            <h3 className="report-heading">Boundary comparison — Final Eligibility categories</h3>
            <div className="boundary-table-wrap">
              <table className="boundary-table">
                <thead>
                  <tr>
                    <th>Category</th>
                    <th>Original</th>
                    <th>Optimized</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.keys(result.original_boundaries).map((category) => (
                    <tr key={category}>
                      <td>{category}</td>
                      <td className="mono">
                        [{result.original_boundaries[category].map((n) => Math.round(n)).join(', ')}]
                      </td>
                      <td className="mono highlight">
                        [{result.optimized_boundaries[category].map((n) => Math.round(n)).join(', ')}]
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        </div>
      )}
    </div>
  )
}

function MseStat({ label, value, highlight, isPercent }) {
  return (
    <div className={`mse-stat ${highlight ? 'highlight' : ''}`}>
      <span className="mse-label">{label}</span>
      <span className="mse-value">{isPercent ? value : value}</span>
    </div>
  )
}

export default OptimizerPage