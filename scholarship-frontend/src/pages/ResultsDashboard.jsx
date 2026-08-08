import ModuleCharts from '../components/ModuleCharts'

import './ResultsDashboard.css'
import ExplanationPanel from '../components/ExplanationPanel'
const RECOMMENDATION_COLORS = {
  'Not Eligible': '#e63946',
  'Low Priority': '#f4a261',
  'Medium Priority': '#e9c46a',
  'High Priority': '#2a9d8f',
  'Highly Recommended': '#1b998b',
}

function ResultsDashboard({ result, onReset }) {
  if (!result) return null

  const {
    academic_strength,
    need_score,
    achievement_score,
    final_eligibility,
    recommendation,
  } = result

  const badgeColor = RECOMMENDATION_COLORS[recommendation] || '#4a4de7'

  return (
    <div className="results-dashboard">
      <div className="dashboard-top">
        <div className="eligibility-card">
          <div className="eligibility-percent">{final_eligibility}%</div>
          <div className="eligibility-label">Final Eligibility Score</div>
          <span className="recommendation-badge" style={{ backgroundColor: badgeColor }}>
            {recommendation}
          </span>
        </div>

        <div className="module-cards">
          <ModuleCard label="Academic Strength" data={academic_strength} />
          <ModuleCard label="Financial / Social Need" data={need_score} />
          <ModuleCard label="Achievement" data={achievement_score} />
        </div>
      </div>

      <ModuleCharts academic={academic_strength} need={need_score} achievement={achievement_score} />
      
      <ExplanationPanel result={result} />


      <button className="reset-btn" onClick={onReset}>
        Evaluate Another Student
      </button>
    </div>
  )
}

function ModuleCard({ label, data }) {
  return (
    <div className="module-card">
      <div className="module-score">{data.score}</div>
      <div className="module-category">{data.category}</div>
      <div className="module-label">{label}</div>
    </div>
  )
}

export default ResultsDashboard