from math import *
print("------------------------------------")
print("         Advanced Calculator        ")
print("------------------------------------")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Cube Root\n7. Power\n8. Modulus\n9. Common Log\n10. Natural Log\n11. Sine\n12. Cosine\n13. Tangent\n14. GCD\n15. LCM\n16. Percentage\n17. Average")
print("------------------------------------")
op = int(input("Enter the number of operation: "))

    
if op == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} + {num2} =", num1 + num2)
elif op == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} - {num2} =", num1 - num2)
elif op == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} * {num2} =", num1 * num2)
elif op == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} / {num2} =", num1 / num2)
elif op == 5:
        num = float(input("Enter the number: "))
        print(f"Square Root of {num} = ""{:.1f}".format(sqrt(num)))
elif op == 6:
        num = float(input("Enter the number: "))
        print(f"Cube Root of {num} = ", round(num**(1/3), 6))
elif op == 7:
        num1 = float(input("Enter first number(Base): "))
        num2 = float(input("Enter second number(Exponent): "))
        print(f"{num1} ^ {num2} =", pow(num1, num2))
elif op == 8:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} % {num2} =",num1 % num2)
elif op == 9:
        num = float(input("Enter the number to find its common Log: "))
        print(f"Common Log of {num} =", log10(num))
elif op == 10:
        num = float(input("Enter the number to find its Natural Log: "))
        print(f"Natural Log of {num} =", log(num))
elif op == 11:
        num = float(input("Enter the number: "))
        print(f"Sine of {num} =", sin(num))
elif op == 12:
        num = float(input("Enter the number: "))
        print(f"Cosine of {num} =", cos(num))
elif op == 13:
        num = float(input("Enter the number: "))
        print(f"Tangent of {num} =", tan(num))
elif op == 14:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"GCD of {num1} and {num2} =", gcd(num1, num2))
elif op == 15:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"LCM of {num1} and {num2} =", lcm(num1, num2))
elif op == 16:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        percent = num1 / num2 * 100
        print(f"Percentage of {num1} out of {num2} = ""{:.1f}%".format (percent))
elif op == 17:
        n = int(input("How many numbers? "))
        numbers = []
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
        total_sum = sum(numbers)
        avg = total_sum / n
        print("Sum = {}\nAverage = {:.1f}".format(total_sum, avg))
else:
        print("Invalid number!")
# print("Note:")
# print("value of PI = ", pi)
# print("value of e = ", e)
# print("value of Tau = ", tau)