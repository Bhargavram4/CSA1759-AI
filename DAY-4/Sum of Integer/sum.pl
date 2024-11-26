% Base Case:
sum(0,0).
% Recursive Case:
sum(N,Result):-
    N>0,
    N1 is N-1,
    sum(N1,TempResult),
    Result is TempResult+N.
