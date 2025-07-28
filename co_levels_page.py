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

def main(page: ft.Page):
     
    def Reaction_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Reaction_page.py")
        subprocess.Popen(["python3",script_path])
        page.window.close()

    def Levels_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Levels_page.py")
        subprocess.Popen(["python3",script_path])
        page.window.close()
        
    def inyection_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Inyection_page.py")
        subprocess.Popen(["python3",script_path])
        page.window.close()

    def co_levels_page(e):
        # script_path=os.path.join(os.path.dirname(__file__),"co_levels_page.py")
        # subprocess.Popen(["python3",script_path])
        # page.window.close()
        return

#button declaration
    reaction_button=ft.ElevatedButton(text="Reaction",on_click=Reaction_page,style=ft.ButtonStyle( bgcolor="#BF5D17" ,color=ft.colors.WHITE))
    levels_button=ft.ElevatedButton(text="Levels",on_click=Levels_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))
    inyection_button=ft.ElevatedButton(text="Inyection",on_click=inyection_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))
    Co_levels_button=ft.ElevatedButton(text="Co2 levels",on_click=co_levels_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))

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
    page.add(navigation)

ft.app(target=main)