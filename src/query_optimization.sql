-- Initial query (unoptimized)
SELECT student_id, AVG(score) AS avg_score
FROM student_scores
WHERE course_id = 101
GROUP BY student_id;

-- Analyze query performance
EXPLAIN ANALYZE
SELECT student_id, AVG(score) AS avg_score
FROM student_scores
WHERE course_id = 101
GROUP BY student_id;

-- Create index to optimize
CREATE INDEX idx_course_id ON student_scores(course_id);

-- Re-run query to compare performance
EXPLAIN ANALYZE
SELECT student_id, AVG(score) AS avg_score
FROM student_scores
WHERE course_id = 101
GROUP BY student_id;
