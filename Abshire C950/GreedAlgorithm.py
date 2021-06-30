
#imports graph function and variable from edgeweights
from EdgeWeights import weights




#finds the route using the nearest neighbor algorithm to find the best route
#packages were sorted by some priority
#those without a deadline or special instruction were loaded manually by assigning them to a truck as 1,2,or 3 special note
#While and for loop combined make an N^2 function
def greedy(route):
    path = "4001 South 700 East"
    edge = weights.edge_weights


#normal route without looking for nearest neighbor
    normal = route

#best route using greedy algorithm
    best = [path]

    while len(normal) != 0:
        min = [0, path]
        for place in normal:
            miles = edge[best[-1], place]

          #  for address in all_addresses:
           #   for box in weights.delivery_dict[address]:
           #     if box[7] == "W":
                    

#if mail box is at same location currently then deliver and initiates hub
            if min[0] == 0:
                min = [miles, place]

#if looks for closest location next to go to, sets the lowest miles of options as new min
            if miles < min[0]:
                  min = [miles, place]

            if miles != 0 and miles < min[0]:
                  min = [miles, place]

        #if min[1] == "410 S State St" and len(normal) != 1:
           # continue 

#removes already been to locations where boxes were delivered and restarts algorithm
        if min[1] not in best:
            best.append(min[1])
        normal.remove(min[1])

#Returns the best route to take to deliver the mail using nearest neighbor. 
    return best

