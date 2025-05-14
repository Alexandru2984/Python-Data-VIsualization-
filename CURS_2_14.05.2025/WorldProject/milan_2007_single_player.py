import matplotlib.pyplot as plt
import matplotlib.image as mpimg

folder_name = "Milan2007"

first_image = folder_name + "/" + "00.Dida.png" 
# C:\Users\Micu\Desktop\python\python_data_visualization_09.05.2025\Python-Data-VIsualization-\CURS_2_14.05.2025\Curs2_Data_Visualization_19.05.2025\Milan2007
# C:\Users\Micu\Desktop\python\python_data_visualization_09.05.2025\Python-Data-VIsualization-\CURS_2_14.05.2025\WorldProject\milan_2007.py
figure, axis = plt.subplots()

imagine = mpimg.imread(first_image)
axis.imshow(imagine)
plt.show()