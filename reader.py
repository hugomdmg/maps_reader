import pandas as pd
import rasterio

class Reader:
    def readCsv(route):
        return pd.read_csv(route)
    
    def readTif(route):
        with rasterio.open(route) as dataset:
            return dataset.read(1)
        
    def exportCsv(file_path1, res = 1):
        convertedObject = []
        with rasterio.open(file_path1) as dataset:
            width = dataset.width
            height = dataset.height
            data = dataset.read(1)

            for y in range(height):
                if y%res == 0:
                    for x in range(width):
                        if x%res == 4:
                            if(data[y, x] != 206):
                                x1 = 360*x/width
                                y1 = 180*y/height - 180
                                convertedObject.append({
                                    'lat': y1 * 2 * 3.14 / 360, 
                                    'lon': -x1 * 2 * 3.14 / 360, 
                                    'h': data[y, x]})
            df1 = pd.DataFrame(convertedObject)
            file_path2 = file_path1[:-3] + 'csv'
            df1.to_csv(file_path2)
            print('sucessfully converted: '+file_path2)
