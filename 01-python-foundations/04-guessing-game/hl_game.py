#name = "Robinhood"
#age = 53
#actual_age = 53.65
#math = 5 ** 8 + 4 / 9 * 5 - 2
#result = age + actual_age + math
#print(result)

# Higher-lower game

import random 
random_number = random.randint(1, 100)
print(random_number)

chances = 7
while chances > 0:
    user_guess = input("Enter your guess:")
    user_guess_to_int = int(user_guess)

    print("Your guess is", user_guess)

    if user_guess_to_int > random_number:
        print("Your guess is greater")
        chances -= 1
    elif user_guess_to_int < random_number :
        print("Your guess is lesser") 
        chances -= 1
    else: 
        print("Your guess is correct") 
        chances = 7
        random_number = random.randint(1, 100)


# weight = 0.0
# while weight < 1.5:
#     weight = weight + 0.5
#     print("Current weight: " + str(weight))

# sentence = "latte and espresso"
# words = sentence.split(" and ")
# print(words)
# rejoined = "-".join(words)
# print(rejoined)

# def add_tax(subtotal):
#     return subtotal * 1.08

# final_total = add_tax(10.0)
# print(final_total)

# class Node:
#     def _init_(self, data):
#         self.data = data
#         self.next = None 

# head = Node("Start")
# head.next = Node("End")

# current = head
# while current is not None:
#     print(current.data)
#     current = current.next