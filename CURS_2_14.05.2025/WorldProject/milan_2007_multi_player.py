import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
folder_name = "Milan2007"

first_image = folder_name + "/" + "00.Dida.png" 

figure, axis = plt.subplots(nrows=1, ncols=2)

imagine = mpimg.imread(first_image)
axis[0].imshow(imagine)
plt.show()


