# InraTasks
## Tasks1
    *import random

    numbers = list(range(1, 11))*

    Here, I have imported the random module and created a list of numbers from 1 to 10 using rnage() function.

    *for i in range(len(numbers)):
    index1 = random.randint(0, len(numbers)-1)
    index2 = random.randint(0, len(numbers)-1)
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]*

    Here, we loop through the list of numbers and swap the positions of two random numbers in each iteration.
    For each iteration of the loop there will be two random numbers generated using randint() function between 0 and 11 which means numbers it can be any numbers from 1 to 10.
    Once two numbers are generated then we swap those numbers to create a random order of the numbers.

    *print(numbers)*

    And finally, we print the updated list of numbers whcih will list the numbers from 1 to 10 in random order.




