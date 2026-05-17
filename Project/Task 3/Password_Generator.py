import random

special_char = ["@", "#", "$", "!", ".", "&", "_", "-", ">", "<"]

number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

alphabets = [
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
"k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
"u", "v", "w", "x", "y", "z"
]

uppercase = [
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
"U", "V", "W", "X", "Y", "Z"
]

def password_generator(length):


    password = []

    password.append(random.choice(special_char))
    password.append(random.choice(number))
    password.append(random.choice(alphabets))
    password.append(random.choice(uppercase))

    all_characters = special_char + number + alphabets + uppercase

    for i in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)

length = int(input("Enter password length: "))

print("Generated Password:", password_generator(length))
