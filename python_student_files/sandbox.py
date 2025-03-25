
import string
import random

accounts_list = [
    ['Emily','Rodriguez',39,1234,'emily.rodriguez1234@hmm.com','password123','A-100'],
    ['Audrey','Rodriguez',9,1234,'audrey.rodriguez1234@hmm.com','password123','A-100'],
    ['Benjamin','Rodriguez',7,1234,'benjamin.rodriguez1234@hmm.com','password123','A-100'],
    ['Mario,Rodriguez',41,1234,'mario.rodriguez1234@hmm.com','JrxR4+:3','A-100'],
    ['Neil','Armstrong',35,1234,'neil.armstrong1234@hmm.com','UzD3]8x=','A-100'],
    ['Buzz,Aldrin',44,1234,'buzz.aldrin1234@hmm.com','G_5#Pza3','A-100']
]

def id_gen():

    user_id = 0

    while True:
        #generate random number from 1000 to 9999
        random_integer = random.randint(1000, 9999)
        print(random_integer)
        for account in accounts_list:
            if random_integer in account:
                random_integer = random.randint(1000, 9999)
        else:
            user_id = random_integer
            break

    return user_id



def main():
    
    user_id = id_gen()
    print(user_id)

if __name__ == "__main__":
    main()