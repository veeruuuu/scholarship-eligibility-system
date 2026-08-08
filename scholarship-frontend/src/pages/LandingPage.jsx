import './LandingPage.css'

function LandingPage({ onStart }) {
  return (
    <div className="landing">
      <div className="landing-copy">
        <span className="eyebrow">Hierarchical fuzzy logic · 4 modules</span>
        <h1>
          Scholarship eligibility,<br />
          <em>assessed transparently.</em>
        </h1>
        <p>
          Every result is built from three underlying assessments — academic
          strength, financial &amp; social need, and achievement — combined
          through an explainable fuzzy inference engine. No black-box scoring.
        </p>
        <ul className="landing-points">
          <li>See exactly which fuzzy rules produced your result</li>
          <li>Academics, need, and achievement weighed together</li>
          <li>A clear rating from Not Eligible to Highly Recommended</li>
        </ul>
        <button className="btn-primary" onClick={onStart}>
          Start Assessment →
        </button>
      </div>

      <div className="landing-preview" aria-hidden="true">
        <div className="preview-card">
          <div className="preview-header">
            <span>Sample Report</span>
            <span className="preview-badge">Highly Recommended</span>
          </div>
          <div className="preview-score">
            <span className="preview-number">87</span>
            <span className="preview-unit">/100</span>
          </div>
          <div className="preview-ladder">
            <span className="seg" /><span className="seg" /><span className="seg" /><span className="seg" /><span className="seg filled" />
          </div>
          <div className="preview-rows">
            <div className="preview-row">
              <span>Academic Strength</span>
              <span className="mono">88</span>
            </div>
            <div className="preview-row">
              <span>Need Score</span>
              <span className="mono">82</span>
            </div>
            <div className="preview-row">
              <span>Achievement</span>
              <span className="mono">76</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default LandingPage