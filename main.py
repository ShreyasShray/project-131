import csv
import pandas as pd

# Creating a empty list to store data
star_data_rows = []

# Storing all data in a array
with open("final.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        star_data_rows.append(row)

star_data_rows.pop(0)

# print(star_data_rows)

# Creating empty list to store mass and radius of all stars
masses = []
radiuses = []

for star_data in star_data_rows:
    masses.append(float(star_data[3])*1.989e+30)
    radiuses.append(float(star_data[4])*6.957e+8)

# print(masses)
# print(radiuses)

gravity = []

for index, mass in enumerate(masses):
    temp_gravity = (mass/(radiuses[index]*radiuses[index]))*6.67e-11
    gravity.append(temp_gravity)

# print(gravity)

# Creating final list to store the gravity with all the data
final_star_list = []

for index, star_data in enumerate(star_data_rows):
    temp_star_list = star_data
    temp_star_list.pop(0)  # To remove the serial no.
    temp_star_list.append(gravity[index])
    final_star_list.append(temp_star_list)

# print(final_star_list)

df = pd.DataFrame(final_star_list, columns = ["name", "distance", "mass", "radius", "gravity"])
df.to_csv("star_data_with_gravity.csv")