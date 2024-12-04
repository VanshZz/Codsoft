#Basic Calculator with some arithmetic operation by Vansh
print('Welcome to the Calculator\n')
a = int(input('Enter the First number:'))
b = int(input('Enter the Second number:'))
print('Choose From The Available Operators')
print('+\n-\n*\n/\n%')
C = input('Enter the operator:')
if C == '+':
  print(f"The sum of {a} and {b} is {a+b}")
elif C == '-':
  print(f"The difference of {a} and {b} is {a-b}")
elif C == '*':
  print(f"The product of {a} and {b} is {a*b}")
elif C == '/':
  print(f"The quotient of {a} and {b} is {a/b}")
elif C == '%':
  print(f"The Modulo of {a} and {b} is {a%b}")
else:
  print('Print invalid operator')