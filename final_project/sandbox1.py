
PODS = {'A-100': 6, 'A-101': 6, 'A-102': 3, 'A-103': 0, 'A-104': 5, 'A-105': 4, 'OVERFLOW':0}

def pod_assignment():
    print('This is the pod function')

    global PODS
    max_capacity = 6

    available_slot = min(PODS, key=PODS.get)
    PODS[available_slot] += 1 
    print(PODS[available_slot])
    return available_slot

    # for key, value in PODS.items():
    #     print(key)
    #     if PODS[key] > max_capacity:
    #         continue
    #     elif PODS[key] < max_capacity:
    #         PODS[key] +=1
    #         return key
    #     else:
    #         print('Total capacity has been reached.\n'
    #         'No POD assignment has been made')
    #         return 'OVERFLOW'
        
def main():

    my_pod_assignment = pod_assignment()
    print(my_pod_assignment)

if __name__ == "__main__":
    main()