%Facts:
fact(has_fever).
fact(has_cough).
% Rules:
has_flu:-has_fever,has_cough.
has_fever:-fact(has_fever).
has_cough:-fact(has_cough).
