import flet as ft 
import os
import subprocess

def get_asset_path(filename):
    return os.path.join(os.path.dirname(__file__),filename)

def main(page: ft.Page):
    page.title = "BioBlast Injection Dashboard"
    page.scroll = "auto"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Ensure page content is centered
    
        # Error message text field to display validation errors
    error_message = ft.Text("", color=ft.Colors.RED, size=14)

    # Function to validate integer input
    def validate_integer(e, text_field):
        value = e.control.value.strip()
        if value == "":
            error_message.value = ""
            page.update()
            return
        try:
            float(value)  # Try converting to integer
            error_message.value = ""  # Clear error if valid
        except ValueError:
            error_message.value = "Please enter a valid integer."
            text_field.value = ""  # Clear invalid input
        page.update()
        
    #the function for the to sent the amount of quimic 
    def inject_ferrous_sulfate(e):
        print(Ferrous_Sulfate.controls[1].content.value)
        return

    def inject_Hydrochloric_Acid(e):
        print(Hydrochloric_Acid.controls[1].content.value)
        return

    def inject_Hydrogen_Peroxide(e):
        print(Hydrogen_Peroxide.controls[1].content.value)
        return
    
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
            ft.Text("Injection", size=20, weight="bold")
          
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center column contents
    )
    
    Ferrous_Sulfate=ft.Row(controls=[
    ft.Container(ft.Text("Ferrous Sulfate",size=20,weight=ft.FontWeight.BOLD),bgcolor=ft.Colors.BLUE,width=250,padding=10),
    
    ft.Container(ft.TextField("", keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: validate_integer(e, Ferrous_Sulfate.controls[1].content)),
                 border=ft.border.all(width=2, color=ft.Colors.WHITE)),
    ft.Container(
        ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.WHITE,size=30),
        bgcolor=ft.Colors.ORANGE,
        border_radius=50,
        on_click=inject_ferrous_sulfate,)
    
    ],alignment=ft.MainAxisAlignment.CENTER)

    Hydrochloric_Acid=ft.Row(controls=[
        
    ft.Container(ft.Text("Hydrochloric Acid",size=20,weight=ft.FontWeight.BOLD),bgcolor=ft.Colors.BLUE,width=250,padding=10),
    
    ft.Container(ft.TextField("", keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: validate_integer(e, Hydrochloric_Acid.controls[1].content)), 
                 border=ft.border.all(width=2, color=ft.Colors.WHITE)),
    ft.Container(
        ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.WHITE,size=30),
        bgcolor=ft.Colors.ORANGE,
        border_radius=50,
        on_click=inject_Hydrochloric_Acid,
    )
    
    ],alignment=ft.MainAxisAlignment.CENTER)

    Hydrogen_Peroxide=ft.Row(controls=[
    ft.Container(ft.Text("Hydrogen Peroxide",size=20,weight=ft.FontWeight.BOLD),bgcolor=ft.Colors.BLUE,width=250,padding=10),
    
    ft.Container(ft.TextField("", keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: validate_integer(e, Hydrogen_Peroxide.controls[1].content)), 
                 border=ft.border.all(width=2, color=ft.Colors.WHITE)),
    ft.Container(
        ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.WHITE,size=30),
        bgcolor=ft.Colors.ORANGE,
        border_radius=50,
        on_click=inject_Hydrogen_Peroxide,
    )
    ],alignment=ft.MainAxisAlignment.CENTER)


    inyection_controls=ft.Column(
        controls=[Ferrous_Sulfate,Hydrochloric_Acid,Hydrogen_Peroxide],horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    warning_icon=ft.Stack([
        
        ft.Icon(name=ft.Icons.WARNING, color=ft.Colors.RED,size=60),
        ft.Icon(name=ft.Icons.WARNING_AMBER, color=ft.Colors.WHITE,size=60),
        
        ])

    feedback=ft.Row(controls=[
        warning_icon,
        ft.Text("RECOMENDED: \n• 15 mL of 3% hydrogen peroxide(diluted in water)\n• 0.27g of iron (II) sulfate heptahydrate\n•5drops of hydrochloric acid"),
        error_message
        ],alignment=ft.MainAxisAlignment.CENTER)

    page.add(navigation,inyection_controls,feedback)

ft.app(target=main)