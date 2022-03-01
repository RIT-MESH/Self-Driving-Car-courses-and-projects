# Lane detection

The goal of this project is to detect lanes in image, videos or live feed.

The procedure is as follow
1) select desired video or image
2) convert it into grayscale
3) apply noise reduction
4) apply the canny method to identify edges in our image or video.
5) specify a region of interest in image or video that we're going to use to detect our lines 
6) apply this mask on to our canny image to ultimately only show the region of interest.We do this by applying the bitwise operator.
7) apply Hough Transform to identify the lane in the region of interest
8) combine both Hough Transformed and original image or video to show marked lanes

 Original             |  Final output
:-------------------------:|:-------------------------:
![](https://github.com/RIT-MESH/Self-Driving-Car-courses-and-projects/blob/main/6%20Lane%20detection/original.gif)  |  ![](https://github.com/RIT-MESH/Self-Driving-Car-courses-and-projects/blob/main/6%20Lane%20detection/final%20output.gif)
