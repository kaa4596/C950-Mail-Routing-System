#Kaitlynn Abshire #000970207
#Data Structures and Algorithms II – C950
#Performance Assessment: Data Structures and Algorithms II - NHP2

from GreedAlgorithm import greedy
from Hashtable import print_result
from Trucks import load_trucks_efficiently, truck1, truck2, delivery_stat, all_total_miles, \
    send_mail, truck3


# Interface that the user uses to load trucks, view specific mail, and view total mileage.
def ui():

# Main Options
    main = input("Please select an action. \n"
                      "[1] Inset Mail on Trucks \n"
                      "[2] Find a Package By ID \n"
                      "[0] EXIT \n")

# exit
    if main == "0":
        print("0 was selected or an invalid option. Exiting program.")
        SystemExit

 #Load all boxes
    if main == "1":
        print("It is currently 8:00")
        print("Mail has been placed on the appropriate vehicles.")
        load_trucks_efficiently()
   
        status_1 = input("\nPlease select an action. \n"
                         "[1] View mail updates between 8:35 a.m. and 9:25 a.m \n"
                         "[2] Find a Package By ID \n"
                         "[0] EXIT \n")

# Exit
        if status_1 == "0":
            print("0 was selected or an invalid option. Exiting program.")
            SystemExit


# Update mail status 1
        if status_1 == "1":

            delivery_stat(9, 25, 0)

# Next: Fix the package #9 address
            print("\nIt was noted at 10:20 that the address for mail id: 9 is incorrect. Would you like to fix it?")
            fix_pkg = input("Enter 1 to fix it or 0 TO EXIT: ")

# Exit
            if fix_pkg == "0":
                print("0 was selected or an invalid option. Exiting program.")
                SystemExit

# Removes the incorrect package.
            if fix_pkg == "1":
                for package in truck3.mail:
                    if package[7] == "4":
                        truck3.delete(package)  
        
# UInserts the correct address with the package.
                updated_package_9 = ['9', '410 S State St', 'Salt Lake City', 'UT', '84111', '17:00', '2', 'W', 'en_route']
         
                truck3.path = greedy(truck3.path)  
                truck3.insert(updated_package_9) 
                truck3.path.append("4001 South 700 East") 

                print("Mail Id: 9 updated.")

#Next block of mail updates 2
                status_2 = input("\nPlease select an action below. \n"
                                 "[1] View mail updates between 9:35 a.m. and 10:25 a.m \n"
                                 "[2] Find a Package By ID \n"
                                 "[0] EXIT \n")

#Exits
                if status_2 == "0":
                    print("0 was selected or an invalid option. Exiting program.")
                    SystemExit

#View Updates
                if status_2 == "1":

                    delivery_stat(10, 25, 0)

#Next block of mail updates 3
                    status_3 = input("\nPlease select an action below. \n"
                                     "[1] View mail updates between 12:03 p.m. and 1:12 p.m (13:12) \n"
                                     "[2] Find a Package By ID \n"
                                     "[0] EXIT \n")

#Exit
                    if status_3 == "0":
                        print("0 was selected or an invalid option. Exiting program.")
                        SystemExit

#View Updates
                    if status_3 == "1":

                        delivery_stat(13, 12, 0)

#All deliveries finished update 4
                        final = input("\nAll trucks have completed deliveries view final times and mileage?\n"
                                      "[1] To see all mail deliveries, total mileage, and time finished\n"
                                      "[2] Find a Package By ID \n"
                                      "[0] EXIT\n")

# Exit
                        if final == "0" or final != "1":
                            print("0 was selected or an invalid option. Exiting program.")
                            SystemExit

# Finished results
                        if final == "1":

                            send_mail()
                            all_total_miles()
                            print("All trucks have returned by :", truck3.finish_time.time())
                            SystemExit

# Lookup funciton to find mail by id                        
                        if final == "2":
                            print("It is currently 9:34 AM.")

                        checker = "1"
                        while checker == "1":
                        # Prompt the user to get package ID to search for.
                            user_search_string = input("Please type and enter the ID of the mail you are looking for: ")
                            try:
                                user_search_int = int(user_search_string)
                                print_result(user_search_int)
                            except ValueError:
                                print("Not a valid number or does not exist.")
                            try_again = input("To look for another package enter 1. 0 to exit.")
                            if checker == "0":
                                print("0 was selected or an invalid option. Exiting program.")
                            checker = try_again

                        return final

# Lookup funciton to find mail by id                        
                    if status_3 == "2":
                        print("It is currently 9:34 AM.")

                    checker = "1"
                    while checker == "1":
                    # Prompt the user to get package ID to search for.
                        user_search_string = input("Please type and enter the ID of the mail you are looking for: ")
                        try:
                            user_search_int = int(user_search_string)
                            print_result(user_search_int)
                        except ValueError:
                            print("Not a valid number or does not exist.")
                        try_again = input("To look for another package enter 1. 0 to exit.")
                        if checker == "0":
                            print("0 was selected or an invalid option. Exiting program.")
                        checker = try_again

                    return status_3
                           
# Lookup funciton to find mail by id                        
                if status_2 == "2":
                    print("It is currently 9:34 AM.")

                checker = "1"
                while checker == "1":
                # Prompt the user to get package ID to search for.
                    user_search_string = input("Please type and enter the ID of the mail you are looking for: ")
                    try:
                        user_search_int = int(user_search_string)
                        print_result(user_search_int)
                    except ValueError:
                        print("Not a valid number or does not exist.")
                    try_again = input("To look for another package enter 1. 0 to exit.")
                    if checker == "0":
                      print("0 was selected or an invalid option. Exiting program.")
                    checker = try_again

                return status_2

# Lookup funciton to find mail by id
        if status_1 == "2":
            print("It is currently 8:34 AM.")

            checker = "1"
            while checker == "1":
                # Prompt the user to get package ID to search for.
                user_search_string = input("Please type and enter the ID of the mail you are looking for: ")
                try:
                    user_search_int = int(user_search_string)
                    print_result(user_search_int)
                except ValueError:
                    print("Not a valid number or does not exist.")
                try_again = input("To look for another package enter 1. 0 to exit.")
                if checker == "0":
                    print("0 was selected or an invalid option. Exiting program.")
                checker = try_again

            return status_1
           


# Lookup funciton to find mail by id
    if main == "2":
        print("It is currently 7:59AM.")

        checker = "1"
        while checker == "1":
            # Prompt the user to get package ID to search for.
            user_search_string = input("Please type and enter the ID of the mail you are looking for: ")
            try:
                user_search_int = int(user_search_string)
                print_result(user_search_int)
            except ValueError:
                print("Not a valid number or does not exist.")
            try_again = input("To look for another package enter 1. All other values exit.")
            if checker == "0":
                 print("0 was selected or an invalid option. Exiting program.")
            checker = try_again
        ui()




 

# Beginning of UI
print("Greetings! It is currently 7:59AM")
ui()
