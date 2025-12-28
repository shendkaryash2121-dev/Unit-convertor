from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# ---------------- UI COLORS ----------------
Window.clearcolor = (0.96, 0.97, 0.98, 1)
PRIMARY = (0.12, 0.38, 0.85, 1)
TEXT_GRAY = (0.4, 0.4, 0.4, 1)

# ---------------- BIO FORMULAS ----------------

# Mass
def mass_convert(value, from_u, to_u):
    units = {"kg": 1000, "g": 1, "mg": 0.001, "oz": 28.35}
    return (value * units[from_u]) / units[to_u]

# Volume
def volume_convert(value, from_u, to_u):
    units = {"L": 1000, "mL": 1, "µL": 0.001}
    return (value * units[from_u]) / units[to_u]

# Dilution C1V1 = C2V2
def dilution(c1, v1, c2):
    return (c1 * v1) / c2

# Protein concentration
def protein_concentration(a280):
    return a280 * 1.5

# Percentage solutions
def percent_wv(grams, volume):
    return (grams / volume) * 100

def percent_vv(solute, solution):
    return (solute / solution) * 100

def percent_mv(mass, volume):
    return (mass / volume) * 100

# ---------------- CARD ----------------
class Card(BoxLayout):
    def __init__(self, title, subtitle, action, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 5
        self.size_hint_y = None
        self.height = 140

        with self.canvas.before:
            Color(1,1,1,1)
            self.bg = RoundedRectangle(radius=[20])
        self.bind(pos=self.update_bg, size=self.update_bg)

        self.add_widget(Label(text=title, bold=True))
        self.add_widget(Label(text=subtitle, font_size=12, color=TEXT_GRAY))

        btn = Button(text="Open", size_hint_y=None, height=40,
                     background_color=PRIMARY)
        btn.bind(on_press=action)
        self.add_widget(btn)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

# ---------------- HOME SCREEN ----------------
class Home(BoxLayout):
    def __init__(self, switch, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15

        self.add_widget(Label(text="Biocal", font_size=26, bold=True))
        self.add_widget(Label(text="Biotechnology Lab Calculator", color=TEXT_GRAY))

        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=15, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        grid.add_widget(Card("Mass", "kg g mg oz",
                             lambda x: switch("mass")))
        grid.add_widget(Card("Volume", "L mL µL",
                             lambda x: switch("volume")))
        grid.add_widget(Card("Dilution", "C₁V₁=C₂V₂",
                             lambda x: switch("dilution")))
        grid.add_widget(Card("Protein", "A280 × 1.5",
                             lambda x: switch("protein")))
        grid.add_widget(Card("Percentage", "w/v v/v m/v",
                             lambda x: switch("percent")))

        scroll.add_widget(grid)
        self.add_widget(scroll)

# ---------------- MASS SCREEN ----------------
class MassScreen(BoxLayout):
    def __init__(self, switch, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        self.val = TextInput(hint_text="Value", input_filter="float")
        self.f = Spinner(values=["kg","g","mg","oz"], text="g")
        self.t = Spinner(values=["kg","g","mg","oz"], text="kg")
        self.out = TextInput(readonly=True, hint_text="Result")

        btn = Button(text="Convert", background_color=PRIMARY)
        btn.bind(on_press=self.calc)

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: switch("home"))

        for w in [self.val, self.f, self.t, btn, self.out, back]:
            self.add_widget(w)

    def calc(self, x):
        try:
            self.out.text = str(
                mass_convert(float(self.val.text), self.f.text, self.t.text)
            )
        except:
            self.out.text = "Error"

# ---------------- VOLUME SCREEN ----------------
class VolumeScreen(MassScreen):
    def calc(self, x):
        try:
            self.out.text = str(
                volume_convert(float(self.val.text), self.f.text, self.t.text)
            )
        except:
            self.out.text = "Error"

# ---------------- DILUTION ----------------
class DilutionScreen(BoxLayout):
    def __init__(self, switch, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        self.padding=20
        self.spacing=10

        self.c1 = TextInput(hint_text="C1")
        self.v1 = TextInput(hint_text="V1")
        self.c2 = TextInput(hint_text="C2")
        self.out = TextInput(readonly=True)

        btn = Button(text="Calculate V2", background_color=PRIMARY)
        btn.bind(on_press=self.calc)

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: switch("home"))

        for w in [self.c1,self.v1,self.c2,btn,self.out,back]:
            self.add_widget(w)

    def calc(self,x):
        try:
            self.out.text=str(
                dilution(float(self.c1.text),
                         float(self.v1.text),
                         float(self.c2.text))
            )
        except:
            self.out.text="Error"

# ---------------- PROTEIN ----------------
class ProteinScreen(BoxLayout):
    def __init__(self, switch, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        self.padding=20

        self.a = TextInput(hint_text="Absorbance A280")
        self.out = TextInput(readonly=True)

        btn = Button(text="Calculate", background_color=PRIMARY)
        btn.bind(on_press=self.calc)

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: switch("home"))

        self.add_widget(self.a)
        self.add_widget(btn)
        self.add_widget(self.out)
        self.add_widget(back)

    def calc(self,x):
        try:
            self.out.text=str(protein_concentration(float(self.a.text)))+" mg/mL"
        except:
            self.out.text="Error"

# ---------------- PERCENT ----------------
class PercentScreen(BoxLayout):
    def __init__(self, switch, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        self.padding=20

        self.a = TextInput(hint_text="Mass/Volume")
        self.b = TextInput(hint_text="Total Volume")
        self.out = TextInput(readonly=True)

        btn = Button(text="%(w/v)", background_color=PRIMARY)
        btn.bind(on_press=self.calc)

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: switch("home"))

        self.add_widget(self.a)
        self.add_widget(self.b)
        self.add_widget(btn)
        self.add_widget(self.out)
        self.add_widget(back)

    def calc(self,x):
        try:
            self.out.text=str(
                percent_wv(float(self.a.text), float(self.b.text))
            )+" %"
        except:
            self.out.text="Error"

# ---------------- MAIN APP ----------------
class BiocalApp(App):
    def build(self):
        self.root = BoxLayout()
        self.screens = {
            "home": Home(self.switch),
            "mass": MassScreen(self.switch),
            "volume": VolumeScreen(self.switch),
            "dilution": DilutionScreen(self.switch),
            "protein": ProteinScreen(self.switch),
            "percent": PercentScreen(self.switch),
        }
        self.root.add_widget(self.screens["home"])
        return self.root

    def switch(self, name):
        self.root.clear_widgets()
        self.root.add_widget(self.screens[name])

if __name__ == "__main__":
    BiocalApp().run()
