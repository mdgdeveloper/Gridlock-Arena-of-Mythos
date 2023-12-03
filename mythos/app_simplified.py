# Define the creatures and their properties
creatures = [
    {"name": "Dragon", "start": [2,2], "moves": ["RIGHT","LEFT","DOWN"], "power": 7, "icon": "🐉"},
    {"name": "Goblin", "start": [2,3], "moves": ["LEFT","RIGHT","UP"], "power": 3, "icon": "👺"},
    {"name": "Ogre", "start": [0,0], "moves": ["RIGHT","DOWN","DOWN"], "power": 5, "icon": "👹"}
]

# Define the directions and the board
directions = {"UP": [-1,0], "DOWN": [1,0], "LEFT": [0,-1], "RIGHT": [0,1]}
board = [["⬜️" for _ in range(5)] for _ in range(5)]

# Initialize scores and place creatures on the board
scores = {creature["name"]: 0 for creature in creatures}
for creature in creatures:
    board[creature["start"][0]][creature["start"][1]] = creature["icon"]

# Define helper functions
def print_board(): print('\n'.join(' '.join(row) for row in board))
def get_creature_by_name(name): return next((c for c in creatures if c["name"] == name), None)
def get_creature_by_icon(icon): return next((c for c in creatures if c["icon"] == icon), None)

# Battle function
def battle(creature1, creature2):
    if creature1["power"] > creature2["power"]:
        scores[creature1["name"]] += creature1["power"] - creature2["power"]
        scores[creature2["name"]] -= creature1["power"] - creature2["power"]
    else:
        scores[creature1["name"]] -= creature2["power"] - creature1["power"]
        scores[creature2["name"]] += creature2["power"] - creature1["power"]

# Game loop
for i in range(3):
    for creature in creatures:
        current_position = creature["start"]
        next_move = creature["moves"][i]
        next_position = [current_position[0] + directions[next_move][0], current_position[1] + directions[next_move][1]]

        if next_position[0] < 0 or next_position[0] > 4 or next_position[1] < 0 or next_position[1] > 4:
            print(f"{creature['name']} is out of the board")
            continue

        if board[next_position[0]][next_position[1]] != "⬜️":
            other_creature = get_creature_by_icon(board[next_position[0]][next_position[1]])
            board[current_position[0]][current_position[1]] = "🤺"
            board[next_position[0]][next_position[1]] = "🤺"
            battle(creature, other_creature)
            print_board()
            print(f"Scores: {scores}")
            board[current_position[0]][current_position[1]] = creature["icon"]
            board[next_position[0]][next_position[1]] = other_creature["icon"]
            continue

        board[current_position[0]][current_position[1]] = "⬜️"
        board[next_position[0]][next_position[1]] = creature["icon"]
        creature["start"] = next_position

    print(f"Move {i+1}")
    print_board()
    print(f"Scores: {scores}")