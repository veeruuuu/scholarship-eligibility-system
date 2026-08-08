// src/utils/suggestions.js

/**
 * Generates plain-language improvement suggestions based on which module
 * categories are weakest. Purely presentational — does not affect scoring.
 */
export function generateSuggestions(academic, need, achievement) {
  const suggestions = []

  if (['Poor', 'Average'].includes(academic.category)) {
    suggestions.push('Improving board exam or entrance exam scores would raise the Academic Strength score.')
  }
  if (academic.category === 'Good') {
    suggestions.push('A stronger CGPA or entrance percentage could push Academic Strength into the Excellent range.')
  }

  if (['Low', 'Medium'].includes(achievement.category)) {
    suggestions.push('Participating in more extra-curricular activities (state or national level) would raise the Achievement score.')
  }

  if (need.category === 'Low') {
    suggestions.push('Eligibility is currently limited by lower financial/social need relative to other applicants.')
  }

  if (suggestions.length === 0) {
    suggestions.push('All module scores are strong — focus on maintaining current academic and extracurricular performance.')
  }

  return suggestions
}