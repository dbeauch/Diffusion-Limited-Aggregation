import random
import time
random.seed(int(time.time()))
import numpy as np
import matplotlib.pyplot as plt


def valid_direction(coord, step_direction, size):
    x, y = coord
    if step_direction == 1:  # North
        return y > 0
    elif step_direction == 2:  # East
        return x < size-1
    elif step_direction == 3:  # South
        return y < size-1
    elif step_direction == 4:  # West
        return x > 0


def perform_step(coord, cluster_sites, size):
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

    return new_coord


def adjacent(coord, cluster_sites):
    adjacent_sites = [(coord[0]-1, coord[1]), (coord[0]+1, coord[1]), (coord[0], coord[1]-1), (coord[0], coord[1]+1)]
    for site in adjacent_sites:
        if site in cluster_sites:
            return True
    return False


def generate_border_site(cluster_sites, size):
    index = random.randint(1,size-1)
    border_options = [(0,index), (index,size-1), (size-1, index), (index, 0)]
    return random.choice(border_options)
 

def run_walker(cluster_sites, size):
    # Initialize a walker
    coord = generate_border_site(cluster_sites, size)
    while coord in cluster_sites:
        coord = generate_border_site(cluster_sites, size)

    # Randomly walk until clustered
    while not adjacent(coord, cluster_sites):
        coord = perform_step(coord, cluster_sites, size)
        
    return coord


def run_dla():
    # Initialize cluster and seed
    # 150x150 could not fit 9000 sites
    size = 150
    max_sites = 4000
    cluster_sites = {(size//2, size//2)}
    
    # Run walkers
    while len(cluster_sites) < max_sites:
        new_coord = run_walker(cluster_sites, size)
        cluster_sites.add(new_coord)
        
        index = len(cluster_sites)
        if index % 10 == 0:
            print(f"Site {index} complete")

    with open('dla.txt', 'w') as f:
        for coord in cluster_sites:
            f.write(f"{coord[0]}\t{coord[1]}\n")


    coordinates = np.loadtxt('dla.txt', dtype=int)
    mesh = np.zeros((size, size), dtype=int)
    for x, y in coordinates:
        mesh[x, y] = 1
    fig, ax = plt.subplots()
    ax.imshow(mesh, cmap='binary', interpolation='nearest', origin='upper')
    
    ax.set_title('DLA Simulation')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    plt.savefig('dla_plot.png')
    plt.show()

    return


run_dla()
