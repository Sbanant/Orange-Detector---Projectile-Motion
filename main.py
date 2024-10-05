import cv2
# Function to extract positions from the video
def extract_positions(video_path):
    cap = cv2.VideoCapture(video_path)
    positions = []

    if not cap.isOpened():
        print("Error: Could not open video.")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video.")
            break

        # Convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define color ranges
        lower_red = (0, 100, 100)
        upper_red = (20, 255, 255)
        lower_blue = (110, 50, 50)
        upper_blue = (130, 255, 255)

        # Threshold the HSV image to get only red and blue colors
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

        # Find contours for red and blue circles
        contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours_red:
            # Assuming only one red object, take the centroid of the largest contour
            contour_red = max(contours_red, key=cv2.contourArea)
            M = cv2.moments(contour_red)
            red_x = int(M["m10"] / M["m00"])
            red_y = int(M["m01"] / M["m00"])
            positions.append(("red", (red_x, red_y)))

        if contours_blue:
            # Assuming only one blue object, take the centroid of the largest contour
            contour_blue = max(contours_blue, key=cv2.contourArea)
            M = cv2.moments(contour_blue)
            blue_x = int(M["m10"] / M["m00"])
            blue_y = int(M["m01"] / M["m00"])
            positions.append(("blue", (blue_x, blue_y)))

    cap.release()
    return positions

# Function to plot trajectory on blue background image
def plot_trajectory(background_img, positions):
    if background_img is None:
        print("Error: Could not load background image.")
        return None

    for color, pos in positions:
        if color == "red":
            cv2.circle(background_img, pos, 10, (0, 0, 255), -1)  # Draw red dot for current position
        elif color == "blue":
            cv2.circle(background_img, pos, 10, (255, 0, 0), -1)  # Draw blue dot for future position
    return background_img

# Path to the input video
video_path = "C:/Users/anant/Downloads/Pysource-Kalman-filter/output_video.mp4"

# Read the blue webp image
background_img = cv2.imread("C:/Users/anant/Downloads/Pysource-Kalman-filter/Pysource Kalman filter/blue_background.webp")

# Extract positions from the video
positions = extract_positions(video_path)

if positions is not None:
    # Plot the trajectory on the blue background image
    result_img = plot_trajectory(background_img, positions)

    if result_img is not None:
        # Show the image with trajectory
        cv2.imshow("Trajectory on Blue Background", result_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("Error: No positions extracted from the video.")
