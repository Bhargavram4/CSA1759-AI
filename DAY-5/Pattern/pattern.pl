% Base Case:
pattern_match([],_).
% Recursive Case:
pattern_match([H|T1],[H|T2]):-pattern_match(T1,T2).
% Recursive Case:
pattern_match(Pattern,[_|T]):-pattern_match(Pattern,T).
