#!/usr/bin/python
#main script for solving "Tourist" problem
import sys

"""
T: Number of campuses
K: Attractions to visit
N: Attractions in campus
V: Number of visits to a campus 
Default list: Ordered from most popular to non-popular
1 < T < 80 
1 < K < N < 50 
1 < V < 10^12
"""

def main():
    """
    Opens text file and reads through it, while executing logic for every campus (block)
    We only iterate once through the .txt file
    """
    total_campuses=0

    with open(sys.argv[1], 'r') as fh:
        print("File successfully opened")
        analyzing_block=False
        popularity_list=[]
        attractions, attractions_to_visit, total_visits = 0,0,0 #N,K,V
        
        for i, line in enumerate(fh):
            if " " in line:
                print(popularity_list)
                if analyzing_block and (len(popularity_list)==attractions):
                    print("Visiting campus...")
                    visit(attractions, attractions_to_visit, total_visits)
                    analyzing_block=False
                    popularity_list=[]
                    attractions, attractions_to_visit, total_visits = 0,0,0 #N,K,V

                print("Starting block found!")
                analyzing_block=True

                s_list = line.split(' ')
                attractions, attractions_to_visit, total_visits = [int(i) for i in s_list]
                continue

            if analyzing_block:
                popularity_list.append(line.strip())
                continue
            elif (i==0):
                total_campuses = int(line)
                continue
        
        #One additional visit (last case, undetected by ending check)
        #TODO Improve logic here
        if analyzing_block and (len(popularity_list)==attractions):
            print(popularity_list)
            print("Visiting campus...")
            visit(attractions, attractions_to_visit, total_visits)

        print("Total number of campuses visited: " + str(total_campuses))
    

    return

def visit(N,K,V):
    """
    Executes the logic for the series of visits for each single campus
    """
    return

if __name__ == "__main__":
    main()

