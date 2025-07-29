import flet as ft
import os
import subprocess
import asyncio
import random


async def read_sensor():
    await asyncio.sleep(0.1)
    return random.randint(400, 1000)  # Replace with actual sensor reading


async def main(page: ft.Page):
    page.title = "BioBlast CO₂ Dashboard"
    page.scroll = "auto"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Ensure page content is centered

    # Chart with number grid
    line_chart = ft.LineChart(
        data_series=[
            ft.LineChartData(
                data_points=[],
                color=ft.Colors.RED,
                stroke_width=2,
                curved=True,
            )
        ],
        min_y=300,
        max_y=1500,
        min_x=0,  # Set X-axis range to 40 seconds (20 points × 2 seconds)
        max_x=40,
        width=600,
        height=300,
        visible=True,
        # Configure horizontal grid lines (Y-axis)
        horizontal_grid_lines=ft.ChartGridLines(
            interval=200,  # Interval between horizontal grid lines (200 ppm)
            color=ft.Colors.with_opacity(0.2, ft.Colors.ON_SURFACE),
            width=1,
        ),
        # Configure vertical grid lines (X-axis)
        vertical_grid_lines=ft.ChartGridLines(
            interval=10,  # Interval every 10 seconds
            color=ft.Colors.with_opacity(0.2, ft.Colors.ON_SURFACE),
            width=1,
        ),
        # Y-axis (left) with numerical labels
        left_axis=ft.ChartAxis(
            labels_interval=200,  # Labels every 200 ppm
            show_labels=True,
            labels_size=40,
            title=ft.Text("CO₂ (ppm)", size=16),
        ),
        # X-axis (bottom) with numerical labels
        bottom_axis=ft.ChartAxis(
            labels_interval=10,  # Labels every 10 seconds
            show_labels=True,
            labels_size=40,
            title=ft.Text("Time (s)", size=16),
        ),
    )

    # Wrap chart in a Container for centering
    chart_container = ft.Container(
        content=line_chart,
        alignment=ft.alignment.center,  # Center the chart
        padding=10,
    )

    chart_title = ft.Text("CO₂ Levels (ppm)", size=24, visible=True)

    async def update_chart():
        x = 0  # Time in seconds
        while True:
            co2_value = await read_sensor()
            print(f"CO₂: {co2_value} ppm")

            line_chart.data_series[0].data_points.append(
                ft.LineChartDataPoint(x=x, y=co2_value)
            )
            x += 2  # Increment by 2 seconds per update

            if len(line_chart.data_series[0].data_points) > 20:
                line_chart.data_series[0].data_points.pop(0)
                # Shift X-axis to keep a 40-second window
                for point in line_chart.data_series[0].data_points:
                    point.x -= 2

            line_chart.update()
            await asyncio.sleep(2)

    asyncio.create_task(update_chart())

    def open_script(filename):
        script_path = os.path.join(os.path.dirname(__file__), filename)
        subprocess.Popen(["python", script_path])
        page.window.close()

    def Reaction_page(e):
        open_script("Reaction_page.py")

    def Levels_page(e):
        open_script("Levels_page.py")

    def Inyection_page(e):
        open_script("Inyection_page.py")

    def co_levels_page(e):
        page.update()

    # Buttons with consistent styling
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
        on_click=Inyection_page,
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

    # Layout
    navigation = ft.Column(
        controls=[
            ft.Text("BIOBLAST", size=30, weight="bold"),
            ft.Text("Plastic Degradation", size=20),
            ft.Row([inyection_button, co_levels_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([reaction_button, levels_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            chart_title,
            chart_container,  # Use centered container with chart
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center column contents
    )

    page.add(navigation)


ft.app(target=main)