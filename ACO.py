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

#distance_matrix = [[0, 130.64838307457157, 243.40295807569802, 297.9681191000138, 334.2005385992069, 404.47744065645986, 362.3534186398687, 290.42899304305007, 274.4157429886266, 204.0833163195855, 143.22360140703069, 259.89613309935953, 92.19544457292888, 285.08595195133694],
 #                  [130.64838307457157, 0, 113.0044246921332, 167.36188335460378, 215.20455385516357, 305.8512710452582, 285.112258592997, 258.0271303564802, 194.48650338776727, 102.4158190906073, 108.46197490364999, 222.81157959136684, 147.02720836634285, 298.5180061570826],
  ##                [297.9681191000138, 167.36188335460378, 54.91812087098393, 0, 117.15374513859982, 237.30360300678115, 264.62237244798484, 310.8311438707518, 204.26698215815497, 146.44111444536335, 227.1607360438859, 281.27744310555727, 298.83942176359534, 390.15509736513764],
    #               [334.2005385992069, 215.20455385516357, 140.45995870709916, 117.15374513859982, 0, 120.14990636700472, 157.0031846810758, 234.6422809299296, 126.56223765404908, 132.9661611087573, 216.81558984537992, 213.7755832643195, 301.01494979485653, 329.16864978305574],
     #              [404.47744065645986, 305.8512710452582, 255.66579747787932, 237.30360300678115, 120.14990636700472, 0, 81.25269226308751, 202.20039564748632, 134.6476884316994, 205.65018842685265, 265.97932250458865, 199.69977466186586, 346.9437994834322, 302.9521414349138],
      #             [362.3534186398687, 285.112258592997, 266.3174797117155, 264.62237244798484, 157.0031846810758, 81.25269226308751, 0, 123.40583454602137, 91.23595782365635, 183.43936327844145, 219.20994502987315, 127.2242115322394, 292.43802762294786, 223.0560467685196],
       #            [290.42899304305007, 258.0271303564802, 289.882734911895, 310.8311438707518, 234.6422809299296, 202.20039564748632, 123.40583454602137, 0, 109.87720418721983, 178.4628812946827, 158.1455026233753, 35.22782990761707, 204.658251727117, 101.11874208078342],
        #           [274.4157429886266, 194.48650338776727, 191.48106956041374, 204.26698215815497, 126.56223765404908, 134.6476884316994, 91.23595782365635, 109.87720418721983, 0, 94.20191080864548, 132.77424449041314, 87.23531395025755, 212.34876971623828, 202.6277374892194],
         #          [204.0833163195855, 102.4158190906073, 113.6001760562016, 146.44111444536335, 132.9661611087573, 205.65018842685265, 183.43936327844145, 178.4628812946827, 94.20191080864548, 0, 87.36704184073076, 144.89996549343965, 169.49926253526888, 246.2194143441983],
          #         [143.22360140703069, 108.46197490364999, 183.91846019364124, 227.1607360438859, 216.81558984537992, 265.97932250458865, 219.20994502987315, 158.1455026233753, 132.77424449041314, 87.36704184073076, 0, 124.14910390333068, 84.64632301523794, 190.11838417154718],
           #        [259.89613309935953, 222.81157959136684, 257.41989045137905, 281.27744310555727, 213.7755832643195, 199.69977466186586, 127.2242115322394, 35.22782990761707, 87.23531395025755, 144.89996549343965, 124.14910390333068, 0, 177.40913167027227, 115.39497389401325],
            #       [92.19544457292888, 147.02720836634285, 249.50551096118093, 298.83942176359534, 301.01494979485653, 346.9437994834322, 292.43802762294786, 204.658251727117, 212.34876971623828, 169.49926253526888, 84.64632301523794, 177.40913167027227, 0, 193.0025906561878],
             #      [285.08595195133694, 298.5180061570826, 359.35636908228025, 390.15509736513764, 329.16864978305574, 302.9521414349138, 223.0560467685196, 101.11874208078342, 202.6277374892194, 246.2194143441983, 190.11838417154718, 115.39497389401325, 193.0025906561878, 0]]
#num_cities = len(distance_matrix)
#aco = AntColonyOptimizer(num_ants=20, num_iterations=100, alpha=1.0, beta=2.0, rho=0.5, q=100, distance_matrix=distance_matrix)
#aco.optimize()

#print("Best tour:", aco.best_tour)
 #       print("Best tour length:", aco.best_length)





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