import cv2

aruco = cv2.aruco

dictionary = aruco.getPredefinedDictionary(aruco.DICT_5X5_50) 
# 5x5 for a balance between distance and accuracy. 50 markers, 0-49

# Marker creation
image = aruco.generateImageMarker(dictionary, 0, 200, 100)
# Missing a parameter

# Marker detection
detector_parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(dictionary, detector_parameters)