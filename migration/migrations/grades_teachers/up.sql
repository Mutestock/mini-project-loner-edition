CREATE TABLE IF NOT EXISTS grades_teachers(
    grade_id INTEGER REFERENCES grades (id) ON UPDATE CASCADE ON DELETE CASCADE,
    teacher_id INTEGER REFERENCES teachers (id) ON UPDATE CASCADE ON DELETE CASCADE
);