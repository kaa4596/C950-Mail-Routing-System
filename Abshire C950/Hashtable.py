#importing csv to class so it can read the text file format
import csv

#class creates a hashtable that helps sort data more efficiently 
class HashTable:

#initializes buckets for data
#one for loop so it is N
     def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

#creates an insert function to change the status of the package to at hub or delayed
     def insert(self, key, mail):
        mail[0] = int(mail[0])
        bucket = key % len(self.table)
        self.table[bucket].append(mail)
        if mail[7] != "Delay":
            mail.append("AT_HUB")  # Adds delivery status for all packages that are not late to the hub
        if mail[7] == "Delay":
            mail.append("DELAYED_ON_FLIGHT")  # Packages that are late to the hub get this delivery status

#Looks for a box of mail based on id. If not found returns words not found.
#one for loop so it is N
     def lookup(self,key):
         bucket = key % len(self.table)
         bucket_list = self.table[bucket]
         for box in bucket_list:
            if box[0] == key:
                return box
         return "Package not found."

#Deletes a box of mail with matching id
#single for loop so N
     def delete(self,key):
         bucket = hash(key) % len(self.table)
         bucket_list = self.table[bucket]

         for box in bucket_list:
            if box[0] == key:
                bucket_list.remove(key)

#Gathers text csv data from the package file
#has one for loop so it is N
def get_mailboxes(name):
    hash_mail = HashTable()
    with open(name) as file:
        data = csv.reader(file)
        next(data, None)  
        for row in data:
            hash_mail.insert(int(row[0]), row)  
    return hash_mail

#function establishes the hashtable with data in a callable variable
mail_hashtable = get_mailboxes("Packages.csv")
    
#Prints the exact boxed mail in search result when found in the hashtable
def print_result(id):
     result = mail_hashtable.lookup(id)
     print(result)
