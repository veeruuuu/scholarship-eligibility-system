import {
  RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis,
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
} from 'recharts'
import './ModuleCharts.css'

function ModuleCharts({ academic, need, achievement }) {
  const chartData = [
    { subject: 'Academic', score: academic.score, fullMark: 100 },
    { subject: 'Need', score: need.score, fullMark: 100 },
    { subject: 'Achievement', score: achievement.score, fullMark: 100 },
  ]

  return (
    <div className="charts-grid">
      <div className="chart-card">
        <h3>Module Score Comparison (Radar)</h3>
        <ResponsiveContainer width="100%" height={280}>
          <RadarChart data={chartData}>
            <PolarGrid stroke="#e0e0ec" />
            <PolarAngleAxis dataKey="subject" tick={{ fontSize: 13, fill: '#444' }} />
            <PolarRadiusAxis angle={30} domain={[0, 100]} tick={{ fontSize: 11 }} />
            <Radar
              name="Score"
              dataKey="score"
              stroke="#4a4de7"
              fill="#4a4de7"
              fillOpacity={0.35}
            />
            <Tooltip />
          </RadarChart>
        </ResponsiveContainer>
      </div>

      <div className="chart-card">
        <h3>Module Score Comparison (Bar)</h3>
        <ResponsiveContainer width="100%" height={280}>
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e0e0ec" />
            <XAxis dataKey="subject" tick={{ fontSize: 13, fill: '#444' }} />
            <YAxis domain={[0, 100]} tick={{ fontSize: 11 }} />
            <Tooltip />
            <Bar dataKey="score" fill="#4a4de7" radius={[6, 6, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}

export default ModuleCharts