
import math
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

a,b,c,d=guessrange( -77.870654, 34.221926)

