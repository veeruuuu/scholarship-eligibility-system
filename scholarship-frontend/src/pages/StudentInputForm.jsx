import { useState } from 'react'
import './StudentInputForm.css'
import { validateStudentForm } from '../utils/validation'

const initialFormState = {
  marks10: '',
  marks12: '',
  entranceObtained: '',
  entranceMax: '',
  semester: '',
  cgpa: '',
  annualIncome: '',
  extraCurricular: '',
  disability: 'No',
  hostelType: 'Day Scholar',
  location: 'Urban',
}

function StudentInputForm({ onSubmit }) {
  const [formData, setFormData] = useState(initialFormState)
  const [errors, setErrors] = useState({})

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()

    const validationErrors = validateStudentForm(formData)
    setErrors(validationErrors)

    if (Object.keys(validationErrors).length === 0) {
      onSubmit(formData)
    }
  }

  const semesterNum = Number(formData.semester)
  const showCgpa = semesterNum >= 2

  return (
    <form onSubmit={handleSubmit}>
      {/* Academic Section */}
      <section className="form-section">
        <h2>Academic Details</h2>

        <div className="form-grid">
          <div className="form-field">
            <label>10th Marks (%)</label>
            <input
              type="number"
              name="marks10"
              value={formData.marks10}
              onChange={handleChange}
              min="0"
              max="100"
              required
            />
            {errors.marks10 && (
              <span className="error-text">{errors.marks10}</span>
            )}
          </div>

          <div className="form-field">
            <label>12th Marks (%)</label>
            <input
              type="number"
              name="marks12"
              value={formData.marks12}
              onChange={handleChange}
              min="0"
              max="100"
              required
            />
            {errors.marks12 && (
              <span className="error-text">{errors.marks12}</span>
            )}
          </div>

          <div className="form-field">
            <label>Entrance Exam — Marks Obtained</label>
            <input
              type="number"
              name="entranceObtained"
              value={formData.entranceObtained}
              onChange={handleChange}
              min="0"
              required
            />
            {errors.entranceObtained && (
              <span className="error-text">
                {errors.entranceObtained}
              </span>
            )}
          </div>

          <div className="form-field">
            <label>Entrance Exam — Maximum Marks</label>
            <input
              type="number"
              name="entranceMax"
              value={formData.entranceMax}
              onChange={handleChange}
              min="1"
              required
            />
            {errors.entranceMax && (
              <span className="error-text">{errors.entranceMax}</span>
            )}
          </div>

          <div className="form-field">
            <label>Current Semester</label>
            <input
              type="number"
              name="semester"
              value={formData.semester}
              onChange={handleChange}
              min="1"
              max="8"
              required
            />
            {errors.semester && (
              <span className="error-text">{errors.semester}</span>
            )}
          </div>

          {showCgpa && (
            <div className="form-field">
              <label>Current CGPA (0–10)</label>
              <input
                type="number"
                name="cgpa"
                value={formData.cgpa}
                onChange={handleChange}
                min="0"
                max="10"
                step="0.01"
                required
              />
              {errors.cgpa && (
                <span className="error-text">{errors.cgpa}</span>
              )}
            </div>
          )}
        </div>
      </section>

      {/* Financial / Social Section */}
      <section className="form-section">
        <h2>Financial &amp; Social Background</h2>

        <div className="form-grid">
          <div className="form-field">
            <label>Annual Family Income (₹)</label>
            <input
              type="number"
              name="annualIncome"
              value={formData.annualIncome}
              onChange={handleChange}
              min="0"
              required
            />
            {errors.annualIncome && (
              <span className="error-text">{errors.annualIncome}</span>
            )}
          </div>

          <div className="form-field">
            <label>Disability</label>
            <select
              name="disability"
              value={formData.disability}
              onChange={handleChange}
            >
              <option value="No">No</option>
              <option value="Yes">Yes</option>
            </select>
          </div>

          <div className="form-field">
            <label>Hostel / Day Scholar</label>
            <select
              name="hostelType"
              value={formData.hostelType}
              onChange={handleChange}
            >
              <option value="Day Scholar">Day Scholar</option>
              <option value="Hosteller">Hosteller</option>
            </select>
          </div>

          <div className="form-field">
            <label>Location</label>
            <select
              name="location"
              value={formData.location}
              onChange={handleChange}
            >
              <option value="Urban">Urban</option>
              <option value="Rural">Rural</option>
            </select>
          </div>
        </div>
      </section>

      {/* Achievement Section */}
      <section className="form-section">
        <h2>Extra-Curricular Achievement</h2>

        <div className="form-grid">
          <div className="form-field">
            <label>Achievement Score (0–100)</label>
            <input
              type="number"
              name="extraCurricular"
              value={formData.extraCurricular}
              onChange={handleChange}
              min="0"
              max="100"
              required
            />

            {errors.extraCurricular && (
              <span className="error-text">
                {errors.extraCurricular}
              </span>
            )}

            <small>
              e.g. 0 = none, 30 = school-level, 60 = state-level, 90+ =
              national/international
            </small>
          </div>
        </div>
      </section>

      <button type="submit" className="submit-btn">
        Check Eligibility
      </button>
    </form>
  )
}

export default StudentInputForm