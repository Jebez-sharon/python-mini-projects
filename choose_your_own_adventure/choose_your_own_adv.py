# def arm_strong(num):
#     total_number_digits = len(str(num))
#     armstrong_no = 0
#     n = num

#     while n > 0:
#         last_digit = n % 10
#         armstrong_no += last_digit ** total_number_digits
#         n = n // 10
#     return num == armstrong_no

# print(arm_strong(153))


name = input("Type your name: ")
print("Welcome ", name, "to this adventure!")

answer = input("You are on dirt road , it has come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river , you can walk aroud it or swim accorss? Type walk around and swim to swim accross: ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles , ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge it looks wobbly do you want to cross it or head back (cross/back)?")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger . Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the starnger and they gave you gold, you win")

        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not valid answer. You lose")
    else:
        print("Not a valid option. You lose.")
else:
    print("NOt a valid option. You lose")

print("Thank you for trying ", name)