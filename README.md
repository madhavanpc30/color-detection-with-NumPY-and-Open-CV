# color-detection-with-NumPY-and-Open-CV
A real-time computer vision project using Python and OpenCV that performs background substitution through color detection and motion tracking, creating the effect of an object seamlessly blending into its surroundings.

## 🧭 Instructions

Follow these steps to properly use the project and achieve the best results:

### 1. Prepare the Environment
- Ensure your webcam is connected and functioning.  
- Set up the camera in a stable position facing a static background.  
- Avoid moving the camera once the program starts.

### 2. Capture the Background
- When the program starts, it captures the background for the first few seconds.  
- Stay **out of the frame** during this time so a clean background is recorded.  
- You can adjust the background capture duration in the code (typically 3–5 seconds).

### 3. Select the Target Color
- The program detects a specific color (default: **red**) to make it "invisible".  
- To change the color, modify the HSV range variables in the script:
  ```python
  lower_red = np.array([0, 120, 70])
  upper_red = np.array([10, 255, 255])
