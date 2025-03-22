# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    if number > 1:
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
    else:
        print("Please enter a number greater than 1.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
