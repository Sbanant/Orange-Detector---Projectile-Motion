import cv2
from orange_detector import OrangeDetector
from kalmanfilter import KalmanFilter

# Video file paths
input_video_path = "C:/Users/anant/OneDrive/Pictures/Camera Roll/WIN_20240222_09_13_38_Pro.mp4"
output_video_path = "output_video.mp4"

# Open the input video file
cap = cv2.VideoCapture(input_video_path)

# Get the video's frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (frame_width, frame_height))

# Load detector
od = OrangeDetector()

# Load Kalman filter to predict the trajectory
kf = KalmanFilter()

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    orange_bbox = od.detect(frame)
    x, y, x2, y2 = orange_bbox
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)

    predicted = kf.predict(cx, cy)
    cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 4)
    cv2.circle(frame, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)

    # Write the frame into the output video
    out.write(frame)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(150)
    if key == 27:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
