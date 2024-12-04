#Password generator made by Vansh
import random, string

character = "".join(string.ascii_letters)
numbers = "".join(string.digits)
joined = character + numbers
joinedh = joined + '!,@,*,&'
print("Welcome to Password Generator\n")
print("Complexity Modes:\nEasy\nMedium\nHard\n")

com = input("Enter the complexity of the password:")
leng = int(input("Enter the length in numbers:"))
if leng >= 1 and leng <= 99:
  if com.lower() == 'easy':
    print('Easy Mode:')
    rese = "".join(random.choices(string.ascii_letters, k=leng))
    print("Generated Password is: ", rese)

  elif com.lower() == 'medium':
    print('Medium Mode:')
    resm = "".join(random.choices(joined, k=leng))
    print("Generated Password is: ", resm)

  elif com.lower() == 'hard':
    print('Hardest Mode:')
    resh = "".join(random.choices(joinedh, k=leng))
    print("Generated Password is: ", resh)
  else:
    print("Wrong Input")
else:
  print("Enter length between 1-99")
  exit()