#Lucky Lotto Numbers- Will give you 6 random numbers for the lottery

from random import randint

username = input("What is your name?")
min_str = ("1")
max_str = ("59")
minimum = int(min_str)
maximum = int(max_str)
lotto_no1 = randint(minimum, maximum)
lotto_no2 = randint(minimum, maximum)
lotto_no3 = randint(minimum, maximum)
lotto_no4 = randint(minimum, maximum)
lotto_no5 = randint(minimum, maximum)
lotto_no6 = randint(minimum, maximum)

print("Hello " + username + "! Your Lotto numbers are: " + str(lotto_no1) + ", " + str(lotto_no2) + ", " +
      str(lotto_no3) + ", " + str(lotto_no4) + ", " + str(lotto_no5) + ", " + str(lotto_no6))

print("Thank You for using this random number generator and Good Luck!")

print()
input("Press return to close the program")
