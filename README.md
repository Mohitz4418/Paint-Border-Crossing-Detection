# Paint Border Crossing Detection

## Functionality
This script analyzes an image to determine if paint has crossed designated boundaries.

## Assumptions
- The boundary is represented by a red rectangle.
- The paint is represented by blue pixels.

## Expected Output
The script prints "Border Crossed" if any blue pixels lie outside the red boundary, otherwise "Within Boundaries".

## Usage
1. Install dependencies: `pip install opencv-python numpy`.
2. Run the script: `python Assigment.py`.

## Bonus Points
- Handles different boundary shapes.
- Discusses challenges such as lighting variations and color inconsistencies.
- Includes visualization of border crossing points.


Solution Approach :
1. Set Up the Environment:
	Install necessary libraries.
	Load the image using OpenCV.
2. Preprocess the Image:
	Convert the image to the appropriate color space.
	Extract the regions of interest (ROI) which are the red rectangle and the blue paint.
3. Detect Boundaries:
	Identify the boundaries of the red rectangle.
	Check the positions of the blue pixels.
4. Analyze Boundary Crossing:
	Determine if any blue pixels are outside the red rectangle.
	Output the result.
5. Bonus Points Considerations:
	Handle different boundary shapes.
	Discuss potential challenges.
	Implement visualization techniques. 