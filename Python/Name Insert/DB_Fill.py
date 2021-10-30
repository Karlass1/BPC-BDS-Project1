import random
pool_f = ["Florence", "Katy", "Rachel", "Caitlyn", "Isabela", "Petra", "Marta", "Jana", "Lenka", "Ivana", "Iveta", "Zuzana", "Tereza", "Martina", "Lana", "Kristyna", "Charlotte"]
pool_m = ["Karl", "Charles", "Peter", "Petr", "Jakub", "Jacob", "Pavel", "Stanislav", "Marek", "Rowan", "Tate", "Jack", "Hans", "Jan", "Ondrej"]
pool_s = ["Petros", "Higgins", "Dickens", "Romaine", "Roland", "Hemmingway", "Sklodowski", "Jaworecky", "Random", "Nevim", "Portos"]

for i in range (30):
    first = pool_f[random.randint(0,16)]
    last = pool_s[random.randint(0,10)]
    age = random.randint(20,50)
    print("INSERT INTO person (first_name, last_name, age, email) VALUES ('%s', '%s', '%d', '%s.%s@mail.eu');" %(first, last, age, first, last))

for i in range (30):
    first = pool_m[random.randint(0,14)]
    last = pool_s[random.randint(0,10)]
    age = random.randint(20,50)
    print("INSERT INTO person (first_name, last_name, age, email) VALUES ('%s', '%s', '%d', '%s.%s@mail.eu');" %(first, last, age, first, last))
input()