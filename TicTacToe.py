def p_input(player):
    while True:
        game_display()
        print("Player {} turn".format(player))
        choice = input("Please make a selection:")
        if choice.isdigit():
            if int(choice) in range(1, 10):
                if choice in ticdic[choice]:
                    print(f"{choice} is in {ticdic[choice]}")
                    break
        print("Invalid input")
    return choice


def game_display():
    print("""{}
  {}  |  {}  |  {}  
{}
{}
{}
  {}  |  {}  |  {}  
{}
{}
{}
  {}  |  {}  |  {}  
{}""".format(vert_line, ticdic['1'], ticdic['2'], ticdic['3'], vert_line, horz_line,
             vert_line, ticdic['4'], ticdic['5'], ticdic['6'], vert_line, horz_line,
             vert_line, ticdic['7'], ticdic['8'], ticdic['9'], vert_line))


def game_replace(choice, player):
    ticdic[choice] = player
    if player == "X":
        return "O"
    if player == "O":
        return "X"


ticdic = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
player = "X"
vert_line = f"     |     |     "
horz_line = f"-----+-----+-----"
game_continue = True
while True:
    choice = p_input(player)
    player = game_replace(choice, player)
    game_continue = False
    for k, v in ticdic.items():
        if v.isdigit():
            game_continue = True
            break
    if game_continue is False:
        game_display()2
        break
print("Board filed up, winning conditions in next version")
