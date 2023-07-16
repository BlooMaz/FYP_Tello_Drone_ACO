import pywhatkit
from datetime import datetime
import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import random
from timeit import default_timer as timer
#temperary array to store coordinates
coordinate_temp =[]



class Ant:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.tour = []
        self.visited = [False] * num_cities

    #function for if ant has visited a node it will be true
    def visit_city(self, city):
        self.tour.append(city)
        self.visited[city] = True

    #checks if the node is visited,true if visited
    def is_visited(self, city):
        return self.visited[city]

    #find the length for the tour
    def tour_length(self, distance_matrix):
        length = 0
        for i in range(self.num_cities - 1):
            length += distance_matrix[self.tour[i]][self.tour[i+1]]
        length += distance_matrix[self.tour[-1]][self.tour[0]]
        return length

class AntColonyOptimizer:
    #contructor
    def __init__(self, num_ants, num_iterations, alpha, beta, rho, q, distance_matrix):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha  # influence of pheromone
        self.beta = beta    # influence of heuristic information
        self.rho = rho      # pheromone evaporation rate
        self.q = q          # pheromone deposit factor
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        self.pheromone_matrix = [[1.0] * self.num_cities for _ in range(self.num_cities)]
        self.best_tour = None
        self.best_length = float('inf')
        self.ants = []  # List to store the ants

    #ants contructor
    def construct_ants(self):
        self.ants = [Ant(self.num_cities) for _ in range(self.num_ants)]

    #tour for ants
    def construct_tour(self, ant):
        ant.visit_city(random.randint(0, self.num_cities - 1))
        while len(ant.tour) < self.num_cities:
            city = self.select_next_city(ant)
            ant.visit_city(city)

    def select_next_city(self, ant):
        current_city = ant.tour[-1]
        unvisited_cities = [i for i in range(self.num_cities) if not ant.is_visited(i)]
        #using the probability function to calculate probabiliy that an ant will visit to the next city
        probabilities = [self.calculate_probability(current_city, city) for city in unvisited_cities]
        total = sum(probabilities)
        #normalize the probabilities in the probabilities list
        probabilities = [p / total for p in probabilities]
        return random.choices(unvisited_cities, probabilities)[0]

    def calculate_probability(self, current_city, next_city):
        pheromone = self.pheromone_matrix[current_city][next_city]
        distance = self.distance_matrix[current_city][next_city]
        return (pheromone ** self.alpha) * ((1 / distance) ** self.beta)

    def update_pheromone(self):
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                self.pheromone_matrix[i][j] *= (1 - self.rho)
        for ant in self.ants:
            tour = ant.tour
            for i in range(self.num_cities - 1):
                current_city = tour[i]
                next_city = tour[i+1]
                self.pheromone_matrix[current_city][next_city] += self.q / self.distance_matrix[current_city][next_city]

    def optimize(self):
        for _ in range(self.num_iterations):
            self.construct_ants()
            for ant in self.ants:
                self.construct_tour(ant)
                length = ant.tour_length(self.distance_matrix)
                if length < self.best_length:
                    self.best_length = length
                    self.best_tour = ant.tour
            self.update_pheromone()


# Example usage

distance_matrix = [
    [0, 637.18, 263.91, 561.06, 179.71, 365.86, 838.72, 240.28, 547.88, 316.63, 730.16, 309.49, 291.76, 912.33, 260.07],
    [637.18, 0, 660.34, 241.54, 819.22, 306.12, 978.39, 561.57, 175.75, 196.37, 937.85, 633.48, 788.82, 598.48, 510.73],
    [263.91, 660.34, 0, 453.11, 476.48, 224.88, 709.45, 353.86, 417.01, 401.38, 761.04, 302.29, 406.71, 928.53, 467.43],
    [561.06, 241.54, 453.11, 0, 791.23, 278.61, 822.35, 673.62, 268.3, 403.84, 838.92, 472.64, 743.3, 365.03, 340.31],
    [179.71, 819.22, 476.48, 791.23, 0, 647.82, 808.03, 126.93, 733.4, 558.22, 922.75, 463.14, 323.2, 1067.37, 431.83],
    [365.86, 306.12, 224.88, 278.61, 647.82, 0, 616.84, 358.52, 429.46, 235.17, 659.07, 115.88, 465.46, 756.23, 205.96],
    [838.72, 978.39, 709.45, 822.35, 808.03, 616.84, 0, 911.07, 798.94, 778.12, 278.45, 760.55, 696.57, 1202.23, 779.78],
    [240.28, 561.57, 353.86, 673.62, 126.93, 358.52, 911.07, 0, 689.77, 466.67, 971.82, 413.91, 137.65, 1207.57, 452.68],
    [547.88, 175.75, 417.01, 268.3, 733.4, 429.46, 798.94, 689.77, 0, 285.43, 762.55, 618.48, 614.53, 542.95, 618.15],
    [316.63, 196.37, 401.38, 403.84, 558.22, 235.17, 778.12, 466.67, 285.43, 0, 639.71, 492.53, 432.12, 624.41, 314.84],
    [730.16, 937.85, 761.04, 838.92, 922.75, 659.07, 278.45, 971.82, 762.55, 639.71, 0, 612.5, 856.01, 1325.64, 855.33],
    [309.49, 633.48, 302.29, 472.64, 463.14, 115.88, 760.55, 413.91, 618.48, 492.53, 612.5, 0, 449.05, 741.84, 184.68],
    [291.76, 788.82, 406.71, 743.3, 323.2, 465.46, 696.57, 137.65, 614.53, 432.12, 856.01, 449.05, 0, 1053.84, 412.9],
    [912.33, 598.48, 928.53, 365.03, 1067.37, 756.23, 1202.23, 1207.57, 542.95, 624.41, 1325.64, 741.84, 1053.84, 0, 910.99],
    [260.07, 510.73, 467.43, 340.31, 431.83, 205.96, 779.78, 452.68, 618.15, 314.84, 855.33, 184.68, 412.9, 910.99, 0]
]

coo = [
    [285, 769],
    [673, 141],
    [475, 624],
    [829, 285],
    [186, 940],
    [613, 363],
    [940, 732],
    [112, 599],
    [829, 401],
    [516, 238],
    [791, 876],
    [349, 493],
    [68, 835],
    [949, 65],
    [524, 181]
]
num_cities = len(distance_matrix)
aco = AntColonyOptimizer(num_ants=100, num_iterations=100, alpha=1.0, beta=2.0, rho=0.5, q=100, distance_matrix=distance_matrix)
start = timer()
aco.optimize()

print("Best tour:", aco.best_tour)
for i in range(len(aco.best_tour)):
    print(coo[aco.best_tour[i]])
print("Best tour length:", aco.best_length)

end = timer()
print(end - start, "seconds")


#send notification
keyboard = Controller()
def send_whatsapp_message(msg: str):
    try:

        pywhatkit.sendwhatmsg_instantly(
            phone_no="+601159159119",
            message=msg,
        )
        time.sleep(5)
        pyautogui.click(1050, 1000)
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))

#send_whatsapp_message(msg="This is a message from python script")