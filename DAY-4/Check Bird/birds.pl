% Facts:
can_fly(eagle).
can_fly(sparrow).
can_fly(pigeon).
cannot_fly(ostrich).
cannot_fly(penguin).
cannot_fly(kangaroo).
% Rule:
cannot_fly_check(Bird):-
   cannot_fly(Bird),write(Bird),write(' Cannot fly').
can_fly_check(Bird):-
    can_fly(Bird),write(Bird),write(' Can fly').
check_bird(Bird):-
    can_fly_check(Bird);
    cannot_fly_check(Bird).
