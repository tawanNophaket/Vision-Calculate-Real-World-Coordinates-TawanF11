# Vision Calculate X, Y, Z Real World Coordinates

### Weekly progress : 
Please submit the mission progress report weekly, with the count beginning on Monday.
https://drive.google.com/drive/folders/1GHSxOlMksPtX5ELdGl0nE9wDlvAI7Dgg?usp=sharing
### Mission:
The objective of this project is to calculate the real-world X, Y, and Z coordinates of a ball relative to the Webcam Rapoo C260. The system will measure the distance (depth) between the ball and the camera, as well as provide the (x, y) coordinates when compared to the camera position (0,0). Additionally, the diameter of the ball should be determined as close as possible to its real-world size.

---

## Scenario

1. **Ball Detection:** Detect the ball in front of the camera. This requires image processing techniques such as object detection and instance segmentation.
2. **Camera Setup:** The camera is placed at position (0,0) and three balls are positioned at (-1000, 2000), (0,1000), and (800,1000) in millimeters.
3. **Day/Night Calibration:** The system should work in both day and night environments, with the ability to calibrate the camera before testing.

---

## Dataset
You can download the dataset used for testing and training the model from the following link:  
[Dataset Link](https://drive.google.com/drive/folders/1CtUM9Ws3VJKr09Ehsu-97xzHhIW0mnpS?usp=drive_link)

---

## Environment Setup

- **Testing Location:** The test will take place on the third-floor platform.
- **Camera Position:** The camera is elevated from the floor.
- **Time of Testing:** Tests will be conducted during both day and night, without specific time constraints.

---

## Validation Criteria

1. The model/algorithm should successfully detect the ball and differentiate it by color.
2. It should return the distance in two axes as coordinates (x, y), relative to the camera's position at (0, 0), and calculate the distance between the ball and the Webcam Rapoo C260.
3. The system should also return the diameter of the ball in millimeters.
4. **Input Parameters:**
    - Color of the ball to detect.
    - Return the coordinates (x, y) and the diameter of the ball in millimeters.
    - Options for output:
      - Return the nearest ball's coordinates.
      - Return the most confidently detected ball's coordinates.

---

## Equipment List

| Equipment            | Quantity |
|----------------------|----------|
| Webcam Rapoo C260     | 1        |
| Tripod                | 1        |
| Ball                  | 6        |

---

## Variable Flexibility

- The system should allow for flexible adjustments of variables through global settings.
- Please follow the naming conventions outlined in this [article](https://khalilstemmler.com/blogs/camel-case-snake-casepascal-case/#Comparison-of-naming-conventions-in-other-programming-languages).

---

## How to Submit Work

- Use **GitHub** to submit all work.
- Commit at least **3 times per week**. Each commit should clearly describe the changes made in **English**.
- Fork the repository [Vision-Calculate-Real-World-Coordinates](https://github.com/Lworakan/Vision-Calculate-Real-World-Coordinates.git) and append your name to it (e.g., Vision-Calculate-Real-World-Coordinates-AthizF10).

---
## Timeline

The project duration is from **October 7, 2024, to November 7, 2024**. The final commit must be made before 23:59 on November 7, 2024.

---

## Resources

Please refer to the following link for knowledge and resources on **camera calibration and 3D reconstruction**:  
[OpenCV Camera Calibration](https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html)

---

## Please remind to create the Instructions for Use 

All of you need to create the topic na krubb
