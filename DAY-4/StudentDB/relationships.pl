% Facts:
student(john).
student(mary).
teacher(dr_smith).
teacher(dr_jones).
subject(math).
subject(english).
subject_code(math,'M101').
subject_code(english,'E104').
teaches(dr_smith,math).
teaches(dr_jones,english).
enrolled(john,math).
enrolled(mary,english).
% Rules:
teacher_of_subject(Teacher,Subject):-teaches(Teacher,Subject).
students_in_subject(Student,Subject):-enrolled(Student,Subject).

