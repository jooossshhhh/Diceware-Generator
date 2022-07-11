import csv
import time
import random

if __name__=='__main__':
    #initialize seed based on time, so that we are truly random
    random.seed(time.time())
    
    #read diceware file, then create a dict object out of it
    dict_from_csv = {}
    with open("path\to\file\diceware_gen.csv",'r') as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[0]:rows[1] for rows in reader}
    
    #create set containing our five digit numbers
    diceware = set()
    n_times = 6
    for i in range(n_times):
        #'roll' dice 5 times and save it to numbers
        numbers = []
        for i in range(5):
            numbers.append(str(random.randint(1,6)))

        #join list of numbers together
        diceware.add(''.join(map(str,numbers)))
    #find the words that correspond to each five digit number
    print("You're new password is: \n")
    for dice in diceware:
        print(dict_from_csv[dice])

  
