#Calculates the location using a bisectional method
#Assumes the max distance is 1 mile

import geocoder
import math

range=1#in miles
longChange=54.6*range
latChange=69.172*range

def getCurrent():
    loc=geocoder.location('me')
    return loc

def longCalc(curCoor):
    long=curCoor[0]*math.pi/180
    long=math.cos(long)
    longChange = long*latChange
