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

#this function is for the color changes in the status of quimics
def status(FSG_color=ft.colors,MPG_color=ft.colors,HAG_color=ft.colors,HPG_color=ft.colors):
    FS=False
    MP=False
    HA=False
    HP=False

    if FS==True:
        FSG_color=ft.colors.BLUE
    else:
        FSG_color=ft.colors.ORANGE
    if MP==True:
        MPG_color=ft.colors.BLUE
    else:
        MPG_color=ft.colors.ORANGE
    if HA==True:
        HAG_color=ft.colors.BLUE
    else:
        HAG_color=ft.colors.ORANGE
    if HP==True:
        HPG_color=ft.colors.BLUE
    else:
        HPG_color=ft.colors.ORANGE

        return FSG_color,MPG_color,HAG_color,HPG_color
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

    
    Ferrous_Sulfate_grafic=ft.Container(width=100,
            height=100,
            bgcolor=status([0]),  # Circle fill color
            border=ft.border.all(width=2, color=ft.colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            content=ft.Text("Ferrous Sulfate"),
            alignment=ft.alignment.center)

    Macroplastic_grafic=ft.Container(width=100,
            height=100,
            bgcolor=status([1]),  # Circle fill color
            border=ft.border.all(width=2, color=ft.colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            content=ft.Text("Macroplastic"),
            alignment=ft.alignment.center)
    
    Hydrochloric_Acid_grafic=ft.Container(width=100,
            height=100,
            bgcolor=status([2]),  # Circle fill color
            border=ft.border.all(width=2, color=ft.colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            content=ft.Text("Hydrochloric_Acid"),
            alignment=ft.alignment.center)
    
    Hydrogen_Peroxide_grafic=ft.Container(width=100,
            height=100,
            bgcolor=status([4]),  # Circle fill color
            border=ft.border.all(width=2, color=ft.colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            content=ft.Text("Hydrogen_Peroxide"),
            alignment=ft.alignment.center)

        # ft.Icon(name=ft.Icons.STAR, color=ft.Colors.ORANGE,size=30), 
        # ft.Icon(name=ft.Icons.STAR, color=ft.Colors.BLUE, size=30),

    grafics_row=ft.Row(
        controls=[Ferrous_Sulfate_grafic,Macroplastic_grafic,Hydrochloric_Acid_grafic,Hydrogen_Peroxide_grafic],alignment=ft.alignment.center
    )
    levels=ft.Column(controls=[grafics_row,],alignment=ft.alignment.center
        )

    page.add(navigation,main_content,levels)

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
