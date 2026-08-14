function Header({ onNavigateOptimizer }) {
  return (
    <header className="app-header">
      <div className="header-inner">
        <div className="brand">
          <span className="brand-mark">SE</span>
          <div className="brand-text">
            <span className="brand-name">Scholarship Eligibility</span>
            <span className="brand-tagline">Fuzzy Assessment Engine</span>
          </div>
        </div>
        <button className="header-link" onClick={onNavigateOptimizer}>
          GA Optimizer
        </button>
      </div>
    </header>
  )
}

export default Header