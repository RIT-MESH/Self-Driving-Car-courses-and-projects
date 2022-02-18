import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_coordinates(image, line):
    """we can't actually draw them unless we also specify their coordinates to actually specify where we
    want our lines to be placed.The x1, y1 x2 and y2 for each line.
    So what we'll do is we'll define a function, doth make coordinates with argument, image and line parameters.
    """
    slope, intercept = line
    y1 = int(image.shape[0])
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])


def average_slope_intercept(image, lines):
    """
        This function combines line segments into one or two lane lines
    """
    left_fit = []  # contains the coordinate of on the line in the left
    right_fit = []
    if lines is None:
        return None
    # now loop through very line we did previously
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0:  # y is reversed in image
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))

        """now What polyfit will do for us is it will fit a first degree polynomial,
        which would simply be a linear function of Y= mx + b it's going to fit this polynomial to our X and Y
        points and return a vector of coefficients which describe the slope and Y intercept.
        """



    # add more weight to longer lines
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    averaged_lines = [left_line, right_line]
    return averaged_lines


# print(left_fit_average,'left' )
# print(right_fit_average,'right')




def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # converting color image to gray scale
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # blure image(reduction of noise) with kerne(5,5) and deviation is 0
    canny = cv2.Canny(blur, 50, 150)  # canny image with low and high threshold of 50 and 150 respectively
    return canny

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    #to check if lines are detected
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            #cv2.line('draw line in line_image', 2nd & 3rd arguments are for coordinates for lines,
            #then specify color(255,0,0) will show blue color, line thickness)
            cv2.line(line_image, (x1, y1), ( x2, y2), (255, 0, 0), 10)
    return line_image




#define an image, it will return closed region of our field view
def region_of_interest(canny):
    height = canny.shape[0]
    width = canny.shape[1]

    mask = np.zeros_like(canny)
    polygon = np.array([
    [(200, height), (1100, height), (550, 250)]
    ], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    mask_image = cv2.bitwise_and(canny, mask) #this will only show the region of interest
    return mask_image

# image = cv2.imread('test_image.jpg') #display image
# lane_image = np.copy(image)#copying our image in new variable
# canny_image =canny(lane_image)
# cropped_image = region_of_interest(canny_image) #cropping the region of interest
# lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
# averaged_lines = average_slope_intercept(lane_image, lines)
# line_image = display_lines(lane_image, averaged_lines)
# combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)#take sum of our color image with our line image
#
# #plt.imshow(canny)
# cv2.imshow("result", combo_image)
# cv2.waitKey(0) #this will show our window untill we close it
# #plt.show()

cap = cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    canny_image = canny(frame)
    cropped_image = region_of_interest(canny_image)  # cropping the region of interest
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)  # take sum of our color image with our line image

    # plt.imshow(canny)
    cv2.imshow("result", combo_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    #cv2.destroyAllWindows()
    #cv2.waitKey(1)  # this will show our window untill we close it
    # plt.show()