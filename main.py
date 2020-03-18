from pylinac import DRGS

open_img = 'N:/MedicalPhysics/Quality Control Program/Treatment/Monthly/Junctions and Picket Fence/Unit 1 SN 3951/2020_03_10/DRGS/ZPHYSICS_MONTHLY_U1/RI.ZPHYSICS_MONTHLY_U1.MV_179_0a.dcm'
dmlc_img = 'N:/MedicalPhysics/Quality Control Program/Treatment/Monthly/Junctions and Picket Fence/Unit 1 SN 3951/2020_03_10/DRGS/ZPHYSICS_MONTHLY_U1/RI.ZPHYSICS_MONTHLY_U1.MV_208_0a.dcm'

mydrgs = DRGS(image_paths=(open_img, dmlc_img))

mydrgs.analyze(tolerance=1.5)
# print results to the console
print(mydrgs.results())
# view analyzed images
mydrgs.plot_analyzed_image()
mydrgs.publish_pdf('drgs.pdf')