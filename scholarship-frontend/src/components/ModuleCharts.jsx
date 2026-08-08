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
        <h4>Module comparison — radar</h4>
        <ResponsiveContainer width="100%" height={260}>
          <RadarChart data={chartData}>
            <PolarGrid stroke="#E2E4EA" />
            <PolarAngleAxis dataKey="subject" tick={{ fontSize: 12, fill: '#565D74', fontFamily: 'Inter' }} />
            <PolarRadiusAxis angle={30} domain={[0, 100]} tick={{ fontSize: 10, fill: '#8A90A3' }} />
            <Radar name="Score" dataKey="score" stroke="#B9872A" fill="#B9872A" fillOpacity={0.28} />
            <Tooltip contentStyle={{ fontFamily: 'IBM Plex Mono', fontSize: 12, borderRadius: 8, border: '1px solid #E2E4EA' }} />
          </RadarChart>
        </ResponsiveContainer>
      </div>

      <div className="chart-card">
        <h4>Module comparison — bar</h4>
        <ResponsiveContainer width="100%" height={260}>
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#E2E4EA" vertical={false} />
            <XAxis dataKey="subject" tick={{ fontSize: 12, fill: '#565D74', fontFamily: 'Inter' }} axisLine={{ stroke: '#E2E4EA' }} tickLine={false} />
            <YAxis domain={[0, 100]} tick={{ fontSize: 10, fill: '#8A90A3' }} axisLine={false} tickLine={false} />
            <Tooltip contentStyle={{ fontFamily: 'IBM Plex Mono', fontSize: 12, borderRadius: 8, border: '1px solid #E2E4EA' }} cursor={{ fill: '#F5F6F8' }} />
            <Bar dataKey="score" fill="#12182B" radius={[5, 5, 0, 0]} maxBarSize={56} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}

export default ModuleCharts