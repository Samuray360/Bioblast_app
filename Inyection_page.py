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
        subprocess.Popen(["python",script_path])
        page.window.close()

    def Levels_page(e):
        script_path=os.path.join(os.path.dirname(__file__),"Levels_page.py")
        subprocess.Popen(["python",script_path])
        page.window.close()
        
    def inyection_page(e):
        # script_path=os.path.join(os.path.dirname(__file__),"Inyection_page.py")
        # subprocess.Popen(["python",script_path])
        # page.window.close()
        return

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
    
    Ferrous_Sulfate=ft.Row(controls=[
    ft.Container(bgcolor=ft.colors.BLUE,content=ft.Text("Ferrous Sulfate",size=20)), ft.Container(border=ft.border.all(width=2, color=ft.colors.WHITE),content=
                ft.TextField("")),
    ])

    Hydrochloric_Acid=ft.Row(controls=[
    ft.Container(bgcolor=ft.colors.BLUE,content=ft.Text("Hydrochloric_Acid",size=20)),ft.Container(border=ft.border.all(width=2, color=ft.colors.WHITE),content=
                ft.TextField("")),
    ])

    Hydrogen_Peroxide=ft.Row(controls=[
    ft.Container(bgcolor=ft.colors.BLUE,content=ft.Text("Hydrogen_Peroxide",size=20)),ft.Container(border=ft.border.all(width=2, color=ft.colors.WHITE),content=
                ft.TextField(""))
    ])


    Ferrous_Sulfate.controls[1].content.value
    Hydrochloric_Acid.controls[1].content.value
    Hydrogen_Peroxide.controls[1].content.value

    inyection_controls=ft.Column(
        controls=[Ferrous_Sulfate,Hydrochloric_Acid,Hydrogen_Peroxide],horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    warning_icon=ft.Stack([
        
        ft.Icon(name=ft.Icons.WARNING, color=ft.Colors.RED,size=60),
        ft.Icon(name=ft.Icons.WARNING_AMBER, color=ft.Colors.WHITE,size=60),
        
        ])

    feedback=ft.Row(controls=[
        warning_icon,
        ft.Text("RECOMENDED: \n• 15 mL of 3% hydrogen peroxide(diluted in water)\n• 0.27g of iron (II) sulfate heptahydrate\n•5drops of hydrochloric acid")
        ])

    page.add(navigation,inyection_controls,feedback)

ft.app(target=main)