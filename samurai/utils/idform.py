#createform(str(case), str(target_id), target_name, bancode, user_name, reason, enforcement, current_time, pfp="TRUE")
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

def createform(name, pfp=None):
    try:
        id_template = Image.open("idcard.png")
    except:
        return False
    
    if pfp == None:
        jpg
    
    try:
        user_image = Image.open("user_pfp.png")
    except:
        return False