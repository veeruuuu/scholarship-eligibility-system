import { RECOMMENDATION_TIERS } from '../utils/tiers'
import './RatingLadder.css'

function RatingLadder({ recommendation }) {
  const activeIndex = RECOMMENDATION_TIERS.findIndex((t) => t.key === recommendation)

  return (
    <div className="rating-ladder">
      <div className="ladder-track">
        {RECOMMENDATION_TIERS.map((tier, i) => (
          <div
            key={tier.key}
            className={`ladder-segment ${i <= activeIndex ? 'filled' : ''} ${i === activeIndex ? 'active' : ''}`}
            style={{ '--segment-color': tier.color }}
            title={tier.key}
          />
        ))}
      </div>
      <div className="ladder-caption">
        <span className="ladder-dot" style={{ background: RECOMMENDATION_TIERS[activeIndex]?.color }} />
        {recommendation}
      </div>
    </div>
  )
}

export default RatingLadder