from vpython import *

animation = canvas(width=800, height=800)
animation.caption_anchor = 'bottom'


current_object = 'no_mask'


def M(m):
    global current_object

    val = m.selected
    if val == "No Mask":
        current_object = "no_mask"

    elif val == "Medical Mask":
        current_object = "medical_mask"

    elif val == "N95 Mask":
        current_object = "N95_mask"


menu(choices=['No Mask', 'Medical Mask', 'N95 Mask'], index=0, bind=M)


while True:
    rate(100)
