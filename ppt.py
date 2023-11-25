from random import choice


ppt_choice=["piedra", "papel", "tijera"]


def playerChoice():
    print("Seleccciona 1 para priedra, 2 para papel, 3 para tijera")
    player_choice=int(input("Player >"))
    global player_move

    if player_choice==1:
        player_move="piedra"
    elif player_choice==2:
        player_move="papel"
    elif player_choice==3:
        player_move="tijera"
    

    return f"You played --{player_move.upper()}"

def compuChoice():
    global compu_move
    compu_move=choice(ppt_choice)
    return f"computer played --{compu_move.upper()}"

def winLose():

    print()
    #winning conditions for the game
    if (player_move=="piedra" and compu_move == "tijera"):
        return "Player wins!"
    if (player_move=="tijera" and compu_move == "tijera"):
        return "Empate"
    if (player_move=="papel" and compu_move == "tijera"):
        return "Computer Wins!!"
    if (player_move=="piedra" and compu_move == "piedra"):
        return "Empate"
    if (player_move=="papel" and compu_move == "piedra"):
        return "Player wins!"
    if (player_move=="tijera" and compu_move == "piedra"):
        return "Computer wins!!"
    if (player_move=="piedra" and compu_move == "papel"):
        return "Computer wins!!"
    if (player_move=="tijera" and compu_move == "papel"):
        return "Player wins!"
    if (player_move=="papel" and compu_move == "papel"):
        return "Empate"


print(playerChoice())
print(compuChoice())
print(winLose())
    