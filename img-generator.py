from PIL import Image
import hashlib
from random import randint

# Generate a random color 1 pixel image.
# Given nothing generate an image that is stored in an images folder within this parent folder

def generate_random_1px_image():
    color = pick_random_color()
    hexval = generate_hex_str(color)
    name = generate_name(color)
    generate_1px_image(hexval, "images/" + name)


# Generate a 1 pixel image with a specified hex color
# Given a hex_color and a file name generate a 1 pixel image and store the image in the specified filename
# generate_1px_image("#000000", img_02d74341075fdbda814e5f46c66c9a7d.png) -> image with the file name

def generate_1px_image(hex_color, filename="color_pixel.png"):
    img = Image.new("RGB", (1, 1), hex_color)
    img.save(filename)

# Generate Random RGB Color dictionary
# Given none return a dictionary with integer values for "r", "g", "b" that are between 0 and 255
# pick_random_color() -> {"r": 0, "g": 0, "b": 0}

def pick_random_color():
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    return {"r": r, "g": g, "b": b}

# Genrate a Hex String given a color dictionary
# given a color dictionary containing integer rgb values provide a hex string back with # sign at the front
# generate_hex_str({"r": 0, "g": 0, "b", 0}) -> #000000

def generate_hex_str(color):
    rstr = '{:02x}'.format(color['r'])
    gstr = '{:02x}'.format(color['g'])
    bstr = '{:02x}'.format(color['b'])
    hexval = "#" + rstr + gstr + bstr
    return hexval

# Generate a replicatable name that isn't associated with the hex code color
# Given a color dictionary with integer values for "r", "g", "b" that are between 0 and 255
# return a name that is hashed and duplicatable
# generate_name({"r": 0, "g": 0, "b":0 }) -> img_02d74341075fdbda814e5f46c66c9a7d.png

def generate_name(color):
    s = "r"+str(color['r'])+"g"+ str(color['g']) +"b"+ str(color['b'])
    e = s.encode('utf-8')
    h = hashlib.md5(e).hexdigest()
    return "img_" + h + ".png"

generate_random_1px_image()
