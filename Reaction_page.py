import flet as ft 
import cv2
import base64
import threading
import time
import os
import subprocess
from io import BytesIO
from PIL import Image



def get_asset_path(filename):
    return os.path.join(os.path.dirname(__file__),filename)

# OpenCV video capture
cap = cv2.VideoCapture(1)
#function declaration



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


#main
def main(page: ft.Page):
    
    def Reaction_page(e):
        # script_path=os.path.join(os.path.dirname(__file__),"Reaction_page.py")
        # subprocess.Popen(["python",script_path])
        # page.window.close()
        return

    def Levels_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Levels_page.py")
        subprocess.Popen(["python",script_path])
        page.window.close()
        
    def inyection_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Inyection_page.py")
        subprocess.Popen(["python",script_path])
        page.window.close()

    def co_levels_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"co_levels_page.py")
        subprocess.Popen(["python",script_path])
        page.window.close()
        
# code of the camera 
    page.title = "Real-Time Camera"
    cam_image = ft.Image(width=640, height=480,)

    camera_content = ft.Container(

        border=ft.border.all(10,ft.Colors.BLUE),
        content=cam_image,
        alignment=ft.alignment.center,
        expand=True,)
    

 
#button declaration
    reaction_button = ft.Container(
        ft.Text("Reaction", color=ft.Colors.WHITE),
        on_click=Reaction_page,
        bgcolor="#BF5D17",
        width=200,
        padding=10,
        border_radius=5,
        alignment=ft.alignment.center,
    )
    levels_button = ft.Container(
        ft.Text("Levels", color=ft.Colors.WHITE),
        on_click=Levels_page,
        bgcolor="#BF5D17",
        width=200,
        padding=10,
        border_radius=5,
        alignment=ft.alignment.center,
    )
    inyection_button = ft.Container(
        ft.Text("Injection", color=ft.Colors.WHITE),  # Corrected typo
        on_click=inyection_page,
        bgcolor="#BF5D17",
        width=200,
        padding=10,
        border_radius=5,
        alignment=ft.alignment.center,
    )
    co_levels_button = ft.Container(
        ft.Text("CO₂ Levels", color=ft.Colors.WHITE),
        on_click=co_levels_page,
        bgcolor="#BF5D17",
        width=200,
        padding=10,
        border_radius=5,
        alignment=ft.alignment.center,
    )

    #here is the column for the button and text in the top
    navigation = ft.Column(
        controls=[
            ft.Text("BIOBLAST", size=30, weight="bold"),
            ft.Text("Plastic Degradation", size=20),
            ft.Row([inyection_button, co_levels_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([reaction_button, levels_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Text("Reaction", size=20, weight="bold"),
          
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center column contents
    )

     
    page.add(navigation,camera_content)

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
