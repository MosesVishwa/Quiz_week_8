import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect('climate.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM ClimateData")

results = cursor.fetchall()

years = []
co2 = []
temp = []

# put into lists
for r in results:
    years.append(r[0])
    co2.append(r[1])
    temp.append(r[2])

# Close database and cursor connection
cursor.close()
connection.close()

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
plt.savefig("co2_temp_1.png")


