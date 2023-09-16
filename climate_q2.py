import matplotlib.pyplot as plt
import pandas as pd

# Load data from given csv file
df = pd.read_csv('climate.csv')

# Add values to lists
years = df['Year'].tolist()
co2 = df['CO2'].tolist()
temp = df['Temperature'].tolist()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

