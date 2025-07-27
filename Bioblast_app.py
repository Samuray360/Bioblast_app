import flet as ft 
import cv2
import base64
import threading
import time
from io import BytesIO
from PIL import Image

# OpenCV video capture
cap = cv2.VideoCapture(1)


#function declaration
def Reaction_page():
    return
def Levels_page():
    return
def inyection_page():
    return
def co_levels_page():
    return

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
# code of the camera 
    page.title = "Real-Time Camera Feed"
    cam_image = ft.Image(width=640, height=480,)

    main_content = ft.Container(
        content=cam_image,
        alignment=ft.alignment.center,
        expand=True,)
#button declaration
    reaction_button=ft.ElevatedButton(text="Home",on_click=Reaction_page,style=ft.ButtonStyle( bgcolor="#BF5D17" ,color=ft.colors.WHITE))
    levels_button=ft.ElevatedButton(text="Donate",on_click=Levels_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))
    inyection_button=ft.ElevatedButton(text="About",on_click=inyection_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))
    Co_levels_button=ft.ElevatedButton(text="About",on_click=co_levels_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))

# the two button rows 
    button_row_1 = ft.Row(
        controls=[
            
            inyection_button,
            Co_levels_button,
           
        ],spacing=10,
        alignment=ft.MainAxisAlignment.CENTER )
    
    button_row_2 = ft.Row(
        controls=[
            
            reaction_button,
            levels_button,
           
        ],spacing=10,
        alignment=ft.MainAxisAlignment.CENTER )
    
    #here is the column for the button and text in the top
    navigation=ft.Column(
        controls=[
            ft.Text("BIOBLAST"),
            ft.Text("Plastic Degradation"),

            button_row_1,button_row_2
        ],alignment=ft.MainAxisAlignment.CENTER
    )

        #levels dectetor

        _=ft.Container()
        _=ft.Container()
        _=ft.Container()
        _=ft.Container()






    page.add(navigation,main_content)

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
