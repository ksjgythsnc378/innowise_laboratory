

-- 1. create table 'students', 'grades'
CREATE TABLE if NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name TEXT,
birth_year INTEGER);

CREATE TABLE if NOT EXISTS grades (id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER,
subject TEXT,
grade INTEGER);

-- 2. insert data
INSERT INTO students (full_name, birth_year) VALUES ('Alice Johnson', 2005),
        ('Brian Smith', 2004),
        ('Carla Reyes', 2006),
        ('Daniel Kim', 2005),
        ('Eva Thompson', 2003),
        ('Felix Nguyen', 2007),
        ('Grace Patel', 2005),
        ('Henry Lopez', 2004),
        ('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade) VALUES (1, 'Math', 88),
        (1, 'English', 92),
        (1, 'Science', 85),
        (2, 'Math', 75),
        (2, 'History', 83),
        (2, 'English', 79),
        (3, 'Science', 95),
        (3, 'Math', 91),
        (3, 'Art', 89),
        (4, 'Math', 84),
        (4, 'Science', 88),
        (4, 'Physical Education', 93),
        (5, 'English', 90),
        (5, 'History', 85),
        (5, 'Math', 88),
        (6, 'Science', 72),
        (6, 'Math', 78),
        (6, 'English', 81),
        (7, 'Art', 94),
        (7, 'Science', 87),
        (7, 'Math', 90),
        (8, 'History', 77),
        (8, 'Math', 83),
        (8, 'Science', 80),
        (9, 'English', 96),
        (9, 'Math', 89),
        (9, 'Art', 92);

-- 3. all grades for student Alice Johnson
SELECT grades.grade AS "Alice Johnson's grades" FROM grades
        JOIN students
        ON grades.student_id = students.id
        WHERE full_name = 'Alice Johnson';

-- 4. calculate average grade per student
SELECT students.full_name, AVG(grades.grade) AS student_average_grade FROM students
        JOIN grades
        ON grades.student_id = students.id
        GROUP BY students.id;

-- 5. all students born after 2004
SELECT students.full_name AS "born after 2004" FROM students
        WHERE students.birth_year > 2004;

-- 6. average grades per subject
SELECT grades.subject, AVG(grades.grade) AS subject_average_grade FROM grades
        GROUP BY grades.subject;

-- 7. top 3 students with highest aveage grades
SELECT students.full_name, AVG(grades.grade) AS student_average_grade FROM students
        JOIN grades
        ON grades.student_id = students.id
        GROUP BY students.id
        ORDER BY student_average_grade DESC
        LIMIT 3;

-- 8. all students who have scored below 80 in any subject
SELECT students.full_name, grades.subject AS "scored < 80" FROM grades
        JOIN students
        ON grades.student_id = students.id
        WHERE grades.grade < 80;