import flet as ft 
import cv2
import base64
import threading
import time
from io import BytesIO
from PIL import Image

# OpenCV video capture
cap = cv2.VideoCapture(1)

def get_frame_base64():
    ret, frame = cap.read()
    if not ret:
        return None
    # Convert to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Convert to PIL image
    img = Image.fromarray(frame)
    # Save to buffer
    buf = BytesIO()
    img.save(buf, format="PNG")
    # Encode to base64
    base64_img = base64.b64encode(buf.getvalue()).decode("utf-8")
    return base64_img

def main(page: ft.Page):
    page.title = "Real-Time Camera Feed"
    cam_image = ft.Image(width=640, height=480,)
    main_content = ft.Container(
        content=cam_image,
        alignment=ft.alignment.center,
        expand=True,
    )
    page.add(main_content)

    # Function to update the camera image
    def update_loop():
        while True:
            frame_b64 = get_frame_base64()
            if frame_b64:
                cam_image.src_base64 = get_frame_base64()
                page.update()
            time.sleep(1/30)  # ~30 FPS

    # Run camera loop in background
    threading.Thread(target=update_loop, daemon=True).start()

ft.app(target=main)
