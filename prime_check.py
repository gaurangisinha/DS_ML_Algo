# Program to check if a number is prime or not

num = int(input("Enter yor number: "))

isPrime = False

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            isPrime = True
            # break out of loop
            break

# check if flag is True
if isPrime:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")