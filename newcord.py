## This function for a subject moving fron certain coordinates to other coordiantes and calcuates the new coordinates after a certain distance with bearing are traveled
import math
from geographiclib.geodesic import Geodesic # Make sure you install geographiclib  library before running this code.

def newcord(lon,lat,lonb,latb): # Lon, Lat>>current. lonb,latb>> Where the subject is heading ( in our case these are the broadcasted coordniates) 
     
     R = 6378.1 #Radius of the Earth
     brng = Geodesic.WGS84.Inverse(lon, lat, lonb, latb)['azi1']  # Calculate the bearing of the travel
     lat1 = math.radians(lat) #Current lat point converted to radians
     lon1 = math.radians(lon) #Current lon point converted to radians
     d = .005 #Distance traveled in km>> this is assuming the subject  travels at a constant speed of  5 m/s
     
     ##  Calcuating the Lat and Lon points if the device traveled the distance and bearing
     lat2 = math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng)) ##  Calcuating the Lat point if the device traveled the distance and bearing
     lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
     
     #Converting lon2 and lat2 to decimal
     lat2 = math.degrees(lat2)
     lon2 = math.degrees(lon2)
     
     return lon2, lat2




newlon,newlat= newcord( -77.920830,34.175038, -77.941166,34.184132) ### You can call the function as you can be seen here. 


