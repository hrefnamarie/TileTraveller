N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"

def move(movement, current_tile):
    if movement == "n" or movement == "N":
        return tile + 0.1
    elif movement == "e" or movement == "E":
        return tile + 1
    elif movement == "s" or movement == "S":
        return tile - 0.1
    if movement == "w" or movement == "W":
        return tile - 1
    
def get_valid_movement(movement, tile):
    movement = movement.lower
    if tile == 1.1 or tile == 2.1 or tile == 3.1:
        if movement != "n":
            return False
    if tile == 1.2:
        if movement == "w":
            return False
    if tile == 1.3:
        if movement != "e" or movement != "s":
            return False
    if tile == 2.3:
        if movement != "e" or movement != "w":
            return False
    if tile == 2.2 or tile == 3.3:
        if movement != "s" or movement != "w":
            return False
    if tile == 3.2:
        if movement != "n" or movement != "s":
            return False
    return True

while is_valid_movement(movement, current_tile) == True:
    if tile == 1.1 or tile == 2.1 or tile == 3.1:
        travel = "You can travel: {}".format(N)
    if tile == 1.2:
        travel = "You can travel: {} or {} or {}".format(N, E, S)
    if tile == 1.3:
        travel = "You can travel: {} or {}".format(E, S)
    if tile == 2.3:
        travel = "You can travel: {} or {}".format(E, W)
    if tile == 2.2 or tile == 3.3:
        travel = "You can travel: {} or {}".format(S, W)
    if tile == 3.2:
        travel = "You can travel: {} or {}".format(N, S)
    else:
        print ("invalid direction")
    
current_tile = 1.1
    

if current_tile == 3.1:
    print("Victory!")
    
elif current_tile != 3.1:
    is_valid_movement(movement, current_tile)
    direction = input("Direction: ")
    move(movement, current_tile)


    





