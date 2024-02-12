import random
guesses = 0
number_list = []
def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")

        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("this is not a valid input")
    return user_input

for x in range(0, 4, 1):
    number = random.randint(0,9)
    number_list.append(str(number))

while(True):
    cow = 0
    bull = 0
    guess = get_input("please input a 4 digit number", str)
    guess_list = list(guess)
    duplicate_list = [1,1,1,1]
    
    for x, guess in enumerate(guess_list):
        for y, number in enumerate(number_list):
            
            if guess_list[x] == number_list[y] and x == y:
                cow += 1
                duplicate_list[y] = "x"
                break
            
            elif guess_list[x] == number_list[y] and x != y and duplicate_list[y] != "x":
                bull += 1
                
    guesses += 1
    
    print(cow, "cows")
    print(bull, "bulls")
    
    if guess_list == number_list:
        print(f"Well done!  It took you {guesses} guesses")
        break