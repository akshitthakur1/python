import panda as pd
import numpy as np
class station:
    def __init__(self,location):
        self.location = location
        self.data = None

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)






my_station = station("Hamirpur")

