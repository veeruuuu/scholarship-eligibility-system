// Presentation-only mapping of the backend's recommendation strings to
// display order and color. Does not affect scoring or validation logic.
export const RECOMMENDATION_TIERS = [
  { key: 'Not Eligible', color: 'var(--tier-1)' },
  { key: 'Low Priority', color: 'var(--tier-2)' },
  { key: 'Medium Priority', color: 'var(--tier-3)' },
  { key: 'High Priority', color: 'var(--tier-4)' },
  { key: 'Highly Recommended', color: 'var(--tier-5)' },
]