print('''
      ,                      ,
    /                        \\
   ((__-^^-,-^^-__))
      `-_---'  `---_-'
      <__|o`  'o|__>
            \   `   /
             ):   :(
             :o_o:
               "-"  ''')

print("Tame the Beast!")
print("This is the first time you're entering the ring as a professional Matador! Let's show off your skills.\n")
direction = input("Oh! No! Someone let the beast out before time and it's charging towards you! Decide quickly which way you want to move, left or right?\n")
direction = direction.lower()
if direction == "left":
        position = input("You narrowly escaped the beast's wrath, now what do you want to do? Hold current position or look back for the beast's movement. Type, hold or look.\n").lower()
        if position == "look":
                tame = input("Great thinking there but the beast is charging again, chose your action: fight, run or dodge.\n").lower()
                if tame == "fight":
                        print("You tamed the beast and emerged as the shining star of the show!")
                elif tame == "run" or tame == "dodge":
                        print("It apoears, your training didn't pay off and you were thrown out of the ring with all your pride. Let's get back to training.")
                else:
                        print("Wrong input.")
        elif position == "hold":
                print("The beast was quick to throw you out of the ring and here comes to an end to your carrer! ")
        else:
                        print("Wrong input.")
elif direction == "right":
        print("You were thrown out of the ring as well of your professional carrer!")
else:
                        print("Wrong input.")
