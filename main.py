bill = float(input("What was the bill: "))
tip_percentage = int(input("What tip percentage would you like to add? "))
bill_total = bill + (bill * (tip_percentage/100))
bill_total_formatted = "{:.2f}".format(bill_total)
print(f"The total bill is: ${bill_total_formatted}")
print()
num_people = int(input("How many people will be splitting the bill? "))
bill_per_person = bill_total / num_people
bill_per_person_formatted = "{:.2f}".format(bill_per_person)

print(f"You all owe ${bill_per_person_formatted}")