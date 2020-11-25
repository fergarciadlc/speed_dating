import csv
import random


CVS_PATH = 'users.csv'
N_PEOPLE_BY_GROUP = 2
N_ITERATIONS = 15


def chunker(seq, size):
        # https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list
        return [seq[pos:pos + size] for pos in range(0, len(seq), size)]


def generate_calls(user):
    
    shuffle_users = users[:]

    random.shuffle(shuffle_users)

    groups = chunker(shuffle_users, N_PEOPLE_BY_GROUP)

    if len(users) % 2 != 0:
        # not even particpants, last group of three participants
        groups[-2].append(groups[-1][0])
        groups.pop()


    calls = []
    for group in groups:
        call = '  ->  '.join(group)
        print(call)
        calls.append(call)

    return calls


if __name__ == '__main__':

    users = []
    with open(CVS_PATH,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # name and slackname
            users.append(f"{row[0]} ({row[1]})")

    users = users[1:]

    with open("meets.txt", "w") as f:

        for i in range(N_ITERATIONS):
            
            print(f"\nIteration {i+1}:")
            print("-----------------------------------------------")
            f.write(f"\nIteration {i+1}:\n")
            f.write("-----------------------------------------------\n")
            f.writelines("\n".join(generate_calls(users)))
            print("\n")
            f.write("\n\n")
