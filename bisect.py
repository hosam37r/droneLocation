from geographiclib.geodesic import Geodesic # Make sure you install geographiclib  library before running this code.
import math

#########################
#First we define the functions
############################################
####### Function 1 to find max range of lon and lat 
def guessrange(lon,lat): # Lon, Lat>>current.
     R = 6378.1 #Radius of the Earth
     lat1 = math.radians(lat) #Current lat point converted to radians
     lon1 = math.radians(lon) #Current long point converted to radians
     d = 1.609 #Distance in km>> 1 mile
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


#### function 2 to bisect for lon
def findx( guess,a,b,f):
  x_speed=[0]
  i=1
  if f==1:
    lower =a
    upper=guess
  else:
    lower=guess
    upper=a
  guess=lower+(upper-lower)/2

  while True:
    br=drone_sim(guess,b)
    x_speed.append(5 * math.cos(br * math.pi / 180))
    if abs(x_speed[i])<.01:
        return x_speed,guess
    if x_speed[i]< 0:
      upper=guess 
      guess=lower+(upper-lower)/2

    else:
      lower=guess
      guess=lower+(upper-lower)/2


    i=i+1
  
   ########fucntion 3 to bisect for lat  
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
    y_speed.append(5 * math.sin(br * math.pi / 180))
    if abs(y_speed[i])<.01:
        return y_speed,guess
    if y_speed[i]< 0:
      upper=guess 
      guess=lower+(upper-lower)/2

    else:
      lower=guess
      guess=lower+(upper-lower)/2


    i=i+1
  
  

### Function 4 to simulate drone movement. 
def drone_sim(lon,lat): # Lon, Lat>>braodcasted. lonb,latb>> Where the subject is heading ( in our case these are the broadcasted coordniates) 
     
     #Launch location of drone. 
     ## It is hardcoded here. The puprose of this code is to simulate 
     lnch_lon= -77.874886
     lnch_lat=34.211753
     
     R = 6378.1 #Radius of the Earth
     brng = Geodesic.WGS84.Inverse(lon, lat, lnch_lon, lnch_lat)['azi1']  # Calculate the bearing of the travel
     
     
     return brng


#####################################################################################
###Main function starts here
#a,b are the lon and lat where the drone is spotted before braodcasting anything
a=-77.870654
b= 34.221926 

##List to compare the speed of min(lat/lon) max(lat/lon)
xspeed=[0]
yspeed=[0]

maxlon,maxlat,minlon,minlat= guessrange(a,b) ## This function i wrote to calculate the max range for lon lat which is  in the range of 1 mile from a,b above

## First broadcast happens here we broadcast max then min and see which one generate less speed.
br= drone_sim(maxlon,b)
xspeed.append(5 * math.cos(br* math.pi / 180)) 

# to find the guess bounderies first we check which maxlon or minlon generate lessspeed
br= drone_sim(minlon,b)
xspeed.append(5 * math.cos(br* math.pi / 180))
if xspeed[1]> xspeed[2]:
  f=1
  guess=maxlon
else:
  f=0
  guess=minlon

print(findx( guess,a,b,f)) ## where guess is the intial guess. f is to show we selected maxlon or min lon based on the tedt in lines 124-132.

#Repeat above to find lat.
br= drone_sim(a,maxlat)
yspeed.append(5 * math.sin(br* math.pi / 180)) 

br= drone_sim(a,minlat)
yspeed.append(5 * math.sin(br* math.pi / 180))
if yspeed[1]> yspeed[2]:
  f=1
  guess=maxlat
else:
  f=0
  guess=minlat
 

print(findy( guess,a,b,f))

