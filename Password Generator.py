import string
import random



Option1 = list(string.ascii_lowercase)
Option2 = list(string.ascii_uppercase)
Option3 = list(string.punctuation)
Option4 = list(string.digits)


#User provide number of chracters in password
user_input = input("How many characters do you want in your password? ")

while True:

        characters_numbers = int(user_input)


        if characters_numbers < 8:

            print("You neeed to enter at least 8 characters")

            user_input = input("Please enter your number again: ")

        else:

            break

        print("Please enter numbers only.")

        user_input = input("How many characters do you want your password ?")


random.shuffle(Option1)
random.shuffle(Option2)
random.shuffle(Option3)
random.shuffle(Option4)


part1 = round(characters_numbers * (30/100))
part2 = round(characters_numbers * (20/100))


result = []

for x in range(part1):
 
    result.append(Option1[x])
    result.append(Option2[x])
 
for x in range(part2):
 
    result.append(Option3[x])
    result.append(Option4[x])
 
 

random.shuffle(result)
 
 

password = "".join(result)
print("Strong Password: ", password)




    



