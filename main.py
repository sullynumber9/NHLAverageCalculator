# 1. Read in all of the lists

#2. in a master list, store the following parameters

import json

"""
1. The name of the player
2. The number of times they appear in the list
3. a sublist containing each of their rankings

[Connor McDavid, 6, [1, 1, 1, 1, 2]]

"""

with open("config.json", "r") as file:
    fileNames = json.load(file)

fileList = []

fileList.append(fileNames["list_one"])
fileList.append(fileNames["list_two"])
fileList.append(fileNames["list_three"])
fileList.append(fileNames["list_four"])
fileList.append(fileNames["list_five"])
fileList.append(fileNames["list_six"])


for file in fileList:
    print(file)


namesList = []

# Listing off all of the names

firstPass = 0

for fileName in fileList:

    file  = open(fileName, "r")

    for line in file.readlines():

        line = line.strip("\n")

        if line not in namesList:
            namesList.append(line)
    
    file.close()

print(namesList)

# Seeing how many times each name appears in each of the individual lists

masterList = []

for name in namesList:

    nameCount = 0
    nameRankings = []

    for fileName in fileList:

        file = open(fileName, "r")
        listIndex = 1

        for line in file.readlines():
            line = line.strip("\n")
            if (line == name):
                nameCount += 1
                nameRankings.append(listIndex)
            listIndex += 1
    
        file.close()
    
    masterList.append([name, nameCount, nameRankings])

print(masterList)

# getting the average ranking of each player

for subList in masterList:

    total = 0
    for ranking in subList[2]:

        total += ranking
    
    average = total / len(subList[2])

    subList.append(average)

print(masterList)

# sorting the list by the highest number of appearances, then the lowest average ranking
masterList.sort(key=lambda x: (-x[1], x[3], -max(x[2])))

for i in range(len(masterList)):
    print("Player " + str(i+1) + ": " + str(masterList[i][0]) + " | Appearances: " + str(masterList[i][1]) + " | Rankings: " + str(masterList[i][2]) + " | Average: " + str(masterList[i][3]))

#writing the master list to a file

file = open("FinalList.txt", "w")
for i in range(len(masterList)):
    file.write("Player " + str(i+1) + ": " + str(masterList[i][0]) + " | Appearances: " + str(masterList[i][1]) + " | Rankings: " + str(masterList[i][2]) + " | Average: " + str(masterList[i][3]) + "\n")
    if (i+1 == 20):
        file.write("TOP 20 EXCEEDED!!\n")





