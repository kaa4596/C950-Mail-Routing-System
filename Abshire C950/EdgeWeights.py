#importing csv to class so it can read the text file format
import csv

#weight class imports the distances csv data into a format readable by the algorithm
class Weights_Class:

#initializes the lists needed to create the arrays for data
    def __init__(self):
        self.delivery_dict = {}  
        self.edge_weights = {}

#adds a vertex node to a graph so edges can be conected
    def add_point(self, point):
        self.delivery_dict[point] = []

#adds the edgeweights connecting the points on the graph to each other
    def add_weight(self, point_a, point_b, weight=1.0):
        self.edge_weights[(point_a, point_b)] = weight

#creates a dictionary system that defines a box of mail with its point
#has a double for loop making it N^2
    def box__dict(self, ht):
        for bucket in ht.table:
            for item in bucket:
                self.delivery_dict[item[1]].append(item)

#getter for the distance text file
#has a single for loop so it is just N
def get_distances(name):
    data = []
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            data.append(row)
    return data

#compiles all the information together into a data graph
#two for loops so it is N^2
def create_graph(name):
    data = get_distances(name)
    graph = Weights_Class()
    for row in data:
        graph.add_point(row[1]) 
    for row in data:
        for i in range(3, len(row)):  
            graph.add_weight(row[1], data[i-3][1], float(row[i])) 
    return graph

#makes a variable that is easy to call/manipulate the graph
weights = create_graph("Distances.csv")
