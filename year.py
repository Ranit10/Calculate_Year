import datetime

def calculate_year(name, age):
    current_year = datetime.datetime.now().year
    years_to_100 = 100 - age
    year_turn_100 = current_year + years_to_100
    return f"{name}, you will turn 100 in the year {year_turn_100}. You will be {years_to_100} years old."

name = input("What is your name: ")
age = int(input("How old are you: "))

print(calculate_year(name, age))
