import os

fileNames = []

for root, dirs, files in os.walk("/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/Unit 2/2018_11_29_DGRS"):
    for file in files:
        if file.endswith(".dcm"):
             fileNames.append(str(os.path.join(root, file)))
             #print(os.path.join(root, file))

print(fileNames[0])

