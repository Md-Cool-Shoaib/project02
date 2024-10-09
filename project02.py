def get_number(number):
    while True:
        operand1 = input("Number  "+str(number)+":")
        try:
           return float(operand1)
        except:
            print("Invalid Input")

operand1 = get_number(1)
operand2 = get_number(2)

sign = input("sign (+,*,-,/): ")
if sign == "+":
    result =  operand1 + operand2
    print(result)
elif sign == "-":
    result = (operand1) - (operand2)
    print(result)
elif sign == "*":
    result = (operand1) * (operand2)
    print(result)
elif sign == "/":
    if float(operand2) != 0:
        result = (operand1) / (operand2)
    else:
        print("Division by zero")
else:
    print("Not a valid sign")

    