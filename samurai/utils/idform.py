#createform(str(case), str(target_id), target_name, bancode, user_name, reason, enforcement, current_time, pfp="TRUE")
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

def createform(name, pfp=None):
    try:
        id_template = Image.open("idcard.png")
    except:
        return False
    
    draw = ImageDraw.Draw(id_template)
    color = "rgb(200, 106, 155)"

    #font1 = ImageFont.truetype("DezertDemoOutline.ttf", size=80)
    font2 = ImageFont.truetype("font2.ttf", size=70)

    draw.text(
        (200, 310),
        name,
        fill=color,
        font=font2
    )
    id_template.save("user_form.png")

    if pfp == None:
        return True
    
    try:
        user_image = Image.open("user_pfp.jpg")
    except:
        return False

    user_image = user_image.resize((640, 640), Image.LANCZOS)
    mask = Image.new("L", user_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + user_image.size, fill=255)
    pfp_image = ImageOps.fit(user_image, mask.size, centering=(0.5, 0.5))
    pfp_image.putalpha(mask)

    width, height = pfp_image.size
    new_width = int(width * 0.4)
    new_height = int(height * 0.4)
    pfp_image = pfp_image.resize((new_width, new_height))
    pfp_image.save("user_pfp.png")
    os.remove("user_pfp.jpg")

    user_image = Image.open("user_pfp.png")
    mask = Image.new("L", user_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + user_image.size, fill=255)

    id_template.paste(user_image, (220, 50), mask)
    id_template.save("user_form.png")
    os.remove("user_pfp.png")
    return True