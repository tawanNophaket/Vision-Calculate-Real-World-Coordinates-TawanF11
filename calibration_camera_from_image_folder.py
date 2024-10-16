import cv2
import numpy as np
import os

# เริ่มการคาลิเบรทกล้อง
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
chessboard_size = (9,6)  # ขนาดของ chessboard ที่ใช้ในการคาลิเบรท
objp = np.zeros((chessboard_size[0]*chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

objpoints = []  # เก็บตำแหน่งของจุดในโลกจริง (3D)
imgpoints = []  # เก็บตำแหน่งของจุดในภาพ (2D)

# เปิดรูปภาพจากโฟลเดอร์ calibration_img
if not os.path.exists('calibration_img'):
    print("No calibration images found. Please add images to the 'calibration_img' folder.")
    exit()

# สร้างโฟลเดอร์ calibration_draw หากยังไม่มี
if not os.path.exists('calibration_draw'):
    os.makedirs('calibration_draw')

images = os.listdir('calibration_img')

for fname in images:
    img_path = os.path.join('calibration_img', fname)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Failed to load image {img_path}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ค้นหามุมของ chessboard
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if ret:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # แสดงมุมที่พบในภาพ
        cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)
        cv2.imshow('Calibration', img)
        cv2.waitKey(500)

        # บันทึกภาพที่ทำการคาลิเบรทลงในโฟลเดอร์ calibration_draw
        draw_path = os.path.join('calibration_draw', fname)
        cv2.imwrite(draw_path, img)

cv2.destroyAllWindows()

# ทำการคาลิเบรทกล้อง
if len(objpoints) > 0 and len(imgpoints) > 0:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    if ret:
        print("Camera calibrated successfully!")
        print("\nCamera matrix (Intrinsic Parameters):")
        print(mtx)
        print("\nExplanation: The camera matrix contains the focal lengths (fx, fy) and the optical center (cx, cy).\n")
        print(f"Focal Lengths (fx, fy): {mtx[0, 0]:.2f}, {mtx[1, 1]:.2f}")
        print(f"Optical Center (cx, cy): {mtx[0, 2]:.2f}, {mtx[1, 2]:.2f}")
        print("\nDistortion coefficients:")
        print(dist)
        print("\nExplanation: The distortion coefficients are used to correct lens distortion, including radial and tangential distortion.\n")
        print(f"Radial Distortion (k1, k2, k3): {dist[0, 0]:.5f}, {dist[0, 1]:.5f}, {dist[0, 4]:.5f}")
        print(f"Tangential Distortion (p1, p2): {dist[0, 2]:.5f}, {dist[0, 3]:.5f}")
        # บันทึกค่าที่ได้ลงไฟล์
        np.save("camera_mtx.npy", mtx)
        np.save("camera_dist.npy", dist)
    else:
        print("Camera calibration failed.")
else:
    print("Not enough points for calibration. Please provide more calibration images.")