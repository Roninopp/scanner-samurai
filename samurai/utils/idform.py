#createform(str(case), str(target_id), target_name, bancode, user_name, reason, enforcement, current_time, pfp="TRUE")
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os


def reasonlimit(reason):
    listr = reason.split(" ")
    limit1 = 23
    result1 = listr[0]
    teststr = listr[0]
    result2 = ""
    count = 1
    while limit1 <= 23:
        teststr = teststr + " " + listr[count]
        if len(teststr) > 23:
            limit1 = 24
        else:
            result1 = result1 + " " + listr[count]
            count = count + 1
            limit1 = len(result1)
    
    result2 = reason.partition(result1)[2]
    
    return result1, result2


def createform(userid, name, bancode, enforcer, reason, pfp=None):
    try:
        id_template = Image.open("idcard.jpg")
    except:
        return False
    
    draw = ImageDraw.Draw(id_template)
    color = "rgb(200, 106, 155)"

    font2 = ImageFont.truetype("font2.ttf", size=70)
    font3 = ImageFont.truetype("font2.ttf", size=40)
    
    draw.text(
        (410, 290),
        userid,
        fill=color,
        font=font2
    )
    draw.text(
        (410, 388),
        name,
        fill=color,
        font=font2
    )
    draw.text(
        (430, 488),
        bancode,
        fill=color,
        font=font2
    )
    draw.text(
        (420, 590),
        enforcer,
        fill=color,
        font=font2
    )
    if len(reason) > 24:
        str1, str2 = reasonlimit(reason)
        draw.text(
            (390, 695),
            str1,
            fill=color,
            font=font3
        )
        draw.text(
            (100, 780),
            str2,
            fill=color,
            font=font3
        )
    else:
        draw.text(
            (390, 695),
            reason,
            fill=color,
            font=font3
        )

    id_template.save("user_form.png")

    if pfp == None:
        return True
    
    try:
        user_image = Image.open("user_pfp.jpg")
    except:
        return False

    user_image = user_image.resize((1380, 1380), Image.LANCZOS)
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

    id_template.paste(user_image, (1220, 200), mask)
    id_template.save("user_form.png")
    os.remove("user_pfp.png")
    return True