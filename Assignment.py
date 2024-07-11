import cv2
from numpy import array, zeros_like

# Load the image
image = cv2.imread('path_to_image.jpg')

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color range for the red rectangle (boundary)
lower_red = array([0, 100, 100])
upper_red = array([10, 255, 255])
mask_red = cv2.inRange(hsv_image, lower_red, upper_red)

# Define color range for the blue paint
lower_blue = array([100, 150, 0])
upper_blue = array([140, 255, 255])
mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Find contours for the red mask
contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
boundary_contour = max(contours, key=cv2.contourArea)

# Create a binary mask of the boundary
boundary_mask = zeros_like(mask_red)
cv2.drawContours(boundary_mask, [boundary_contour], -1, 255, thickness=cv2.FILLED)

# Check if any blue pixels are outside the red boundary
outside_boundary = cv2.bitwise_and(mask_blue, cv2.bitwise_not(boundary_mask))

# Count non-zero pixels in the result
num_outside_pixels = cv2.countNonZero(outside_boundary)

if num_outside_pixels > 0:
    print("Border Crossed")
else:
    print("Within Boundaries")

# Optional: Visualization
output_image = image.copy()
output_image[outside_boundary > 0] = [0, 0, 255]  # Mark crossing points in red
cv2.imshow('Analysis Result', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
