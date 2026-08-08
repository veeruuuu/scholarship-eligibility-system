// src/services/api.js

const API_BASE_URL = 'http://localhost:8000'

/**
 * Sends student form data to the backend for eligibility evaluation.
 * Converts frontend field names to the shape the backend expects.
 */
export async function evaluateEligibility(formData) {
  const payload = {
    marks_10th: Number(formData.marks10),
    marks_12th: Number(formData.marks12),
    entrance_obtained: Number(formData.entranceObtained),
    entrance_max: Number(formData.entranceMax),
    semester: Number(formData.semester),
    cgpa: formData.semester >= 2 ? Number(formData.cgpa) : null,
    annual_income: Number(formData.annualIncome),
    extra_curricular: Number(formData.extraCurricular),
    disability: formData.disability === 'Yes',
    hostel_type: formData.hostelType,
    location: formData.location,
  }

  const response = await fetch(`${API_BASE_URL}/api/evaluate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}))
    throw new Error(errorBody.detail || `Request failed with status ${response.status}`)
  }

  return response.json()
}