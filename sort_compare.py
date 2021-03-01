import random
import time


def get_me_random_list(n):                  #creates random list
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):                 #sort algo
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value



def shell_sort(a_list):                     #sort algo
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for s_position in range(sublist_count):
            gap_insertion_sort(a_list, s_position, sublist_count)

        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, s, gap):     #sort algo
    for i in range(s + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(a_list):                    #built-in python sorting algo
    return sorted(a_list)


def main():

    random.seed(100)                        #number of lists to create
    sizes = [500, 1000, 5000]               #number of elements in each list
    t_time = 0                              #total time placeholder


    for list_size in sizes:
        for i in range(100):
            sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)         #call list generator func
            s = time.time()                                 #start sorting timer
            ordered_list = shell_sort(my_list)              #order my_list
            e = time.time()                                 #end sorting timer
            duration = e - s
            t_time += duration                              #total time to complete
        avg_time = t_time / 100                             #avg completion time of 100 lists
        print(f"Average sort time for list of {list_size} using Insertion Sort was {avg_time:0.8f} seconds.")

    for list_size in sizes:
        for i in range(100):
            sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            s = time.time()
            ordered_list = insertion_sort(my_list)
            e = time.time()
            duration = e - s
            t_time += duration
        avg_time = t_time / 100
        print(f"Average sort time for list of {list_size} using Shell Sort was {avg_time:0.8f} seconds.")

    for list_size in sizes:
        for i in range(100):
            sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            s = time.time()
            ordered_list = python_sort(my_list)
            e = time.time()
            duration = e - s
            t_time += duration
        avg_time = t_time / 100
        print(f"Average sort time for list of {list_size} using Python Sort was {avg_time:0.8f} seconds.")

if __name__ == "__main__":
    main()