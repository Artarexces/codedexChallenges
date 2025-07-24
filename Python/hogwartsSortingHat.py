Q1 = "Do you like Dawn or Dusk?"
Q2 = "When I’m dead, I want people to remember me as:"
Q3 = "Which kind of instrument most pleases your ear?"

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

answers1 = ["dawn", "dusk"]
answers2 = ["good", "great", "wise", "bold"]
answers3 = ["violin","trumpet","piano","drum"]

answers = input(Q1).lower()

if answers == "dawn":
    gryffindor += 1
    ravenclaw += 1
elif answers == "dusk":
    slytherin += 1
    hufflepuff += 1
else:
    print("Wrong input")

answers = input(Q2).lower()

if answers == "good":
    hufflepuff += 2
elif answers == "great":
    slytherin += 2
elif answers == "wise":
    ravenclaw += 2
elif answers == "bold":
    gryffindor += 2
else:
    print("Wrong input")

answers = input(Q3).lower()

if answers == "violin":
    gryffindor += 3
elif answers == "trumpet":
    slytherin += 3
elif answers == "piano":
    ravenclaw += 3
elif answers == "drum":
    hufflepuff += 3
else:
    print("Wrong input")


if gryffindor > hufflepuff and gryffindor > ravenclaw and gryffindor > slytherin:
    print("Gryffindor!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("Hufflepuff!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("Ravenclaw!")
elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
    print("Slytherin!")
else:
    print("Tie!")
