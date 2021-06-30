#Kaitlynn Abshire #000970207


from Hashtable import mail_hashtable
from GreedAlgorithm import greedy
from datetime import datetime, timedelta, time
from EdgeWeights import weights

#Truck class arranges all trucks with mail, sets them on route, and manages the times of deliveries. 
class Trucks:

    def __init__(self):

        self.begin = None
        self.current = None
        self.end = None
        self.mpm = 0.3
        self.mail = []
        self.path = []

# defines the variable insert to put boxes on trucks and sets initial address
    def insert(self, box):
        self.mail.append(box)  
        self.path.append(box[1])  

# defines the variable delete to remove boxes on trucks and remove the address
    def delete(self, box):
        self.mail.remove(box) 
        self.path.remove(box[1]) 

# Initiates the delivering of boxes of mail
    def begin_delivering(self, time):
        self.start_time = time

# Changes the time to most recent
    def update_time(self, time):
        self.current_time = time
        return time

# End day and routes 
    def end_delivery(self, time):
        self.finish_time = time
        return time


# Initializes trucks as objects to place mail inside
truck1 = Trucks()
truck2 = Trucks()
truck3 = Trucks()

# Create an iterable list of locations used in load_trucks_and_get_best_route()
all_addresses = []

#delayed_mail = []

#nondelayed_mail = []
# Put the packages in the graph's delivery_dict to associate locations with packages
weights.box__dict(mail_hashtable)


#Puts trucks through greedy algorithm after loading
# n^2
def load_trucks_efficiently():

    for location in weights.delivery_dict:
        all_addresses.append(location)

  #  for row in weights.delivery_dict:
      #  if row[7] == "Delay":
       #     delayed_mail.append(row)

   # for row in weights.delivery_dict:
     #   if row[7] != "Delay":
      #      nondelayed_mail.append(row)

#Truck 1 loading by packages that needed to stay together or manually designated as 1
    for address in all_addresses:
        for box in weights.delivery_dict[address]:
            if box[7] == "1" or box[7] == "U":
                truck1.insert(box)

             
#Truck 2 loading by packages that needed to stay on truck 2, were delayed, or manually designated as 2


    for address in all_addresses:
       for box in weights.delivery_dict[address]:
           if box[7] == "2" or box[7] == "Delay":
             truck2.insert(box)


#Truck 3 loading packages manually designated as 3 in special notes
    for address in all_addresses:
        for box in weights.delivery_dict[address]:
            if box[7] == "3" or box[7] == "4":
                truck3.insert(box)

            
#Starts trucks at hub
    truck1_original_route = truck1.path
    truck1_original_route.append("4001 South 700 East")
    truck2_original_route = truck2.path
    truck2_original_route.append("4001 South 700 East")
    truck3_original_route = truck3.path
    truck3_original_route.append("4001 South 700 East")



# Runs trucks through greedy neighbor path
    truck1.path = greedy(truck1.path)
    truck2.path = greedy(truck2.path)
    truck3.path = greedy(truck3.path)

 

# Sends trucks back to hub
    truck1.path.append("4001 South 700 East")
    truck2.path.append("4001 South 700 East")
    truck3.path.append("4001 South 700 East")


    print("All truck & package data after loading: ")
    print("Truck 1 has", len(truck1.mail), "packages")
    print("Truck 1 packages:", *truck1.mail, sep="\n")
    print("Truck 2 has", len(truck2.mail), "packages")
    print("Truck 2 packages:", *truck2.mail, sep="\n")
    print("Truck 3 has", len(truck3.mail), "packages")
    print("Truck 3 packages:", *truck3.mail, sep="\n")


# Calculates the miles a truck took in greedy path.
# One for loop so total N
def total_miles(location):
    edge_weight_list = weights.edge_weights
    miles = 0
    for i in range(0, len(location) - 1):
        miles = miles + edge_weight_list[location[i], location[i+1]]
    return miles



# Calculates how many miles all trucks take in the greedy path.
# One Loop of total miles so N
def all_total_miles():
    t1_miles = total_miles(truck1.path)
    t2_miles = total_miles(truck2.path)
    t3_miles = total_miles(truck3.path)
    total = t1_miles + t2_miles + t3_miles
    print("Truck 1 total miles = ", round(t1_miles, 2), "+ Truck 2 total miles = ", round(t2_miles, 2),
          "+ Truck 3 total miles = ", round(t3_miles, 2), " Total of all trucks =", round(total, 2), "miles.")

   
# Formats time display for packages that were delivered.
# One loop so N
def time_format(time, sec):
    date = datetime(100, 1, 1, time.hour, time.minute, time.second)
    date = date + timedelta(seconds = sec)
    return date.time()


# Starts the delivery of all boxed mail in their designated trucks
# Two for loops so it is N^2
def send_mail():
    miles_between = weights.edge_weights

    # Code for truck 1 mail to be sent
    truck1_start = datetime(2021, 6, 12, 8, 0, 0)
    truck1.start_time = truck1_start
    truck1.current_time = truck1_start
    for i in range(0, len(truck1.path) - 1):
        distance = miles_between[truck1.path[i], truck1.path[i+1]]
        speed = truck1.mpm
        minutes_decimal = distance/speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = time_format(truck1.current_time, seconds_to_add)
        truck1.current_time = datetime(2021, 6, 12, delivered_time.hour, delivered_time.minute, delivered_time.second)
        updated_delivery_status = "delivered :", str(delivered_time)
        for box in truck1.mail:
            if truck1.path[i+1] == box[1]:
                box[8] = updated_delivery_status
    truck1.finish_time = truck1.current_time
    print("Truck 1 Delivery:", *truck1.mail, sep="\n") 

    # Code for truck 2 mail to be sent
    truck2_start = datetime(2021, 6, 12, 9, 5, 0)
    truck2.start_time = truck2_start
    truck2.current_time = truck2_start
    for i in range(0, len(truck2.path) - 1):
        distance = miles_between[truck2.path[i], truck2.path[i + 1]]
        speed = truck2.mpm
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = time_format(truck2.current_time, seconds_to_add)
        truck2.current_time = datetime(2021, 6, 12, delivered_time.hour, delivered_time.minute, delivered_time.second)
        updated_delivery_status = "delivered :", str(delivered_time)
        for box in truck2.mail:
            if truck2.path[i + 1] == box[1]:
                box[8] = updated_delivery_status
    truck2.finish_time = truck2.current_time
    print("Truck 2 Delivery:", *truck2.mail, sep="\n") 

    # Code for truck 3 mail to be sent
    truck3_start = truck1.finish_time
    truck3.start_time = truck3_start
    truck3.current_time = truck3_start
    for i in range(0, len(truck3.path) - 1):
        distance = miles_between[truck3.path[i], truck3.path[i + 1]]
        speed = truck3.mpm
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = time_format(truck3.current_time, seconds_to_add)
        truck3.current_time = datetime(2021, 6, 12, delivered_time.hour, delivered_time.minute, delivered_time.second)
        updated_delivery_status = "delivered :", str(delivered_time)
        for box in truck3.mail:
            if truck3.path[i + 1] ==  box[1]:
                box[8] = updated_delivery_status
    truck3.finish_time = truck3.current_time
    print("Truck 3 Delivery:", *truck3.mail, sep="\n") 


# Modifies field 8 on the hashtable to out for delivery
# One for loop so it is N
def en_route(mail):
    for box in mail:
        if len(box) < 9:
            box.append("en_route")
        elif len(box) == 9:
            box[8] = "en_route"

# Calls specific delivery times of the boxed mail for the consumer to view.
# Two for loops so it is N^2
def delivery_stat(hour, min, sec):
    miles_between = weights.edge_weights
    stop_time = datetime(2021, 6, 12, hour, min, sec)

     # Code for truck 1 mail to be sent and switched to en route
    truck1_start = datetime(2021, 6, 12, 8, 0, 0)
    truck1.start_time = truck1_start
    truck1.current_time = truck1_start
    en_route(truck1.mail)
    for i in range(0, len(truck1.path) - 1):
        distance = miles_between[truck1.path[i], truck1.path[i + 1]]
        speed = truck1.mpm
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = time_format(truck1.current_time, seconds_to_add)
        if delivered_time < stop_time.time():
            truck1.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute, delivered_time.second)
            updated_delivery_status = "delivered :", str(delivered_time)
            for box in truck1.mail:
                if truck1.path[i + 1] ==  box[1]:
                     box[8] = updated_delivery_status
    truck1.finish_time = truck1.current_time
    print("Truck 1 Delivery:", *truck1.mail, sep="\n")  

   # Code for truck 2 mail to be sent and switched to en route
    truck2_start = datetime(2021, 6, 12, 9, 5, 0)
    truck2.start_time = truck2_start
    truck2.current_time = truck2_start
    en_route(truck2.mail)

    for i in range(0, len(truck2.path) - 1):
        distance = miles_between[truck2.path[i], truck2.path[i + 1]]
        speed = truck2.mpm
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = time_format(truck2.current_time, seconds_to_add)
        if delivered_time < stop_time.time():
            truck2.current_time = datetime(2021, 6, 12, delivered_time.hour, delivered_time.minute, delivered_time.second)
            updated_delivery_status = "delivered :", str(delivered_time)
            for box in truck2.mail:
                if truck2.path[i + 1] ==  box[1]:
                     box[8] = updated_delivery_status
    truck2.finish_time = truck2.current_time
    print("Truck 2 Delivery:", *truck2.mail, sep="\n")  

    # Code for truck 3 mail to be sent and switched to en route
    truck3_start = datetime(2021, 6, 12, 9, 5, 0)
    truck3.start_time = truck3_start
    truck3.current_time = truck3_start
    en_route(truck3.mail)
    for i in range(0, len(truck3.path) - 1):
        distance = miles_between[truck3.path[i], truck3.path[i + 1]]
        speed = truck3.mpm
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = time_format(truck3.current_time, seconds_to_add)
        if delivered_time < stop_time.time():
            truck3.current_time = datetime(2021, 6, 12, delivered_time.hour, delivered_time.minute, delivered_time.second)
            updated_delivery_status = "delivered :", str(delivered_time)
            for box in truck3.mail:
                if truck3.path[i + 1] == box[1]:
                    box[8] = updated_delivery_status
    truck3.finish_time = truck3.current_time
    print("Truck 3 Delivery:", *truck3.mail, sep="\n") 




