import math
from geographiclib.geodesic import Geodesic

def newcord(x,y,xb,yb):
R = 6378.1 #Radius of the Earth
brng = Geodesic.WGS84.Inverse(x, y, xb, yb)['azi1']  #bearing
lat1 = math.radians(x) #Current lat point converted to radians
lon1 = math.radians(y) #Current long point converted to radians
d = .005 #Distance in km>> this is assuming the dorne travel 5 m/s

lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
     math.cos(lat1)*math.sin(d/R)*math.cos(brng))

lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
             math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

lat2 = math.degrees(lat2)
lon2 = math.degrees(lon2)

return lon2, lat2
