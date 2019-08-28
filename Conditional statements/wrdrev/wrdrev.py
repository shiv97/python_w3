wrd = input("enter word: ")

for char in range(len(wrd) - 1, -1, -1):
  print(wrd[char], end="")
print("\n")