myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
bill_displayed_in_currency = "{:.2f}".format(answer)

print(f"You all owe ${bill_displayed_in_currency}")