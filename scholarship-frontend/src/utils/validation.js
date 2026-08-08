// src/utils/validation.js

export function validateStudentForm(data) {
  const errors = {}

  // 10th Marks
  if (data.marks10 === '' || isNaN(data.marks10)) {
    errors.marks10 = '10th marks are required'
  } else if (data.marks10 < 0 || data.marks10 > 100) {
    errors.marks10 = 'Must be between 0 and 100'
  }

  // 12th Marks
  if (data.marks12 === '' || isNaN(data.marks12)) {
    errors.marks12 = '12th marks are required'
  } else if (data.marks12 < 0 || data.marks12 > 100) {
    errors.marks12 = 'Must be between 0 and 100'
  }

  // Entrance exam
  if (data.entranceObtained === '' || isNaN(data.entranceObtained)) {
    errors.entranceObtained = 'Marks obtained are required'
  }
  if (data.entranceMax === '' || isNaN(data.entranceMax) || Number(data.entranceMax) <= 0) {
    errors.entranceMax = 'Maximum marks must be greater than 0'
  }
  if (
    !errors.entranceObtained &&
    !errors.entranceMax &&
    Number(data.entranceObtained) > Number(data.entranceMax)
  ) {
    errors.entranceObtained = 'Marks obtained cannot exceed maximum marks'
  }

  // Semester
  if (data.semester === '' || isNaN(data.semester)) {
    errors.semester = 'Semester is required'
  } else if (data.semester < 1 || data.semester > 8) {
    errors.semester = 'Semester must be between 1 and 8'
  }

  // CGPA — only required if semester >= 2
  const semesterNum = Number(data.semester)
  if (semesterNum >= 2) {
    if (data.cgpa === '' || isNaN(data.cgpa)) {
      errors.cgpa = 'CGPA is required from semester 2 onwards'
    } else if (data.cgpa < 0 || data.cgpa > 10) {
      errors.cgpa = 'CGPA must be between 0 and 10'
    }
  }

  // Annual income
  if (data.annualIncome === '' || isNaN(data.annualIncome)) {
    errors.annualIncome = 'Annual income is required'
  } else if (data.annualIncome < 0) {
    errors.annualIncome = 'Income cannot be negative'
  }

  // Extra-curricular
  if (data.extraCurricular === '' || isNaN(data.extraCurricular)) {
    errors.extraCurricular = 'Achievement score is required'
  } else if (data.extraCurricular < 0 || data.extraCurricular > 100) {
    errors.extraCurricular = 'Must be between 0 and 100'
  }

  return errors
}