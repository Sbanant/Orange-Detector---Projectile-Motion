# Orange Motion Detection and Prediction

This project detects the motion of an orange in a video, predicts its future motion using Kalman filtering, and visualizes both the current and predicted positions. The main concept leveraged here is **Projectile Motion**, where the orange moves along a curved path under the influence of gravity and possibly other forces. The project includes:

- **Current Position Tracking**: Displays the current position of the orange.
- **Predicted Position**: Uses Kalman filter to estimate future positions.
- **Trajectory Visualization**: Plots the trajectory on a blue background image.

## Files in the Project

1. `kalmanfilter.py`: Implements Kalman Filter for predicting the trajectory of the orange based on its detected positions.
2. `orange_detector.py`: Detects the orange in the video using color-based masking and contour detection.
3. `main.py`: Plots the positions (current and predicted) of the orange on the selected background.
4. `orange_prediction.py`: Main script that combines the detection and prediction of the orange's trajectory in a video.

## How It Works

### Orange Detection

We detect the orange by converting the video frame to the **HSV color space** and creating a mask for the orange color range. We then find contours to detect the orange's position in each frame.

### Kalman Filter for Prediction

The **Kalman Filter** is used to predict the future position of the orange based on its current motion. Kalman filters are ideal for estimating the state of a moving object where noise is present in the measurement. It smooths out the trajectory and helps in accurately predicting where the orange will be in the near future.

### Visualization

The project outputs a video with:
- A **red circle** showing the current detected position of the orange.
- A **blue circle** showing the predicted position based on Kalman filtering.

It also plots the positions of the detected and predicted trajectory on a **blue background**.
