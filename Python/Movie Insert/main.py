import random

with open("movies.txt") as f:
    movie = f.read().split('\n')

for i in range(50):
    pegi = random.choice([3, 7, 12, 16, 18])
    print(f"INSERT INTO film (film_name, pegi) VALUES ('{movie[i]}', '{pegi}');")
