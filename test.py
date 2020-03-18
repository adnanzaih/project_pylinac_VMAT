import pydicom
import matplotlib.pyplot as plt
import numpy as np

open_img = 'N:/MedicalPhysics/Quality Control Program/Treatment/Monthly/Junctions and Picket Fence/Unit 1 SN 3951/2020_03_10/DRGS/ZPHYSICS_MONTHLY_U1/RI.ZPHYSICS_MONTHLY_U1.MV_179_0a.dcm'
dmlc_img = 'N:/MedicalPhysics/Quality Control Program/Treatment/Monthly/Junctions and Picket Fence/Unit 1 SN 3951/2020_03_10/DRGS/ZPHYSICS_MONTHLY_U1/RI.ZPHYSICS_MONTHLY_U1.MV_208_0a.dcm'


image1 = pydicom.dcmread(open_img)
plt.imshow(np.rot90(image1.pixel_array))
plt.show()
