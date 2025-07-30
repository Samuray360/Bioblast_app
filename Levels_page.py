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

#this function is for the color changes in the status of quimics
def status(fs=False, mp=False, ha=False, hp=False):
    # Return colors based on boolean conditions
    fsg_color = ft.Colors.BLUE if fs else ft.Colors.ORANGE
    mpg_color = ft.Colors.BLUE if mp else ft.Colors.ORANGE
    hag_color = ft.Colors.BLUE if ha else ft.Colors.ORANGE
    hpg_color = ft.Colors.BLUE if hp else ft.Colors.ORANGE
    return fsg_color, mpg_color, hag_color, hpg_color
    
def main(page: ft.Page):
    def Reaction_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Reaction_page.py")
        subprocess.Popen(["python",script_path])
        page.window.close()

    def Levels_page(e):
        # script_path=os.path.join(os.path.dirname(__file__),"Levels_page.py")
        # subprocess.Popen(["python",script_path])
        # page.window.close()
        return
        
    def inyection_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Inyection_page.py")
        subprocess.Popen(["python",script_path])
        page.window.close()

    def co_levels_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"co_levels_page.py")
        subprocess.Popen(["python",script_path])
        page.window.close()

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
            ft.Text("Levels", size=20, weight="bold")
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center column contents
    )
    
    fs_status, mp_status, ha_status, hp_status = False, False, False, False  # Example conditions
    fsg_color, mpg_color, hag_color, hpg_color = status(fs_status, mp_status, ha_status, hp_status)
    

    Ferrous_Sulfate_grafic=ft.Container(
            width=100,
            height=100,
            bgcolor=fsg_color,  # Circle fill color
            border=ft.border.all(width=2, color=ft.Colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            
            )

    Macroplastic_grafic=ft.Container(
            width=100,
            height=100,
            bgcolor=mpg_color,  # Circle fill color
            border=ft.border.all(width=2, color=ft.Colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            
            )
    
    Hydrochloric_Acid_grafic=ft.Container(
            width=100,
            height=100,
            bgcolor=hag_color,  # Circle fill color
            border=ft.border.all(width=2, color=ft.Colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            
            )
    
    Hydrogen_Peroxide_grafic=ft.Container(
            width=100,
            height=100,
            bgcolor=hpg_color,  # Circle fill color
            border=ft.border.all(width=2, color=ft.Colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            
            )
    
    # Create Columns with fixed-height text containers to prevent circle movement
    Ferrous_Sulfate_column = ft.Column(
        controls=[
            Ferrous_Sulfate_grafic,
            ft.Container(
                content=ft.Text("Ferrous Sulfate", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                height=50,  # Fixed height for text area
                alignment=ft.alignment.center
            )
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    Macroplastic_column = ft.Column(
        controls=[
            Macroplastic_grafic,
            ft.Container(
                content=ft.Text("Macroplastic", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                height=50,
                alignment=ft.alignment.center
            )
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    Hydrochloric_Acid_column = ft.Column(
        controls=[
            Hydrochloric_Acid_grafic,
            ft.Container(
                content=ft.Text("Hydrochloric\nAcid", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                height=50,
                alignment=ft.alignment.center
            )
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    Hydrogen_Peroxide_column = ft.Column(
        controls=[
            Hydrogen_Peroxide_grafic,
            ft.Container(
                content=ft.Text("Hydrogen\nPeroxide", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                height=50,
                alignment=ft.alignment.center
            )
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    feedBack=ft.Row(
        controls=[
            ft.Icon(name=ft.Icons.STAR, color=ft.Colors.ORANGE,size=30), 
            ft.Text("Good",weight=ft.FontWeight.BOLD),
            ft.Icon(name=ft.Icons.STAR, color=ft.Colors.BLUE, size=30),
            ft.Text("Increase",weight=ft.FontWeight.BOLD)
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )

    circle_row=ft.Row(
        controls=[Ferrous_Sulfate_column,
                  Macroplastic_column,
                  Hydrochloric_Acid_column,
                  Hydrogen_Peroxide_column
                  ],
                spacing=30,
                alignment=ft.MainAxisAlignment.CENTER
    )

    levels=ft.Column(
        controls=[circle_row,feedBack],
        spacing=50,
        alignment=ft.MainAxisAlignment.CENTER
        )

    page.add(navigation,levels)

ft.app(target=main)