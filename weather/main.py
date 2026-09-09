import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class Station:
    def __init__(self, location):
        self.location = location
        self.data = None

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
        print(f"--- Data loaded for {self.location} ---")
        print(self.data.head())

    def process_data(self):

        self.data['Temp_C'] = (self.data['Temp_F'] - 32) * 5 / 9
        print("\n--- Math complete: Added Temp_C column ---")
        print(self.data.head())

    def predict_future(self, future_year):
        years = self.data['Year']
        temps = self.data['Temp_C']


        slope, intercept = np.polyfit(years, temps, 1)


        prediction = (slope * future_year) + intercept
        print(
            f"\n>>> AI PREDICTION: The average temperature in {self.location} in {future_year} will be {prediction:.2f} °C <<<")


        return slope, intercept

    def plot_data(self, slope, intercept, future_year):

        plt.scatter(self.data['Year'], self.data['Temp_C'], color='blue', label='Historical Data')


        all_years = np.append(self.data['Year'].values, future_year)
        trend_line = (slope * all_years) + intercept

        plt.plot(all_years, trend_line, color='red', linestyle='--', label='AI Trendline')


        plt.title(f"{self.location} Climate AI Prediction")
        plt.xlabel("Year")
        plt.ylabel("Temperature (°C)")
        plt.legend()
        plt.grid(True)
        plt.show()



years = np.arange(2000, 2025)
base_temp = 60
warming_trend = np.linspace(0, 5, len(years))
noise = np.random.normal(0, 2, len(years))

temps_f = base_temp + warming_trend + noise


df = pd.DataFrame({"Year": years, "Temp_F": temps_f})
df.to_csv("weather.csv", index=False)
print("Generated weather.csv!\n")

my_station = Station("Hamirpur")
my_station.load_data("weather.csv")
my_station.process_data()


m, b = my_station.predict_future(2050)


my_station.plot_data(m, b, 2050)