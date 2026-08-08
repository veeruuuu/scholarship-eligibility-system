import { generateSuggestions } from '../utils/suggestions'
import './ExplanationPanel.css'

function ExplanationPanel({ result }) {
  const {
    academic_strength, need_score, achievement_score,
    activated_rules, key_factors, explanation,
  } = result

  const suggestions = generateSuggestions(academic_strength, need_score, achievement_score)

  return (
    <div className="explanation-grid">
      <div className="panel-card">
        <h3>Why This Result?</h3>
        <p className="explanation-text">{explanation}</p>
      </div>

      <div className="panel-card">
        <h3>Key Factors</h3>
        <ul className="factor-list">
          {key_factors.map((factor, i) => (
            <li key={i}>{factor}</li>
          ))}
        </ul>
      </div>

      <div className="panel-card">
        <h3>Activated Fuzzy Rules</h3>
        <ul className="rule-list">
          {activated_rules.map((rule, i) => (
            <li key={i}><code>{rule}</code></li>
          ))}
        </ul>
      </div>

      <div className="panel-card">
        <h3>Improvement Suggestions</h3>
        <ul className="suggestion-list">
          {suggestions.map((s, i) => (
            <li key={i}>{s}</li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default ExplanationPanel