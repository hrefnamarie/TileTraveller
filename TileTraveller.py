#  Give a variable the name "Starting Tile" 
#  Give option of movement.
#  When user moves the variable changes to the tile he is placed in and the loop starts again.
#  if user tries to use movement not available print ("Not a valid direction")
#  When user arrives in tile 3.1 print ("Victory") and end the loop.
N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"
tile = 1.1
def move(movement):
    if movement == "n" or movement == "N":
        tile += 0.1
    if movement == "e" or movement == "E":
        tile += 1
    if movement == "s" or movement == "S":
        tile -= 0.1
    if movement == "w" or movement == "W":
        tile -= 1
def is_valid_movement(tile):
    if tile == 1.1 or tile == 2.1 or tile == 3.1:
        print("You can travel: {}".format(N))
    if tile == 1.2:
        print("You can travel: {} or {} or {}".format(N, E, S))
    if tile == 1.3:
        print("You can travel: {} or {}".format(E, S))
    if tile == 2.3:
        print("You can travel: {} or {}".format(E, W))
    if tile == 2.2 or tile == 3.3:
        print("You can travel: {} or {}".format(S, W))
    if tile == 3.2:
        print("You can travel: {} or {}".format(N, S))

    
    direction = input("Direction: ")
    movement()
