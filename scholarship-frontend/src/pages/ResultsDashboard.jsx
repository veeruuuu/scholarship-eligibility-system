import RatingLadder from '../components/RatingLadder'
import ModuleCharts from '../components/ModuleCharts'
import ExplanationPanel from '../components/ExplanationPanel'
import './ResultsDashboard.css'

function ResultsDashboard({ result, onReset }) {
  if (!result) return null

  const { academic_strength, need_score, achievement_score, final_eligibility, recommendation } = result

  return (
    <div className="results-dashboard">
      <div className="report-header">
        <span className="eyebrow">Assessment report</span>
        <button className="btn-ghost" onClick={onReset}>
          ← New assessment
        </button>
      </div>

      <div className="summary-strip">
        <div className="score-block">
          <span className="score-label">Final Eligibility Score</span>
          <div className="score-value">
            <span className="score-number">{final_eligibility}</span>
            <span className="score-unit">/100</span>
          </div>
        </div>
        <div className="ladder-block">
          <RatingLadder recommendation={recommendation} />
        </div>
      </div>

      <div className="module-cards">
        <ModuleCard label="Academic Strength" data={academic_strength} />
        <ModuleCard label="Financial / Social Need" data={need_score} />
        <ModuleCard label="Achievement" data={achievement_score} />
      </div>

      <section className="report-section">
        <h3 className="report-heading">Score composition</h3>
        <ModuleCharts academic={academic_strength} need={need_score} achievement={achievement_score} />
      </section>

      <section className="report-section">
        <h3 className="report-heading">Explainability</h3>
        <ExplanationPanel result={result} />
      </section>
    </div>
  )
}

function ModuleCard({ label, data }) {
  return (
    <div className="module-card">
      <span className="module-label">{label}</span>
      <div className="module-score-row">
        <span className="module-score">{data.score}</span>
        <span className="module-category">{data.category}</span>
      </div>
    </div>
  )
}

export default ResultsDashboard