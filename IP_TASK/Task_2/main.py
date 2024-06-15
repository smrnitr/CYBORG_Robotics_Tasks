'''
*********************************************************************************
*
*        		===============================================
*           		        CYBORG OPENCV TASK 2
*        		===============================================
*
*
*********************************************************************************
'''

# Author Name:		[Smriti Srivastava]
# Roll No:			[123EI0639]
# Filename:			task_2_smriti.py
# Functions:		detect_arena_parameters
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
   ## You are free to make any changes in this section. ##
##############################################################
import cv2
import numpy as np

#for traffic signal and start node
color_range = {'RED': ([0, 70, 50], [10, 255, 255]), 'GREEN': ([35, 100, 100], [85, 255, 255])}

colors={'RED':[0,0,255],'GREEN':[0,255,0], 'PINK':[203, 192, 25],'ORANGE':[0, 165, 255],'BLUE':[255, 0, 0],'SKYBLUE':[235,206,135]}
letters='ABCDEFG'
##############################################################

def detect_arena_parameters(maze_image):
	

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a dictionary
	containing the details of the different arena parameters in that image

	The arena parameters are of four categories:
	i) traffic_signals : list of nodes having a traffic signal
	ii) horizontal_roads_under_construction : list of missing horizontal links
	iii) vertical_roads_under_construction : list of missing vertical links
	iv) medicine_packages : list containing details of medicine packages
	v)start_node : list containing the start node

	These four categories constitute the four keys of the dictionary
 """
        arena_parameters = {'traffic_signals': [], 'start_node': [],'horizontal_roads_under_construction': [], 'vertical_roads_under_construction': [], 'medicine_packages_present': []}
        
	img_rgb=cv.cvtColor(maze_image,cv.COLOR_BGR2RGB)
	img_hsv=cv.cvtColor(maze_image,cv.COLOR_BGR2HSV)
	img_gray=cv.cvtColor(maze_image,cv.COLOR_BGR2GRAY)

        #for traffic signals
        for color,(lower,upper) in color_range.items():
		llim=np.array(lower) #lower limit
		ulim=np.array(upper) #upper limit
		mask = cv.inRange(hsv_image, llim, ulim)
        contours, hierarchies = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for contour in contours:
   
            x1, x2, y1, y2 = cv.boundingRect(contour)
          
            if color == 'RED' and cv.contourArea(contour) > 100:
                node= f"{letters[x1 // 100]}{x2 // 100 + 1}"
                arena_parameters['traffic_signals'].append(node)
            elif color == 'GREEN' and cv.contourArea(contour) > 100:
                node = f"{letters[x1// 100]}{x2 // 100 + 1}"
                
             # Mentioning start node
                if len(arena_parameters['start_node']) == 0: 
                    arena_parameters['start_node'].append(node)

		
		
	
        
    
"""
	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`arena_parameters` : { dictionary }
			dictionary containing details of the arena parameters
	
	Example call:
	---
	arena_parameters = detect_arena_parameters(maze_image)
	"""    
	arena_parameters = {}

	##############	ADD YOUR CODE HERE	##############

	##################################################
	
	return arena_parameters
