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

# text: str
    # Povinny parametr
    # Vytvoření textu
        #text = Text("Hello world!")
    # Přidání textu do scény
        #self.add(text)

# fill_opacity: float = 1
    # Vytvoření textu s plnou výplní (fill_opacity=1)
        #opaque_text = Text("Defaultní, plně neprůhledný text")
    # Vytvoření textu s částečnou průhledností
        #transparent_text = Text("Částečně průhledný text", fill_opacity=0.5)
        #more_transparent_text = Text("Hodně průhledný text", fill_opacity=0.2)
    # Umístění textů
        #opaque_text.shift(UP * 1.5)
        #more_transparent_text.shift(DOWN * 1.5)
    # Přidání textů do scény
        #self.add(opaque_text, transparent_text,more_transparent_text)

# stroke_width: float = 0
    # Vytvoření textu s různou tloušťkou obrysu
        #no_stroke_text = Text("Bez obrysu", stroke_width=0)
        #thin_stroke_text = Text("Tenký obrys", stroke_width=1)
        #thick_stroke_text = Text("Tlustý obrys", stroke_width=5)
    # Umístění textů
        #no_stroke_text.shift(UP * 1.5)
        #thick_stroke_text.shift(DOWN * 1.5)
    # Přidání textů do scény
        #self.add(no_stroke_text, thin_stroke_text, thick_stroke_text)

# color: ParsableManimColor | None = None
    # Vytvoření textu s různými barvami
        #red_text = Text("Červený text", color = RED)
        #green_text = Text("Zelený text", color = GREEN)
        #blue_text = Text("Modrý text", color = BLUE)
    # Umístění textů
        #red_text.shift(UP * 1.5)
        #blue_text.shift(DOWN * 1.5)
    # Přidání textů do scény
        #self.add(red_text, green_text, blue_text)

# font_size: float = DEFAULT_FONT_SIZE
    # Vytvoření textu s různou velikostí písma
        #small_text = Text("Malý text", font_size = 36)
        #normal_text = Text("Normální text", font_size = 48)
        #large_text = Text("Velký text", font_size = 60)
    # Umístění textů
        #small_text.shift(UP * 1.5)
        #large_text.shift(DOWN * 1.5)
    # Přidání textů do scény
        #self.add(small_text, normal_text, large_text)

# line_spacing: float = -1
    # Vytvoření textu s různým řádkováním
        #single_line_text = Text("Jeden\nřádek", line_spacing = 0)
        #double_line_text = Text("Dva\nřádky", line_spacing = 0.2)
        #triple_line_text = Text("Tři\nřádky", line_spacing = 0.4)
    # Umístění textů
        #single_line_text.shift(UP * 1.5)
        #triple_line_text.shift(DOWN * 1.5)
    # Přidání textů do scény
        #self.add(single_line_text, double_line_text, triple_line_text)

# font: str = "font_name"
    # Vytvoření textu s výchozím fontem
        #default_font_text = Text("Výchozí font")
    # Vytvoření textu s fontem "Comic Sans MS"
        #comic_sans_text = Text("Comic Sans MS", font = "Comic Sans MS")
    # Vytvoření textu s fontem "Arial"
        #arial_text = Text("Arial", font = "Arial")
    # Umístění textů
        #default_font_text.shift(UP * 1.5)
        #arial_text.shift(DOWN * 1.5)
    # Přidání textů do scény
        #self.add(default_font_text, comic_sans_text, arial_text)

# slant: str = NORMAL
    # Pango stuff
    # {NORMAL, ITALIC, OBLIQUE, BOLD}
    # Vytvoření textu s různým sklonem
        #normal_text = Text("Normální sklon textu", slant = NORMAL)
        #italic_text = Text("Italic text", slant = ITALIC)
        #oblique_text = Text("Oblíbený text", slant = OBLIQUE)
    # Umístění textů
        #normal_text.shift(UP * 1.5)
        #oblique_text.shift(DOWN * 1.5)
    # Přidání textů do scény
        #self.add(normal_text, italic_text, oblique_text)

# weight: str = NORMAL
    # Pango stuff
    # {NORMAL, ITALIC, OBLIQUE, BOLD}
    # Only for Pango from below
    # {THIN, ULTRALIGHT, LIGHT, SEMILIGHT, BOOK, MEDIUM, SEMIBOLD, ULTRABOLD, HEAVY, ULTRAHEAVY}
    # Vytvoření textu s rozdilnou tucnosti
        #normal_text = Text("defautní tučnost textu", weight = NORMAL)
        #heavy_text = Text("tučnost textu HEAVY", weight = HEAVY)
        #thin_text = Text("tučnost textu THIN", weight = THIN)
    # Umístění textů
        #thin_text.shift(UP * 1.5)
        #heavy_text.shift(DOWN * 1.5)
    # Přidání textů do scény
        #self.add(normal_text, heavy_text, thin_text)

# t2c: dict[str, str] = None
    # Vytvoření slovníku pro změnu barvy textu
        #text = Text("Text s různými barvami", t2c={"různými": GREEN, "barvami": BLUE})
    # Přidání textu do scény
        #self.add(text)
        #self.wait(2)

# t2f: dict[str, str] = None
    # Vytvoření slovníku pro změnu fontu textu
        #text = Text("Text s různými fonty", t2f={"různými": "Comic Sans MS", "fonty": "Arial"})
    # Přidání textu do scény
        #self.add(text)

# t2g: dict[str, tuple] = None
    # Vytvoření slovníku pro změnu gradientu textu
        #text = Text("Text s gradientem", t2g={"gradientem": (RED, GREEN)})
    # Přidání textu do scény
        #self.add(text)

# t2s: dict[str, str] = None
    # Vytvoření slovníku pro změnu sklonu textu
        #text = Text("Text s různým sklonem", t2s={"různým": ITALIC, "sklonem": OBLIQUE})
    # Přidání textu do scény
        #self.add(text)

# t2w: dict[str, str] = None
    # Vytvoření slovníku pro změnu tučnosti textu
        #text = Text("Text s různou tučností", t2w={"různou": BOLD, "tučností": NORMAL})
    # Přidání textu do scény
        #self.add(text)

# gradient: tuple = None
    # Vytvoření textu s gradientem
        #gradient_text = Text("Gradient dvou barev", gradient = (RED, GREEN))
        #gradient_text_more = Text("Gradient tří barev", gradient = (RED, GREEN, BLUE))
        #gradient_text_more_color = Text("Gradient čtyř barev", gradient = (RED, GREEN, BLUE, PURPLE))
    # Umístění textu
        #gradient_text.shift(UP * 1)
        #gradient_text_more_color.shift(DOWN * 1)
    # Přidání textu do scény
        #self.add(gradient_text, gradient_text_more, gradient_text_more_color)

# tab_width: int = 4
    # Vytvoření textu s tabulátorem
        #text = Text("tabulator = \t default")
        #text_tab_short= Text("tabulator =\t 1", tab_width=1)
        #text_tab_long= Text("tabulator =\t 8", tab_width=8)
    # Umístění textu
        #text_tab_short.shift(UP * 1)
        #text_tab_long.shift(DOWN * 1)
    # Přidání textu do scény
        #self.add(text, text_tab_short, text_tab_long)

# warn_missing_font: bool = True
    # Vytvoření textu s chybějícím fontem
        #text = Text("Text s chybějícím fontem", font="nonexistent_font")
    # Přidání textu do scény
        #self.add(text)

# height: float = None
    # Vytvoření textu s rozdílnou výškou
        #text = Text("defaltní výška")
        #text_taller = Text("vyšší výška textu", height = 1)
        #text_smaller = Text("menší výška textu", height = 0.5)
    # Umístění textu
        #text_smaller.shift(UP * 1)
        #text_taller.shift(DOWN * 1.25)
    # Přidání textu do scény
        #self.add(text, text_taller, text_smaller)

# width: float = None
    # Vytvoření textu s rozdílnou šířkou
        #text = Text("defaltní šířka")
        #text_wider = Text("větší šířka textu", width = 10)
        #text_smaller = Text("menší šířka textu", width = 3)
    # Umístění textu
        #text_smaller.shift(UP * 1)
        #text_wider.shift(DOWN * 1.25)
    # Přidání textu do scény
        #self.add(text, text_wider, text_smaller)

# should_center: bool = True
    # Vytvoření textu s centrováním
        text = Text("Text s centrováním", should_center=False)
    # Přidání textu do scény
        self.add(text)


# disable_ligatures: bool = False
    # Text s povolenými ligaturami (výchozí chování)
        #text_with_ligatures = Text("office", font_size=72)
    # Text s vypnutými ligaturami
        #text_without_ligatures = Text("office", font_size=72, disable_ligatures=True)
    # Umístění textů
        #text_with_ligatures.shift(UP * 2)  # Posun textu nahoru
        #text_without_ligatures.shift(DOWN * 2)  # Posun textu dolů
    # Přidání textů do scény
        #self.add(text_with_ligatures, text_without_ligatures)
        #self.wait(2)