import { useState } from 'react'
import { validateStudentForm } from '../utils/validation'
import './StudentInputForm.css'

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
    <form className="student-form" onSubmit={handleSubmit} noValidate>
      <div className="form-intro">
        <span className="eyebrow">Student assessment</span>
        <h2>Enter student details</h2>
      </div>

      <section className="form-section">
        <div className="section-heading">
          <span className="section-index">01</span>
          <h3>Academic details</h3>
        </div>
        <div className="form-grid">
          <Field label="10th Marks (%)" error={errors.marks10}>
            <input type="number" name="marks10" value={formData.marks10} onChange={handleChange} min="0" max="100" />
          </Field>
          <Field label="12th Marks (%)" error={errors.marks12}>
            <input type="number" name="marks12" value={formData.marks12} onChange={handleChange} min="0" max="100" />
          </Field>
          <Field label="Entrance Exam — Marks Obtained" error={errors.entranceObtained}>
            <input type="number" name="entranceObtained" value={formData.entranceObtained} onChange={handleChange} min="0" />
          </Field>
          <Field label="Entrance Exam — Maximum Marks" error={errors.entranceMax}>
            <input type="number" name="entranceMax" value={formData.entranceMax} onChange={handleChange} min="1" />
          </Field>
          <Field label="Current Semester" error={errors.semester}>
            <input type="number" name="semester" value={formData.semester} onChange={handleChange} min="1" max="8" />
          </Field>
          {showCgpa && (
            <Field label="Current CGPA (0–10)" error={errors.cgpa}>
              <input type="number" name="cgpa" value={formData.cgpa} onChange={handleChange} min="0" max="10" step="0.01" />
            </Field>
          )}
        </div>
      </section>

      <section className="form-section">
        <div className="section-heading">
          <span className="section-index">02</span>
          <h3>Financial &amp; social background</h3>
        </div>
        <div className="form-grid">
          <Field label="Annual Family Income (₹)" error={errors.annualIncome}>
            <input type="number" name="annualIncome" value={formData.annualIncome} onChange={handleChange} min="0" />
          </Field>
          <Field label="Disability">
            <select name="disability" value={formData.disability} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
            </select>
          </Field>
          <Field label="Hostel / Day Scholar">
            <select name="hostelType" value={formData.hostelType} onChange={handleChange}>
              <option value="Day Scholar">Day Scholar</option>
              <option value="Hosteller">Hosteller</option>
            </select>
          </Field>
          <Field label="Location">
            <select name="location" value={formData.location} onChange={handleChange}>
              <option value="Urban">Urban</option>
              <option value="Rural">Rural</option>
            </select>
          </Field>
        </div>
      </section>

      <section className="form-section">
        <div className="section-heading">
          <span className="section-index">03</span>
          <h3>Extra-curricular achievement</h3>
        </div>
        <div className="form-grid">
          <Field label="Achievement Score (0–100)" error={errors.extraCurricular} hint="0 = none · 30 = school-level · 60 = state-level · 90+ = national/international">
            <input type="number" name="extraCurricular" value={formData.extraCurricular} onChange={handleChange} min="0" max="100" />
          </Field>
        </div>
      </section>

      <button type="submit" className="btn-primary submit-btn">
        Run Eligibility Assessment
      </button>
    </form>
  )
}

function Field({ label, error, hint, children }) {
  return (
    <div className="form-field">
      <label>{label}</label>
      {children}
      {hint && <small>{hint}</small>}
      {error && <span className="error-text">{error}</span>}
    </div>
  )
}

export default StudentInputForm