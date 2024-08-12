from player import Player


def display_board(board_map):
    print(" \t 1   \t 2   \t 3 \n")
    print(f"a \t {board_map.get('a1', ' ')}  | \t {board_map.get('a2', ' ')}  | \t {board_map.get('a3', ' ')} \n")
    print("     ______________________\n")
    print(f"b \t {board_map.get('b1', ' ')}  | \t {board_map.get('b2', ' ')}  | \t {board_map.get('b3', ' ')} \n")
    print("     ______________________\n")
    print(f"c \t {board_map.get('c1', ' ')}  | \t {board_map.get('c2', ' ')}  | \t {board_map.get('c3', ' ')} \n\n")


def get_player_info():
    chosen_characters = []
    players = []
    print("Enter players' names and characters (X/O)\n")
    for i in range(2):
        name = input(f"Player {i + 1}'s name: ")
        while True:
            character = input("Character: ").upper()
            if character in ['X', 'O'] and character not in chosen_characters:
                chosen_characters.append(character)
                players.append(Player(name, character))
                break
    return players


ALL_SLOTS = "a1b1c1a2b2c2a3b3c3"


def game_round(gamers):
    for gamer in gamers:
        gamer.to_default()
    board_map = {"filled": 0}
    display_board(board_map)
    finish = False

    print("Select a slot to mark e.g. a1\n")

    def play(player):
        slot = input(f"{player.name}, mark a slot: ")
        if slot in ALL_SLOTS:
            if slot in board_map:
                print(f"OOPS! Slot {slot} is occupied")
                play(player)
            else:
                board_map[slot] = player.character
                board_map["filled"] += 1
                player.position = slot
                display_board(board_map)
        else:
            print(f"Sorry, slot {slot} does not exist on the board")
            play(player)

    def check_winner(player):
        play(player)
        if board_map["filled"] == 9:
            print("\t\t It's a tie! Nobody Wins!")
            return True
        elif player.won():
            print(f"\t\t {player.name} Wins!")
            return True
        return False

    while not finish:
        for gamer in gamers:
            finish = check_winner(gamer)
            if finish:
                break


play_again = "y"
players = get_player_info()
while play_again.lower() == "y":
    game_round(players)
    play_again = input("\t You guys wanna play again? y/n: ")
    print("\n")
