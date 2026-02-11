num1=int(input("Enter the First number"))
num2=int(input("Enter the Second number"))
num3=int(input("Enter the Third number"))

if(num1>num2 and num1>num3):
    print(num1,"Number 1 is Greater")
elif(num2>num1 and num2>num3):
    print(num2,"Number 2 is Greater")
elif(num3>num1 and num3>num2):
  print(num3,"Number 3 is Greater")
else:
  print("Invalid Option")
