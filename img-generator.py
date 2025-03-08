from PIL import Image
import hashlib
from random import randint

def generate_1px_image(hex_color, filename="color_pixel.png"):
    # Create a 1x1 image with the specified color
    img = Image.new("RGB", (1, 1), hex_color)
    
    # Save the image
    img.save(filename)
    print(f"1px image saved as {filename} with color {hex_color}")

def generate_random_1px_image():
    color = pick_random_color()
    hexval = generate_hex_str(color)
    name = generate_name(color)
    generate_1px_image(hexval, "images/" + name)

def pick_random_color():
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    return {"r": r, "g": g, "b": b}

def generate_hex_str(color):
    rstr = '{:02x}'.format(color['r'])
    gstr = '{:02x}'.format(color['g'])
    bstr = '{:02x}'.format(color['b'])
    hexval = "#" + rstr + gstr + bstr
    return hexval




def generate_all_colors():
    for i in range(0, 256):
        for k in range(0,256):
            for l in range(0, 256):
                name = generate_name(i,k,l)
                rstr = '{:02x}'.format(i)
                gstr = '{:02x}'.format(k)
                bstr = '{:02x}'.format(l)
                hexval = "#" + rstr + gstr + bstr
                #generate_1px_image(hexval, "images/" + name + ".png")

# generate_name(color(dict)) -> str
def generate_name(color):
    s = "r"+str(color['r'])+"g"+ str(color['g']) +"b"+ str(color['b'])
    e = s.encode('utf-8')
    h = hashlib.md5(e).hexdigest()
    return "img_" + h + ".png"
# Example usage
#generate_1px_image("#FF5733")  # Generates a 1px image with an orange color
#generate_all_colors()
generate_random_1px_image()
