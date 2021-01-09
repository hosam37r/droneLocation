##The prupose of this function is to simulate drone movement. To find which bearing it is going to head to based on the broadcasted Coordinates 
import math
from geographiclib.geodesic import Geodesic # Make sure you install geographiclib  library before running this code.

def drone_sim(lon,lat): # Lon, Lat>>braodcasted. lonb,latb>> Where the subject is heading ( in our case these are the broadcasted coordniates) 
     
     #Launch location of drone. 
     ## It is hardcoded here. The puprose of this code is to simulate 
     lnch_lon= -77.873886
     lnch_lat=34.241753
     
     R = 6378.1 #Radius of the Earth
     brng = Geodesic.WGS84.Inverse(lon, lat, lnch_lon, lnch_lat)['azi1']  # Calculate the bearing of the travel
     
     
     return brng




bearing= drone_sim( -77.920830,34.175038) ### You can call the function as you can be seen here. 


