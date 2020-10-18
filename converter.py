print("Hello! Welcome to mile-kilometer converter")


while True:
    distance = input("Please, type in the amount of kilometers you want to convert to miles: ")
    distance = float(distance.replace(",", "."))

    print("That would amount in " + str(distance*0.62) + " Miles")

    another_one = input('Do you want to do it again? ').lower()

    if another_one != "yes":
        break

