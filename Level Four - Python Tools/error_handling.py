import logging

logging.basicConfig(
    filemode="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# divide by zero
try :
    a = 10
    b = 0
    c = a/b

except ZeroDivisionError as e:
    logging.error(e)

# invalid input
try:
    n = int(input("Enter number: "))
    print("Number:", n)
except ValueError as e:
    logging.error(e)

# file not found
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError as e:
    logging.error(e)

#  * Append every error in error.log with timestamp