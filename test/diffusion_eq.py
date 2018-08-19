import time
from flask import views
grid_shape = (1024, 1024)

def evolve(grid, dt, D=1.0):
    xmax, ymax = grid_shape
    new_grid = [[0.0,] * ymax for x in xrange(xmax)]
    for i in xrange(xmax):
        for j in xrange(ymax):
            grid_xx = grid[(i+1)%xmax][j] + grid[(i-1)%xmax][j] - 2.0 * grid[i][j]
            grid_yy = grid[i][(j+1)%ymax] + grid[i][(j-1)%ymax] - 2.0 * grid[i][j]
            new_grid[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt
    return new_grid



def run_experiment(num_iterations):
    # Setting up initial conditions
    xmax, ymax = grid_shape
    grid = [[0.0,] * ymax for x in xrange(xmax)]
    block_low = int(grid_shape[0] * .4)
    block_high = int(grid_shape[0] * .5)
    for i in xrange(block_low, block_high):
        for j in xrange(block_low, block_high):
            grid[i][j] = 0.005

        # Evolve the initial conditions
        start = time.time()
        # print(start)
        for i in range(num_iterations):
            grid = evolve(grid, 0.1)
        print(time.time() - start)
        return time.time() - start

run_experiment(5)