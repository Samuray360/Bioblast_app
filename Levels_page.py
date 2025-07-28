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
def main(page: ft.Page):
    def Reaction_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Reaction_page.py")
        subprocess.Popen(["python3",script_path])
        page.window.close()

    def Levels_page(e):
        # script_path=os.path.join(os.path.dirname(__file__),"Levels_page.py")
        # subprocess.Popen(["python3",script_path])
        # page.window.close()
        return
        
    def inyection_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Inyection_page.py")
        subprocess.Popen(["python3",script_path])
        page.window.close()

    def co_levels_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"co_levels_page.py")
        subprocess.Popen(["python3",script_path])
        page.window.close()

#button declaration
    reaction_button=ft.ElevatedButton(text="Reaction",on_click=Reaction_page,style=ft.ButtonStyle( bgcolor="#BF5D17" ,color=ft.colors.WHITE))
    levels_button=ft.ElevatedButton(text="Levels",on_click=Levels_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))
    inyection_button=ft.ElevatedButton(text="Inyection",on_click=inyection_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))
    Co_levels_button=ft.ElevatedButton(text="Co2 Levels",on_click=co_levels_page,style=ft.ButtonStyle (bgcolor="#BF5D17",color=ft.colors.WHITE))

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

    page.add(navigation,levels)

ft.app(target=main)