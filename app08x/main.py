import flet as ft


def main(page: ft.Page):
#Establecer tamaño de pantalla
    page.window_width=800
    page.window_height=800

    page.bgcolor="black"
    page.title="Mictlan"
    page.fgcolor="gray"
    
    
    #Audios
    Intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    
    PrimerNivel=ft.Audio(src"Primer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel1)
    
    SegundoNivel=ft.Audio(src="Segundo_Nivel.mp3",volumen=1,balance=0)
    page.overlay.append(Nivel2)
    
    TercerNivel=ft.Audio(src"Terser_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel3)
    
    CuartoNivel=ft.Audio(src"Cuarto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel4)
    
    QuintoNivel=ft.Audio(src"Quinto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel5)
    
    SextoNivel=ft.Audio(src"Sexto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel6)
    
    SeptimoNivel=ft.Audio(src"septimo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel7)
    
    OctavoNivel=ft.Audio(src"Octavo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel8)
    
    NovenoNivel=ft.Audio(src"Noveno_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel9)
    
    #Creamos la interfaz
    
    btnIntro=ft.FilledButton(text="Escucha el intro",disabled=False)
    
    bntNivel1=ft.ElevetadButton(text="PrimerNivel")
    img1=ft.Image(src="Primer-Nivel.jpeg")
    
    bntNivel2=ft.ElevetadButton(text="segundoNivel")
    img1=ft.Image(src="Segundo-Nivel.jpeg")
    
    btnNivel3=ft.ElevetadButton(text="TercerNivel")
    img3=ft.Image(src="Tercer-Nivel.jpeg")

    bntNivel4=ft.ElevetadButton(text="CuartoNivel")
    img4=ft.Image(src="Cuarto-Nivel.jpeg")
    
    bntNivel5=ft.ElevetadButton(text="QuintoNivel")
    img5=ft.Image(src="Quinto-Nivel.jpeg")
    
    bntNivel6=ft.ElevetadButton(text="sextoNivel")
    img6=ft.Image(src="Sexto-Nivel.jpeg")
    
    bntNivel7=ft.ElevetadButton(text="SeptimoNivel")
    img7=ft.Image(src="Septimo-Nivel.jpeg")
    
    bntNivel8=ft.ElevetadButton(text="OctavoNivel")
    img8=ft.Image(src="Octavo-Nivel.jpeg")

    bntNivel9=ft.ElevetadButton(text="NovenoNivel")
    img9=ft.Image(src="Noveno-Nivel.jpeg")
    page.add(
        ft.Row(
            alignment"start",
            controls=[btnIntro]
        ),
        ft.Column(
            alignment="CENTER",
            spacing=10
            scroll=ft.ScrolMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=()
                )
            ]
        )
    )
    




ft.app(main)
