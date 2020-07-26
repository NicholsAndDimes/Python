def play_game(player):
    while True:
        end_game = winning_conditions()
        if end_game is True:
            return
        choice = p_input(player)
        player = game_replace(choice, player)
        game_continue = False
        for k, v in ticdic.items():
            if v.isdigit():
                game_continue = True
                break
        if game_continue is False:
            game_display()
            break
    print("Tie Game")
    return


def p_input(player):
    while True:
        game_display()
        print("Player {} turn".format(player))
        choice = input("Please make a selection: ")
        if choice.isdigit():
            if int(choice) in range(1, 10):
                if choice in ticdic[choice]:
                    break
        print("""-----------------
| Invalid input |
-----------------""")
    return choice


def game_replace(choice, player):
    ticdic[choice] = player
    winning_conditions()
    if player == "X":
        return "O"
    if player == "O":
        return "X"


def winning_conditions():
    players = ["X", "O"]
    for p in players:
        conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for a in conditions:
            game_continue = True
            x = 0
            for k, v in ticdic.items():
                if int(k) in a:
                    if v != p:
                        game_continue = True
                        continue
                    else:
                        x += 1
                    if x == 3:
                        game_continue = False
                if game_continue is False:
                    game_display()
                    print(f"{p} has won 3 in a row, spots {a}")
                    end_game = True
                    return end_game


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


def play_again():
    while True:
        game_on = input("Would you like to play again? [Y/N]: ")
        if game_on.lower() == "y" or game_on.lower() == "yes":
            print("finishing play again function")
            return
        elif game_on.lower() == "n" or game_on.lower() == "no":
            print("That was fun! Goodbye!")
            quit()
        print("Invalid input")


vert_line = f"     |     |     "
horz_line = f"-----+-----+-----"
while True:
    print("game start")
    ticdic = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
    game_continue = True
    player = "X"
    play_game(player)
    print("looping")
    play_again()
