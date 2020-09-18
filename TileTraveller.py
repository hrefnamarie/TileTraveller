#  Give a variable the name "Starting Tile" 
#  Give a variable the name "Starting Tile" 
#  Give option of movement.
#  When user moves the variable changes to the tile he is placed in and the loop starts again.
#  if user tries to use movement not available print ("Not a valid direction")
#  When user arrives in tile 3.1 print ("Victory") and end the loop.

N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"

current_tile = 1.1

def move(movement, tile):
    if movement == "n" or movement == "N":
        tile += 0.1

    if movement == "e" or movement == "E":
        tile += 1
    
    if movement == "s" or movement == "S":
        tile -= 0.1
    
    if movement == "w" or movement == "W":
        tile -= 1

    return round(tile, 1)

def get_valid_movement(tile):
    if tile == 1.1 or tile == 2.1 or tile == 3.1:
        travel = "You can travel: {}".format(N)

    if tile == 1.2:
        travel = "You can travel: {} or {} or {}.".format(N, E, S)

    if tile == 1.3:
        travel = "You can travel: {} or {}.".format(E, S)
    
    if tile == 2.3:
        travel = "You can travel: {} or {}.".format(E, W)
    
    if tile == 2.2 or tile == 3.3:
        travel = "You can travel: {} or {}.".format(S, W)

    if tile == 3.2:
        travel = "You can travel: {} or {}.".format(N, S)

    return travel

def is_valid_movement(movement, tile):
    movement = movement.lower()
    if tile == 1.1 or tile == 2.1 or tile == 3.1:
        if movement == "n":
            return True

    if tile == 1.2:
        if movement != "w":
            return True

    if tile == 1.3:
        if movement == "e" or movement == "s":
            return True
    
    if tile == 2.3:
        if movement == "e" or movement == "w":
            return True
    
    if tile == 2.2 or tile == 3.3:
        if movement == "s" or movement == "w":
            return True

    if tile == 3.2:
        if movement == "n" or movement == "s":
            return True
    else:
        return False


while True:
    if current_tile== 3.1:
        print("Victory!")
        break

    print(get_valid_movement(current_tile))
    
    direction = input("Direction: ")

    if is_valid_movement(direction, current_tile) == False:
        print("Not a valid direction!")

    if is_valid_movement(direction, current_tile) == True:
        current_tile = move(direction, current_tile)

