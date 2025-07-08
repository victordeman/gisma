-- Create database (optional, students can create manually)
-- CREATE DATABASE student_db;

-- Connect to database
-- \c student_db

-- Create student_scores table
CREATE TABLE student_scores (
    student_id INTEGER,
    course_id INTEGER,
    score FLOAT,
    date DATE NOT NULL
);

-- Insert sample data
INSERT INTO student_scores (student_id, course_id, score, date) VALUES
(1, 101, 85.5, '2023-01-01'),
(1, 101, 90.0, '2023-01-02'),
(2, 101, 88.0, '2023-01-01'),
(2, 101, 92.5, '2023-01-02'),
(3, 101, 78.0, '2023-01-01'),
(3, 102, 85.0, '2023-01-01'),
(4, 101, 95.0, '2023-01-01');

-- Optional: Create index for demo (students will recreate in exercise)
-- CREATE INDEX idx_course_id ON student_scores(course_id);
