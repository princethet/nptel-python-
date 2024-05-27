import csv
from gmplot import gmplot
gmap = gmplot.GoogleMapPlotter(28.675432,77.234567,17)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('route.csv','r') as f:
    reader = csv.reader(f)
    k = 0
    # row = 1
    for row in reader:
        lat = float(row[8])
        long = float(row[9])
        if(k==0):
            gmap.marker(lat,long,'yellow')
            k = 1
        else:
            gmap.marker(lat,long,'blue')
    gmap.marker(lat,long,'red')
    gmap.draw("mymap.html")