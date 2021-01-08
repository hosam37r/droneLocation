from geographiclib.geodesic import Geodesic # Make sure you install geographiclib  library before running this code.
import math
#Current drone location 
a=-77.870654
b= 34.221926 

### Lets define list of how x direction speed and y direction speed change through the code
xpeed=[0]
yspeed[0]

# Guess ranges.
maxlon,maxlat,minlon,minlat=guessrange(a,b) ## This function i wrote to calculate the max range for a,b above with range of 1 mile.

# First guess maxlon maxlat)
longuess= maxlon
latguess=maxlat

br= Geodesic.WGS84.Inverse(a, b, longguess, latguess)['azi1'] ## bearing

xspeed.append(5 * math.cos(br)) ## assuming constant speed of 5 m/s which refelect to 10 mph
yspeed.append(5* math.sin(br))

#Now we get the current drone location 
a,b=newcord(a,b,longguess,latguess)

# 2nd guess maxlon maxlat)
longuess= minlon
latguess=minlat

br= Geodesic.WGS84.Inverse(a, b, longguess, latguess)['azi1'] ## bearing

xspeed.append(5 * math.cos(br)) 
xspeed.append(5 * math.cos(br))

#aagain  we get the current drone location 
a,b=newcord(a,b,longguess,latguess)

if xspeed[1]> xspeed[2]:
  longuess= minlon/2
else:
  longuess= maxlon/2

if uspeed[1]> yspeed[2]:
  latguess= minlat/2
else:
  latguess= maxlat/2
  

  
# Then we continue I need you to figure out how to loop this 



