% Facts:

% Locations with money
location(park, 10).
location(store, 5).
location(bank, 20).

% Price of bananas
price_of_bananas(15).

% Initially, the monkey has no money
has_money(monkey, 0).

% Rules:

% The monkey can move to a location to collect money.
collect_money(Monkey, Location) :-
    location(Location, Amount),
    has_money(Monkey, CurrentAmount),
    NewAmount is CurrentAmount + Amount,
    retract(has_money(Monkey, CurrentAmount)),
    assert(has_money(Monkey, NewAmount)).

% The monkey can buy bananas if it has enough money.
buy_bananas(Monkey) :-
    has_money(Monkey, Money),
    price_of_bananas(Price),
    Money >= Price,
    write('Monkey has enough money to buy bananas!').

% The monkey can check if it can buy bananas or needs to collect more money.
can_buy_bananas(Monkey) :-
    has_money(Monkey, Money),
    price_of_bananas(Price),
    Money >= Price,
    write('Monkey can buy bananas with the current money: '),
    write(Money),
    nl.

can_buy_bananas(Monkey) :-
    has_money(Monkey, Money),
    price_of_bananas(Price),
    Money < Price,
    write('Monkey does not have enough money, needs '),
    MissingMoney is Price - Money,
    write(MissingMoney),
    write(' more to buy bananas.'),
    nl.

% Query examples:
% Collect money from different locations
% ?- collect_money(monkey, park).
% ?- collect_money(monkey, store).
% ?- collect_money(monkey, bank).

% Check if the monkey can buy bananas
% ?- can_buy_bananas(monkey).
