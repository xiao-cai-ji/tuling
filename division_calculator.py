try:
    print(5/2)
except ZeroDivisionError:
    print("Error")

print("Give me two number,and I'll divide them")
print("Enter 'Q' to quit")
while True:
    first_number = input("Enter First number: ")
    if first_number == "Q":
        break
    second_number = input("Enter Secnond number: ")
    if second_number == "Q":
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Error")
    else:
        print(answer)