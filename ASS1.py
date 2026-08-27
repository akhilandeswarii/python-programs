#Student Attendance system
name = input("Enter student name: ")
total_classes = int(input("Enter total classes: "))
present_classes = int(input("Enter attended classes: "))
percentage = (present_classes / total_classes) * 100
print("Student:", name)
print("Attendance Percentage:", percentage, "%")


#ATM system
balance = 10000
pin = int(input("Enter PIN: "))
if pin == 1234:
    print("PIN verified")
    print("Current Balance:", balance)
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Cash dispensed:", amount)
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")