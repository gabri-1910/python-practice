# This program is meant to take user input and perform operations using functions
def wordGame(name, number, place, time):
    num = number + time
    print("Hello again, ", name, "how are you?")
    print("You lost your wallet in the year of", num, "at the", place)
    return


print("Hello There! Welcome to the game.")
print("Here, we'll use your data to make up stuff.")


name = str(input("To begin, tell me your name: "))
number = int(input("Choose a number: "))
place = str(input("Choose a place: "))
time = int(input("choose a year: "))

wordGame(name,number,place,time)