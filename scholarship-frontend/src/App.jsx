import { useState } from 'react'
import Header from './components/Header'
import './components/Header.css'
import LandingPage from './pages/LandingPage'
import StudentInputForm from './pages/StudentInputForm'
import ResultsDashboard from './pages/ResultsDashboard'
import { evaluateEligibility } from './services/api'
import './App.css'

// view: 'landing' | 'form' | 'results'

function App() {
  const [view, setView] = useState('landing')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleFormSubmit = async (formData) => {
    setLoading(true)
    setError(null)
    try {
      const data = await evaluateEligibility(formData)
      setResult(data)
      setView('results')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleReset = () => {
    setResult(null)
    setError(null)
    setView('form')
  }

  return (
    <div className="app">
      <Header />
      <main className="app-main">
        {view === 'landing' && <LandingPage onStart={() => setView('form')} />}

        {view === 'form' && (
          <>
            <StudentInputForm onSubmit={handleFormSubmit} />
            {loading && <p style={{ marginTop: '1rem' }}>Evaluating eligibility...</p>}
            {error && (
              <p style={{ marginTop: '1rem', color: '#e63946' }}>
                Error: {error}
              </p>
            )}
          </>
        )}

        {view === 'results' && result && (
          <ResultsDashboard result={result} onReset={handleReset} />
        )}
      </main>
    </div>
  )
}

export default App