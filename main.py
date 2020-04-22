from pylinac import DRGS

import os

fileNames = []

for root, dirs, files in os.walk("/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/Unit 2/2018-07-20"):
    for file in files:
        if file.endswith(".dcm"):
             fileNames.append(str(os.path.join(root, file)))
             #print(os.path.join(root, file))



open_img = fileNames[0]
dmlc_img = fileNames[1]

mydrgs = DRGS(image_paths=(open_img, dmlc_img))

mydrgs.analyze(tolerance=1.5)
# print results to the console
# print(mydrgs.results())
# view analyzed images
# mydrgs.plot_analyzed_image()
mydrgs.publish_pdf("test.pdf")
