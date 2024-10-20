from manim import *

class GridScene(Scene):
    def construct(self):
    # Nastavení defaut gridu s osami
        grid = NumberPlane(
            x_range=[-7, 7, 1],  # Rozsah pro osu x
            y_range=[-4, 4, 1],  # Rozsah pro osu y
            background_line_style={
                "stroke_color": BLUE_D,  # Barva čar gridu
                "stroke_width": 2,       # Tloušťka čar gridu
                "stroke_opacity": 0.8    # Průhlednost čar
            }
        )
        #self.add(grid)
        #grid.add_coordinates()


# fill_opacity: float = 1
        # Vytvoření textu s plnou výplní (fill_opacity=1)
        opaque_text = Text("Defaultní, plně neprůhledný text(1)", fill_opacity=1)
        # Vytvoření textu s částečnou průhledností
        transparent_text = Text("Částečně průhledný text(0.5)", fill_opacity=0.5)
        more_transparent_text = Text("Hodně průhledný text(0.2)", fill_opacity=0.2)
        # Umístění textů
        opaque_text.shift(UP * 1.5)
        more_transparent_text.shift(DOWN * 1.5)
        # Přidání textů do scény
        #self.add(opaque_text, transparent_text,more_transparent_text)
        #self.wait(2)


# weight: str = NORMAL
    # Pango stuff
    # {NORMAL, ITALIC, OBLIQUE, BOLD}
    # Only for Pango from below
    # {THIN, ULTRALIGHT, LIGHT, SEMILIGHT, BOOK, MEDIUM, SEMIBOLD, ULTRABOLD, HEAVY, ULTRAHEAVY}
        # Vytvoření textu s rozdilnou tucnosti
        normal_text = Text("defautní tučnost textu", weight=NORMAL)
        heavy_text = Text("tučnost textu HEAVY", weight=HEAVY)
        thin_text = Text("tučnost textu THIN", weight=THIN)
        # Umístění textů
        thin_text.shift(UP * 1.5)
        heavy_text.shift(DOWN * 1.5)

        # Přidání textů do scény
        #self.add(normal_text, heavy_text, thin_text)
        #self.wait(2)


# disable_ligatures: bool = False
        # Text s povolenými ligaturami (výchozí chování)
        text_with_ligatures = Text("office", font_size=72)

        # Text s vypnutými ligaturami
        text_without_ligatures = Text("office", font_size=72, disable_ligatures=True)

        # Umístění textů
        text_with_ligatures.shift(UP * 2)  # Posun textu nahoru
        text_without_ligatures.shift(DOWN * 2)  # Posun textu dolů

        # Přidání textů do scény
        #self.add(text_with_ligatures, text_without_ligatures)
        #self.wait(2)


# gradient: tuple = None
        # Vytvoření textu s gradientem
        gradient_text = Text("Gradient texts", gradient=(RED, GREEN))
        gradient_text_more = Text("Gradient textss", gradient=(RED, GREEN, BLUE))
        gradient_text_more_color = Text("Gradient textsss", gradient=(RED, GREEN, BLUE, PURPLE))

        # Umístění textu
        gradient_text.shift(UP * 1)
        gradient_text_more_color.shift(DOWN * 1)
        # Přidání textu do scény
        #self.add(gradient_text, gradient_text_more, gradient_text_more_color)
        #self.wait(2)

# t2c: dict[str, str]
        # Vytvoření slovníku pro změnu barvy textu
        text = Text("Text s různými barvami", t2c={"různými": GREEN, "barvami": BLUE})
        # Přidání textu do scény
        self.add(text)
        self.wait(2)