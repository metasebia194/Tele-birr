def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total * (1 + tip_rate)
    return total_with_tip / people

bill_total = float(input("Enter the total bill (ETB): "))

people = int(input("Enter the number of people: "))

while people <= 0:
    print("Number of people must be greater than 0.")
    people = int(input("Enter the number of people: "))

names = []

for i in range(people):
    name = input(f"Enter the name of person {i + 1}: ")
    names.append(name)

share = split_bill(bill_total, people)

print("\n----- Bill Summary -----")
print(f"Total Bill: {bill_total:.2f} ETB")
print("Tip Rate: 10%")
print(f"Each Person Pays: {share:.2f} ETB\n")

for name in names:
    print(f"{name} pays {share:.2f} ETB")