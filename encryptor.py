normalDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '3', '2', '4', '5', '6', '7', '8', '9']
reversedDict = ['9', '8', '7', '6', '5', '4', '2', '3', '1', '0', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'l', 'm', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
stringNumber = []
reversed = []

string = str(input("Your string : "))
string = string.lower()

for i in range(len(string)):
  if string[i] in normalDict:
    for x in range(26):
      if string[i] == normalDict[x]:
        stringNumber.append(x)

stringNumber.reverse(); x = stringNumber

def writeToFile():
	file = open("main.txt", "a")
	file.write("\n")
	file.write(str(x))
	file.close()

def clearFile():
	file = open("main.txt", "w")
	file.write("")
	file.close()

writeToFile()
