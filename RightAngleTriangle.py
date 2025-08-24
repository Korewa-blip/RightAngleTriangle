print("Half Pyramid Pattern of Stars (*):")
n=int(input("Enter the number of stars"))       
for i in range(n):
  for j in range(i+1):
      print("* ",end="")
  print()                                          