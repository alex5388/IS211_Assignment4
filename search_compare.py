import random
import time



def get_me_random_list(n):                      #creates random list

    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):            #search algo
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def ordered_sequential_search(a_list, item):        #search algo
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binary_search_iterative(a_list, item):          #search algo
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found



def binary_search_recursive(a_list, item):          #search algo
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)



def main():

    random.seed(100)                                #number of lists to create
    sizes = [500, 1000, 5000]                       #number of elements in each list
    t_time = 0                                      #total time placeholder

    for list_size in sizes:
        for i in range(100):
            sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)         #call list generator func
            s = time.time()                                 #start time count
            ordered_list = sequential_search(my_list, random.randint(0, len(my_list) + 100))
            e = time.time()                                 #end time count
            duration = e - s
            t_time += duration                              #total time of sort
        avg_time = t_time / 100                             #avg total time of 100 sorts
        print(f"Average search time for list of {list_size} using Sequential search was {avg_time:0.8f} seconds.")

    for list_size in sizes:
        for i in range(100):
            sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            s = time.time()
            ordered_list = ordered_sequential_search(my_list, random.randint(0, len(my_list) + 100))
            e = time.time()
            duration = e - s
            t_time += duration
        avg_time = t_time / 100
        print(f"Average search time for list of {list_size} using Ordered sequential search was {avg_time:0.8f} seconds.")

    for list_size in sizes:
        for i in range(100):
            sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            s = time.time()
            ordered_list = binary_search_iterative(my_list, random.randint(0, len(my_list) + 100))
            e = time.time()
            duration = e - s
            t_time += duration
        avg_time = t_time / 100
        print(f"Average search time for list of {list_size} using binary search iterative  search was {avg_time:0.8f} seconds.")

    for list_size in sizes:
        for i in range(100):
            sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            s = time.time()
            ordered_list = binary_search_recursive(my_list, random.randint(0, len(my_list) + 100))
            e = time.time()
            duration = e - s
            t_time += duration
        avg_time = t_time / 100
        print(f"Average search time for list of {list_size} using binary search recursive was {avg_time:0.8f} seconds.")

if __name__ == "__main__": #start and run main()
    main()