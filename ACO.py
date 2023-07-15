import pywhatkit
from datetime import datetime
import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import random
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

#distance_matrix = [[0,57,36,53,32],
                  # [57,0,84,22,79],
                   #[36,84,0,64,37],
                   #[53,22,64,0,67],
                   #[32,79,37,67,0]]
#coo =[[23, 57],[89, 12],[46, 91],[75, 33],[10, 82]]
#num_cities = len(distance_matrix)
#aco = AntColonyOptimizer(num_ants=10, num_iterations=100, alpha=1.0, beta=2.0, rho=0.5, q=100, distance_matrix=distance_matrix)
#aco.optimize()

#print("Best tour:", aco.best_tour)
#for i in range(len(aco.best_tour)):
 #   print(coo[aco.best_tour[i]])
#print("Best tour length:", aco.best_length)





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