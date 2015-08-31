import numpy as np
import pyfits
import matplotlib.pyplot as plt
import matplotlib
import math
from pydl.photoop.photoobj import unwrap_objid

#open image
#calculate center of image and input that as guess of centroid
#extract box around calculated centroid
#rotate box and subtract the two arrays
#normalize if necessary
#calculate

dr7objid = 587722952230175035 #currently using dr7objid of entry #2 of combined1_half1 (first spiral galaxy)

params = unwrap_objid(array([587722952230174000])) [0] #returns list of skyversion, rerun, camcol, frame (field), id

imgData= pyfits.getdata("sampleimage.fits") #extracts array of pixel values
plt.imshow(imgData)
plt.gray()
#plt.show()
centerX = input("Please enter center X coordinate: ") #gets user input center x coord of star, try 1055 for this image
centerY = input("Please enter center Y coordinate: ") #gets user input center y coord of star, try 350 for this image
centroidX = 0
centroidY = 0
side = input("Please enter the side length of the square you would like to analyze, in pixels: ") #try 20 for this image, any smaller is not big enough for star


def getImageData():
    
    selectedData = imgData[centerY - side/2:centerY + side/2 + 1,
                           centerX - side/2:centerX + side/2 + 1]
##    print centerY - side/2
##    print centerY + side/2 + 1
##    print centerX - side/2
##    print centerX + side/2 + 1
##    print np.shape(selectedData)
##    plt.imshow(selectedData)
##    #plt.show()
    return selectedData

def calculateCentroid(selectedData): #calculates weighted averages
    sumIntensities = np.sum(selectedData)
    weightedX = np.empty((side,side)) 
    weightedY = np.empty((side,side))
    for i in range(selectedData.shape[0]):
        for k in range(selectedData.shape[1]):
            weightedY[i][k] = (i + 1)*selectedData[i][k]#multiplies each weighted pixel by its position
            weightedX[i][k] = (k + 1)*selectedData[i][k]
    sumX = np.sum(weightedX)#sums weighted averages
    sumY = np.sum(weightedY)#sums weighted averages
    centroidX = sumX/sumIntensities #Divides sum of x values by sum of intensities to get weighted mean for X coordinates
    centroidY = sumY/sumIntensities ##Divides sum of y values by sum of intensities to get weighted mean for Y coordinates
    actualX = centroidX + centerX - side/2 - 1 #adds calculated centroid difference to actual center pixel, adjusting by -1 for shift in matrix indices
    actualY = centroidY + centerY - side/2 - 1
    print "Centroid: (", actualX, "," , actualY, ")"
    getUncertainty(actualX, actualY, selectedData, sumIntensities) #calculates uncertainties for centroid calculations
    
calculateCentroid(getImageData())


