import random
# North = 1
# East = 2
# South = 3
# West = 4
def valid_direction(coord, step_direction, size):
    result = True
    if step_direction == 1:
        if coord[1] < 1:
            return False
    elif step_direction == 2:
        if coord[0] > size-1:
            return False
    elif step_direction == 3:
        if coord[1] > size-1:
            return False
    elif step_direction == 4:
        if coord[0] < 1:
            return False
    return result


def perform_step(lattice, cluster_sites, size):
    step_direction = random.randint(1,4)
    while not valid_direction(coord, step_direction, size):
        step_direction = random.randint(1,4)
        
    if step_direction == 1:
        new_coord = (coord[0], coord[1]-1)
    elif step_direction == 2:
        new_coord = (coord[0]+1, coord[1])
    elif step_direction == 3:
        new_coord = (coord[0], coord[1]+1)
    elif step_direction == 4:
        new_coord = (coord[0]-1, coord[1])
        
    if # new_coord is adjacent to a cluster site:
        # create a new cluster site
    else:
        # perform another step
            
    return active_sites


def run_dla():
    # Make a lattice with sites set to 0
    size = 150
    lattice = [[0 for i in range(size)] for j in range(size)]
    max_sites = 9000
    lattice[size//2)][size//2] = 1
    cluster_sites = [(size//2, size//2)]

    while cluster_sites < max_sites:
        active_sites = perform_step(lattice, cluster_sites, size)

    print(lattice)
    return


run_dla()
