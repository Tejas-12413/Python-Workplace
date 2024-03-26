normalDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '/', '?', '[', '{', ']', '}', '.', ',', '<', '>', '`', '~'] 
reversedDict = ['~', '`', '>', '<', ',', '.', '}', ']', '{', '[', '?', '/', '=', '-', '+', '_', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!', ' ', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

fE = open("encrypted.txt", "r"); count = sum(1 for _ in fE); fE.close()

newNumber = []
lineHolder = []

file = open("encrypted.txt", "r")
x = file.readline()
file.close()
fileD = open("decrypted.txt", 'a')

for j in range(count):
  for i in x:
    for z in range(len(reversedDict)):
      if i == reversedDict[z]:
        newNumber.append(z)

  newNumber.reverse()
  for i in newNumber:
    finalString = f"{normalDict[i]}"
    fileD.write(finalString)
    
fileD.write("\n")
fileD.close()