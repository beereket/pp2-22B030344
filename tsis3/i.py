def convert_grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

def filter_primes(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]

def has_33(list):
    for i in range(len(list)-1):
        if  list[i] == 3 and list[i+1] == 3:
            return True
    return False

def spy_game(list):
    for i in range(len(list)-1):
        if  list[i] == 0 and list[i+1] == 0 and list[i+2]==7:
            return True
    return False

def volume_of_sphere(radius):
    return (radius**3)*4/3

def unique_elements(list):
    new_list=[]
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    return new_list

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def histogram(list):
    for i in list:
        print('*'*i)

import random
 
def guess_the_number():
        print('Hello! What is your name?')
        name=input()
        print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    
        number=random.randint(1, 20)
        tries=0
        while True:
            print("Take a guess.")
            guess=int(input())
            tries+=1
            if guess>number:
                print("Your number is too high.")
            elif guess<number:
                print("Your number is too low.")
            else:
                break
        print("Good job, " + name + "! You guessed my number in " + str(tries) + " tries!")

def permutations(data, index=0):
    if index == len(data):
        print("".join(data))
    else:
        for i in range(index, len(data)):
            data[index], data[i] = data[i], data[index]
            permutations(data, index + 1)
            data[index], data[i] = data[i], data[index]

            
def reverse_sentence(sentence):
    words = sentence.split()
    return " ".join(reversed(words))
