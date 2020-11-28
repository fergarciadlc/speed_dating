# run: python pairs.py > meets.txt
import random
import csv

CSV_PATH = 'users.csv'
N_ITERATIONS = 20

users = []

with open(CSV_PATH,'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # name and slackname
        users.append(f"{row[0]} ({row[1]})")

users = users[1:]

nb_participants = len(users)
pairs_history = []
nb_pairs = nb_participants // 2

def includes_pair(history,pair):
    for hist_pair in history:
        if( ((pair[0] == hist_pair[0]) and (pair[1] == hist_pair[1] )) or
            ((pair[0] == hist_pair[1]) and (pair[1] == hist_pair[0] ))  ):
            return True
    return False

def make_pair(to_assign,history):
    is_existing = True
    max_iter = 100
    sample_pair = []
    while (is_existing and (max_iter>0)):
        sample_pair = random.sample(to_assign, 2)
        is_existing = includes_pair(history,sample_pair)
        max_iter = max_iter - 1
    #print(max_iter)
    return sample_pair

def print_pair(new_pair):
    print(f"{users[new_pair[0]]} --> calls --> {users[new_pair[1]]}")

def remove_pair(list_to_remove_from,pair_to_remove):
    list_to_remove_from.remove(pair_to_remove[0])
    list_to_remove_from.remove(pair_to_remove[1])
    return

def add_pair(history,pair):
    history.append(pair)
    return

def select():
    this_round = []
    participants_to_assign = []
    for i in range(nb_participants):
        participants_to_assign.append(i)

    max_iter = 100
    while((len(participants_to_assign) > 1) and (max_iter>0)):
        new_pair = make_pair(participants_to_assign,pairs_history)
        print_pair(new_pair)
        remove_pair(participants_to_assign,new_pair)
        add_pair(this_round,new_pair)
        add_pair(pairs_history,new_pair)
        max_iter = max_iter - 1
    if(len(participants_to_assign) == 1):
        print(f"{users[participants_to_assign[0]]} will be called by a manager")
        add_pair(this_round,[participants_to_assign[0], 999])#999 is the code for a manager
    return this_round

# print("=========== round 1 ===========")
# round1 = select()
# print("--history--")
# print(pairs_history)
# print("=========== round 2 ===========")
# round2 = select()
# print("--history--")
# print(pairs_history)

for i in range(N_ITERATIONS):
    print(f"Iteration {i+1}:")
    print("----------------------------------")
    select()
    print("\n")

print("Finished")
