
# Define the creatures array containing the following:
# Names: Dragon, Goblin, Ogre
# Start: 2,2 , 2,3 , 0,0 
# Moves: RIGHT,LEFT,DOWN , LEFT,RIGHT,UP, RIGHT,DOWN,DOWN
# Power: 7,3,5
# Icon: 🐉,👺,👹

NUM_MOVES = 3

creatures = [
    {
        "name": "Dragon",
        "start": [2,2],
        "moves": ["RIGHT","LEFT","DOWN"],
        "power": 7,
        "icon": "🐉"
    },
    {
        "name": "Goblin",
        "start": [2,3],
        "moves": ["LEFT","RIGHT","UP"],
        "power": 3,
        "icon": "👺"
    },
    {
        "name": "Ogre",
        "start": [0,0],
        "moves": ["RIGHT","DOWN","DOWN"],
        "power": 5,
        "icon": "👹"
    }
]

# Define a directions object to map the movement directions to their respective changes in coordinates
directions = {
    "UP": [-1,0],
    "DOWN": [1,0],
    "LEFT": [0,-1],
    "RIGHT": [0,1]
}

# Initialize the board with a 5x5 grid of ⬜️
board = [["⬜️" for i in range(5)] for i in range(5)]

# Define a function to print the board
def print_board():
    for row in board:
        print(" ".join(row))

# Define a scores object to store the scores of the creatures
scores = {}

# For each creature initialize the scores to 0 
for creature in creatures:
    scores[creature["name"]] = 0

# Place each creature in the board at their respective start coordinates
for creature in creatures:
    board[creature["start"][0]][creature["start"][1]] = creature["icon"]

# Print the board
# Print a Welcome Message in AScii 
print("--------------------")
print("Welcome to Mythos!")
print("🐉👺👹")
print("--------------------")
print("")
print_board()
print("")

# Print the scores
print(f"Scores: {scores}")

# Create battle function which receives two creatures and calculates the result of the battle for each creature
# The result is calculated by substracting the lower value to the higher and adding the result to the score of the winner in positve and in negative to the score of the loser
def battle(creature1,creature2):
    # creature1 and creature2 are the names of the creatures
    # Find the creatures in the creatures array
    creature1 = next((creature for creature in creatures if creature["name"] == creature1), None)
    creature2 = next((creature for creature in creatures if creature["name"] == creature2), None)
    # Calculate the result of the battle
    # The creature with higher number gets summed to its score the difference between the two numbers
    # The creature with lower number gets substracted from its score the difference between the two numbers
    if creature1["power"] > creature2["power"]:
        scores[creature1["name"]] += creature1["power"] - creature2["power"]
        scores[creature2["name"]] -= creature1["power"] - creature2["power"]
    else:
        scores[creature1["name"]] -= creature2["power"] - creature1["power"]
        scores[creature2["name"]] += creature2["power"] - creature1["power"]

# Function to get the name of a creature from its icon
def get_name(icon):
    for creature in creatures:
        if creature["icon"] == icon:
            return creature["name"]

# Iterate through the creatures array, for each creature:

# After a block move finishes (all creatures have moved one position of the array), print the board and the scores. Indicate the move number
# I a move of a creature is landing in a position where another creature is already in, a battle is triggered
# Do not proceed with the move of the creature, change both creatures to the battle icon "🤺", calculate the battle result and print the board and the scores. Indicate that it is a battle.
# Resume the moves of the crature that was stopped by the battle.

for i in range(NUM_MOVES):
    for creature in creatures:
        # Get the current position of the creature 
        current_position = creature["start"]

        # Get the next move of the creature
        next_move = creature["moves"][i]

        # Get the next position of the creature
        next_position = [current_position[0] + directions[next_move][0], current_position[1] + directions[next_move][1]]

        # Check if the next position is out of the board
        if next_position[0] < 0 or next_position[0] > 4 or next_position[1] < 0 or next_position[1] > 4:
            print(f"{creature['name']} is out of the board")
            continue

        # Check if the next position is occupied by another creature
        if board[next_position[0]][next_position[1]] != "⬜️":
            # Print the battle message
            print("")
            # Print the original creature move
            print(f"{creature['name']} is moving {next_move}")
            print(f"{creature['name']} is battling {get_name(board[next_position[0]][next_position[1]])}")

            # Get the name of the creature in the next position
            other_creature = get_name(board[next_position[0]][next_position[1]])
            # Store current icons
            current_icon = creature["icon"]
            other_icon = board[next_position[0]][next_position[1]]
            # Change icons in the board to battle icon
            board[current_position[0]][current_position[1]] = "🤺"
            board[next_position[0]][next_position[1]] = "🤺"
            # Trigger battle
            battle(creature["name"],other_creature)
            print_board()
            print(f"Scores: {scores}")
            print("")
            # Restore creatures icons
            board[current_position[0]][current_position[1]] = current_icon
            board[next_position[0]][next_position[1]] = other_icon
            continue

        # Update the board with the new position of the creature
        board[current_position[0]][current_position[1]] = "⬜️"
        board[next_position[0]][next_position[1]] = creature["icon"]
        # Update the start position of the creature
        creature["start"] = next_position
    
    print(f"Move {i+1}")
    print_board()
    print(f"Scores: {scores}")
    print("")
