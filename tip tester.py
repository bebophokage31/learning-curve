def get_total():

    meal_cost = int(input("Please enter cost of meal: "))
    tip_percent = int(input("Please enter your tip percentage as whole number:"))
    tax_percent = int(input("Please enter tax percentage as whole number: "))

    tip = ((meal_cost * tip_percent) / 100)
    tax = ((meal_cost * tax_percent) / 100)
    total = int(round(meal_cost + tip + tax))

    return str(total)

print("The total cost of your meal is " + get_total() + " dollars.")