#!/usr/bin/python
from geographiclib.geodesic import Geodesic # Make sure you install geographiclib  library before running this code.
import math

  ###### below this point is functions

def guessrange(lon,lat): # Lon, Lat>>current.
     R = 6378.1 #Radius of the Earth
     lat1 = math.radians(lat) #Current lat point converted to radians
     lon1 = math.radians(lon) #Current long point converted to radians
     d = 1.609 #Distance in km>>
     brng1=0
     brng2=math.pi/2
     brng3=math.pi
     brng4=math.pi*1.5

     maxlat = math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng1))
     lat2 = math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng2))
     maxlon = lon1 + math.atan2(math.sin(brng2)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
     minlat = math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng3))
     lat2 = math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng4))
     minlon = lon1 + math.atan2(math.sin(brng4)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

     maxlat = math.degrees(maxlat)
     maxlon = math.degrees(maxlon)
     minlat = math.degrees(minlat)
     minlon = math.degrees(minlon)

     return maxlon, maxlat,minlon, minlat
  ###function 1 bi-section loop to find the lon
def findx( guess,a,b,f,k):
  x_speed=[k]
  i=1
  if f==1:
    lower =a
    upper=guess
  else:
    lower=guess
    print(lower)
    upper=a
    print(upper)

  guess=lower+(upper-lower)/2
  print(guess)
  while True:
    br=drone_sim(guess,b)
    x_speed.append(5 * math.cos(br))
    if abs(x_speed[i])<.01:
      return x_speed,guess
    if x_speed[i]> x_speed[i-1]:
      upper=guess
      guess=lower+(upper-lower)/2
    else:
      lower=guess
      guess=lower+(upper-lower)/2
    i=i+1

 
###function 1 bi-section loop to find the lat.

def findy( guess,a,b,f):
  y_speed=[0]
  i=1
  if f==1:
    lower =b
    upper=guess
  else:
    lower=guess
    upper=b
  guess=lower+(upper-lower)/2
  while True:
    br=drone_sim(a,guess)
    yspeed.append(5 * math.cos(br)) 
    if abs(y_speed[i])<.01:
      return y_speed,guess
    if y_speed[i]> y_speed[i-1]:
      upper=guess
      guess=lower+(upper-lower)/2
    else:
      lower=guess
      guess=lower+(upper-lower)/2
    i=i+1
      
## function 3. it finds the maximum range of guesses      


      
    
    
    
    
## Function 4 to simulate drone movement 

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








#Current drone location 
a=-77.870654
b= 34.221926 

### Lets define list of how x direction speed and y direction speed change through the code
xspeed=[0]
yspeed=[0]

# Guess ranges.
maxlon,maxlat,minlon,minlat= guessrange(a,b) ## This function i wrote to calculate the max range for a,b above with range of 1 mile.


br= drone_sim(maxlon,b)
xspeed.append(5 * math.cos(br)) 

br= drone_sim(minlon,b)
xspeed.append(5 * math.cos(br))



if xspeed[1]> xspeed[2]:
  xspeedlist, lon_fix=findx(minlon,a,b,0,xspeed[2])
else:
  xspeedlist, lon_fix=findx(maxlon,a,b,1,xspeed[1])
  
 
br= drone_sim(a,maxlat)
yspeed.append(5 * math.sin(br)) 

br= drone_sim(a,minlat)
yspeed.append(5 * math.sin(br))



if yspeed[1]> yspeed[2]:
  yspeedlist, lat_fix=findy(minlat,a,b,0)
else:
  yspeedlist, lat_fix=findx(maxlat,a,b,1)
  

  
print(xspeedlist)
