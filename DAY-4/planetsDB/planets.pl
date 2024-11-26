% Facts:
planet_distance(mercury,57.9).
planet_distance(venus,108.2).
planet_distance(earth,149.6).
planet_distance(mars,277.9).
planet_distance(jupiter,400.2).
planet_distance(saturn,450.9).
planet_distance(uranus,557.9).
planet_distance(neptune,673.9).
% Rules:
distance_from_sun(Planet,Distance):-planet_distance(Planet,Distance).

