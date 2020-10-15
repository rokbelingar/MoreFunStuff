
guess = int(input('Vnesi število od 1-100: '))

for x in range(1, guess + 1):
    if x % 5 == 0 & x % 3 == 0:
        print("fizzbuzz!")
    elif x % 3 == 0:
        print("fizz!")
    elif x % 5 == 0:
        print("buzz!")
    else:
        print(x)
