import './LandingPage.css'

function LandingPage({ onStart }) {
  return (
    <div className="landing">
      <div className="landing-content">
        <h2>Find Out Your Scholarship Eligibility</h2>
        <p>
          This system evaluates your academic strength, financial &amp; social need,
          and extra-curricular achievement using a hierarchical fuzzy logic model —
          giving you a transparent, explainable eligibility result instead of a
          black-box score.
        </p>
        <ul className="landing-points">
          <li>Explainable scoring — see exactly why you got your result</li>
          <li>Covers academics, financial need, and achievements together</li>
          <li>Instant recommendation: from Not Eligible to Highly Recommended</li>
        </ul>
        <button className="start-btn" onClick={onStart}>
          Check My Eligibility →
        </button>
      </div>
    </div>
  )
}

export default LandingPage