from utils.utils import take_brush
from utils.utils import apply_toothpaste
from utils.utils import brush_teeth
from utils.utils import wash_the_toothbrush
from utils.utils import wash_mouth

from utils.utils import prepare_ingredients
from utils.utils import add_coffee
from utils.utils import add_water
from utils.utils import add_sugar
from utils.utils import drink

def do_brush_teeth():
    take_brush()
    apply_toothpaste()
    brush_teeth()
    wash_the_toothbrush()
    wash_mouth()

def make_coffee():
    prepare_ingredients()
    add_coffee()
    add_water()
    add_sugar()
    drink()

def start_day():
    print("Сперва почистить зубы следуя этим шагам: ")
    do_brush_teeth()
    print("\n Сделать кофе следуя этим шагам: ")
    make_coffee()
start_day()