def get_direction(full_direction) :
    dir = full_direction[1:]
    if dir == 'N' :
        return [0,1]
    elif dir == 'S' :
        return [0,-1]
    elif dir == 'E' :
        return [1,0]
    elif dir == 'W' :
        return [-1,0]
    elif dir == 'NE' :
        return [1,1]
    elif dir == 'NW' :
        return [-1,1]
    elif dir == 'SE' :
        return [1,-1]
    else :
        return [-1,-1]

def terminus (initial_lattice_point ,directions) :
    start_x = initial_lattice_point[0]
    start_y = initial_lattice_point[1]
    for i in directions :
        list_directions = get_direction(i)
        steps = int(i[0])
        start_x += steps*list_directions[0]
        start_y += steps*list_directions[1]
    final_lattice_point=[start_x,start_y]
    return final_lattice_point

print(terminus((1, 1), ["1N", "3NW"]))
print(terminus((-1, 1), ["1NE"]))
