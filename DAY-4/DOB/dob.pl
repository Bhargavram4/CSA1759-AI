% Facts:
person('Eswar','2005-12-16').
person('Sriram','2006-06-16').
person('Vamsi','2000-05-24').
% Rule:
dob(Name,DOB):-person(Name,DOB).
