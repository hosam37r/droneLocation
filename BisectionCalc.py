#Calculates the location using a bisectional method
#Assumes the max distance is 1 mile


import geocoder
import math

range=1 #in miles
longDegree=54.6
latDegree=69.172
longChange=range/longDegree #longitude change in degree from the range
latChange=range/latDegree #latitude change in degree from the range

def getCurrent():
    '''gets the lat long of current position in a list'''
    loc=geocoder.location('me')
    return loc

def longCalc(curCoor):
    '''Calculates the number of miles in 1 degree of longitude'''
    long=curCoor[0]*math.pi/180
    long=math.cos(long)
    longChange = range/(long*latDegree)

def calcMinLat(curCoor):
    '''calculates the minimum lat value for the location'''
    return curCoor[0]-latChange

def calcMaxLat(curCoor):
    '''calculates the maximum lat value for the location'''
    return curCoor[0]+latChange

def calcMinLong(curCoor):
    '''calculates the minimum long value for the location'''
    return curCoor[1]-longChange

def calcMaxLong(curCoor):
    '''calculates the maximum long value for the location'''
    return curCoor[1]+longChange

