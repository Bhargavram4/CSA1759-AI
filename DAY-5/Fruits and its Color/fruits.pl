% Facts:
fruit(orange,orange).
fruit(apple,red).
fruit(grape,green).
fruit(banana,yellow).
fruit(kiwi,brown).
fruit(lemon,yellow).
fruit(peer,green).
fruit(strawberry,red).
% Rules:
fruit_color(Fruit,Color):-fruit(Fruit,Color).
color_by_fruit(Color,Fruit):-fruit(Fruit,Color).
