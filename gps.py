#gps route ,
# requirement :-> csv file is needed of latitude and longitude
import csv
with open('route.csv','r') as f:
    reader  = csv.reader(f)
    for new in reader:
        lat =  float(row[0])
        lon =  float(row[1])
        print(lat)
        print(long)
        print(lat+long)