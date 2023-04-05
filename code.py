def lowercase_and_remove(word):
    temp_word = ""
    ignore_this_bitches = "! . , ? : ; - "
    for ch in word:
        if ch in ignore_this_bitches:
            continue
        else:
            temp_word += ch
    temp_word = temp_word.lower()
    return temp_word

file_path1 = "/Users/gabe/Desktop/Spring23/CIS-172/AbbyCode/KJV/kjv.txt"
file = open(file_path1,"r")


dict = {}

for line in file:
    temp_line = line.split()
    if("John" in line.split()[0]):
        for i in range(0,len(temp_line)):
            temp_word = lowercase_and_remove(line.split()[i])
            if(i==0):
                continue
            elif (temp_word in dict):
                dict[temp_word] += 1
            else:
                dict[temp_word] = 1

print(dict)
user_input = ""
while(user_input != "Q"):
    word = (input("What word would you like to check: "))
    if(word in dict):
        print(dict[word])
    else:
        print("Not contained in dictionary")

    user_input = (input("Enter Q to quit or enter to check for another word: "))
    



file.close()
        