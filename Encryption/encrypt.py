normalDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '/', '?', '[', '{', ']', '}', '.', ',', '<', '>', '`', '~'] 
reversedDict = ['~', '`', '>', '<', ',', '.', '}', ']', '{', '[', '?', '/', '=', '-', '+', '_', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!', ' ', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
stringNumber = []

string = input("Your string : ")
string = string.lower()

def clearFile():
	file = open("encrypted.txt", "w")
	file.write("")
	file.close()

for i in range(len(string)):
	for x in range(63):
		if string[i] == normalDict[x]:
			stringNumber.append(x)
stringNumber.reverse(); reversedStringNumber = stringNumber

if string != 'cls' and string != '':
	file = open("encrypted.txt", "a")
	for i in reversedStringNumber:
		file.write(reversedDict[i])
	file.write("\n")
	file.close()

if string == 'cls':
	clearFile()