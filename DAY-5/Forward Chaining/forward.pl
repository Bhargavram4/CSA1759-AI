%Facts:
parent(naruto,boruto).
parent(naruto,himawari).
parent(minato,naruto).
parent(hinata,boruto).
%Rules:
sibling(X,Y):-parent(Z,X),parent(Z,Y),X\=Y.
grandparent(X,Y):-parent(X,Z),parent(Z,Y).

