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
    reaction_button=ft.Container(ft.Text("Reaction",color=ft.colors.WHITE),on_click=Reaction_page,bgcolor="#BF5D17",width=200)
    levels_button=ft.Container(ft.Text("Levels",color=ft.colors.WHITE),on_click=Levels_page,bgcolor="#BF5D17",width=200)
    inyection_button=ft.Container(ft.Text("Inyection",color=ft.colors.WHITE),on_click=inyection_page,bgcolor="#BF5D17",width=200)
    Co_levels_button=ft.Container(ft.Text("Co2 Levels",color=ft.colors.WHITE),on_click=co_levels_page,bgcolor="#BF5D17",width=200)
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
            
            )

    Macroplastic_grafic=ft.Container(width=100,
            height=100,
            bgcolor=status([1]),  # Circle fill color
            border=ft.border.all(width=2, color=ft.colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            
            )
    
    Hydrochloric_Acid_grafic=ft.Container(width=100,
            height=100,
            bgcolor=status([2]),  # Circle fill color
            border=ft.border.all(width=2, color=ft.colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            
            )
    
    Hydrogen_Peroxide_grafic=ft.Container(width=100,
            height=100,
            bgcolor=status([4]),  # Circle fill color
            border=ft.border.all(width=2, color=ft.colors.WHITE),  # Border: 2px wide, black
            border_radius=50,  # Half of width/height for a perfect circle
            
            )
    Ferrous_Sulfate_column=ft.Column(controls=(Ferrous_Sulfate_grafic,ft.Text("Ferrous Sulfate")))
    Macroplastic_column=ft.Column(controls=(Ferrous_Sulfate_grafic,ft.Text("Macroplastic"),))
    Hydrochloric_Acid_column=ft.Column(controls=(Ferrous_Sulfate_grafic,ft.Text("Hydrochloric_Acid")))
    Hydrogen_Peroxide_column=ft.Column(controls=(Ferrous_Sulfate_grafic,ft.Text("Hydrogen_Peroxide")))
    
    feedBack=ft.Row(controls=[
        ft.Icon(name=ft.Icons.STAR, color=ft.Colors.ORANGE,size=30), 
        ft.Text("Good"),
        ft.Icon(name=ft.Icons.STAR, color=ft.Colors.BLUE, size=30),
        ft.Text("Increase")
        ],alignment=ft.MainAxisAlignment.CENTER)

    column_row=ft.Row(
        controls=[Ferrous_Sulfate_column,Macroplastic_column,Hydrochloric_Acid_column,Hydrogen_Peroxide_column],spacing=10,alignment=ft.alignment.center
    )

    levels=ft.Column(controls=[column_row,feedBack],alignment=ft.alignment.center
        )

    page.add(navigation,levels)

ft.app(target=main)