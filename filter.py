import pandas as pd
import matplotlib
import csv

rows = []
with open("main1.csv") as f:
    cvsreader = csv.reader(f)
    for row in cvsreader:
        rows.append(row)

header = rows[0]
star_data_row = rows[1:]

star_distance = []
star_mass = []
star_radius = []
star_gravity = []
for star_data in star_data_row:
    star_distance.append(float(star_data[2]))
    star_mass.append(float(star_data[3]))
    star_radius.append(float(star_data[4]))
    star_gravity.append(float(star_data[5]))

less_distance_star = []
for index,distance in enumerate(star_distance):
    if distance <= 100.0:
        less_distance_star.append(star_data_row[index])

gravity_list = []
for gravity_star in less_distance_star:
    gravity_list.append(float(gravity_star[5]))

print(gravity_list,len(gravity_list))

low_gravity_distance_row = []
for index,gravity in enumerate(gravity_list):
    if gravity >150 and gravity <350:
        low_gravity_distance_row.append(star_data_row[index])

print(low_gravity_distance_row)

with open("main2.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(low_gravity_distance_row)
