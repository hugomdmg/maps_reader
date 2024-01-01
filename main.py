import matplotlib.pyplot as plt
import numpy as np
from reader import Reader

class Maps:
    def shadowMap(path):
        color = []
        previousValue = 0
        data = Reader.readCsv(path)

        for i in data.itertuples():
            value = i.value - previousValue
            if(i.value and value != 0):
                c = 5 if value > 0 else -5
            color.append(255/abs(50*value + c))
            previousValue = i.value
            
        size = int(len(color)**(1/2))
        colorFormat = np.array(color).reshape(size, size)

        plt.imshow(colorFormat, cmap='viridis')
        plt.show()

    def altitudeMap(path):
        color = []
        data = Reader.readCsv(path)
        
        for i in data.itertuples():
            value = i.value
            if(i.value and value != 0):
                if(value%20 < 0.5):
                    value = 0
            color.append(value)

        size = int(len(color)**(1/2))
        colorFormat = np.array(color).reshape(size, size)

        plt.imshow(colorFormat, cmap='viridis')
        plt.show()

    def printPlanet(path):
        data = Reader.readTif(path)
        plt.imshow(data, cmap='magma')
        plt.show()


files = ['./lidar_data/earth.tif',
         './lidar_data/Lunar_DEM_118m.tif',
         './lidar_data/Europa_Voyager_GalileoSSI_500m.tif',
         './lidar_data/Venus_Magellan_2025m.tif',
         './lidar_data/Mercury_Messenger_665m.tif'
         ]
lidar = ['./lidar_data/PNOA_penalara.csv',
         './lidar_data/PNOA_matalascanas.csv',
         './lidar_data/PNOA_duraton.csv']

print('\nChoose option:\n')
menuOption = int(input('1: Print map .tif\n2: Print map .csv\n3: Export .tif to .csv\n'))
if menuOption == 1:
    print('=============')
    print('Choose planet:')
    option = int(input('1: Earth\n2: Moon\n3: Europa\n4: Venus\n')) - 1
    Maps.printPlanet(files[option])

if menuOption == 2:
    print('=============')
    print('Choose kind of map:\n')
    mapOption = int(input('1: shadow map\n2: altitude map\n'))
    print('choose data:\n')
    dataOption = int(input('1: Penalara\n2: Matalascanas\n3: Duraton\n')) - 1

    if mapOption == 1:
        Maps.shadowMap(lidar[dataOption])
    if mapOption == 2:
        Maps.altitudeMap(lidar[dataOption])

if menuOption == 3:
    print('=============')
    print('Choose data:\n')
    option = int(input('1: Earth\n2: Moon\n3: Europa\n4: Venus\n')) - 1
    Reader.exportCsv(files[option], 40)

