import math
import ACO
from timeit import default_timer as timer
import test as ts
i=0
#temperary array to store coordinates
coordinate_temp =[]
#to store xy value when splitting string from reading lines from txt files
xy_value = []




def calculate():
    for i in range(2):
        start = timer()
        filename = 'coordinates' + str(i) + '.txt'
        fh = open(filename, 'r')
        temp = fh.readline()
        # split the string with ,
        coordinate_temp = temp.split(",")
        coordinate_temp.pop()
        # making 2d array for the coordinates
        coordinate = [[0 for k in range(2)] for l in range(len(coordinate_temp))]
        j = 0
        for j in range(len(coordinate_temp)):
            xy_value = coordinate_temp[j].split(" ")
            coordinate[j][0] = int(xy_value[0])
            coordinate[j][1] = int(xy_value[1])
            # clear the list for next iteration
            xy_value.clear()
        # making 2d array for distance to input into matrix of ACO
        # size of xy_distance = number of coordinates ^ 2
        # if there is 5 coordinates then array is xy_distance[5][5]
        xy_distance = [[0 for k in range(len(coordinate))] for l in range(len(coordinate))]
        m = 0
        n = 0
        for m in range(len(coordinate)):
            for n in range(len(coordinate)):
                if m == n:
                    xy_distance[m][n] = 0
                else:
                    xy_distance[m][n] = math.dist(coordinate[m], coordinate[n])
        print(xy_distance)
        print(coordinate)



        # Using ACO calculate the best tour
        num_cities = len(xy_distance)
        aco = ACO.AntColonyOptimizer(num_ants=10, num_iterations=10, alpha=1.0, beta=2.0, rho=0.3, q=100,
                                     distance_matrix=xy_distance)
        aco.optimize()
        end = timer()
        print("Best tour:", aco.best_tour)
        print("Best tour length:", aco.best_length)
        coordinate_new = [[0 for k in range(2)] for l in range(len(coordinate))]
        for mb in range(len(coordinate)):
            coordinate_new[mb][0] = coordinate[aco.best_tour[mb]][0]
            coordinate_new[mb][1] = coordinate[aco.best_tour[mb]][1]

        print("New coordinates: ",coordinate_new)
        print(end - start, "seconds")

        ts.start_plotting(coordinate_new,i)
        # clear both list before next iteration
        xy_distance.clear()
        coordinate.clear()
        if i == 1:
            print("All done")
        else:
            print("Continuing...")
            print("  ")

if __name__ == "__Calculate_distance_matrix_4Drones__":
    calculate()


