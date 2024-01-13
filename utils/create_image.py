import os
from .mappings import role_image_dict
from PIL import Image, ImageDraw, ImageFont

from utils import image_dir

font = os.path.abspath(os.path.join('assets', 'fonts'))
pass_font = os.path.join(font, 'passfont.ttf')

base_image = os.path.join(image_dir, 'base.png')


def resolve_stamps(roles: list):
    """
    Get a list of stamps from user roles
    :param roles: list of user roles
    :return: list containing stamps
    """
    stamps = [role_image_dict.get(str(role).lower()) for role in roles]
    stamps = [x for x in stamps if x is not None]
    return stamps


async def add_stamps(stamps: list, user_name: str, avatar: Image):
    bg = Image.open(base_image)
    avatar = avatar.resize((500, 500), Image.LANCZOS)
    bg.paste(avatar, (100, 420))
    for stamp in stamps:
        overlay = Image.open(stamp)
        bg.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(bg)
    name_font = ImageFont.truetype(pass_font, size=70)
    draw.text((660, 550), user_name.upper(), font=name_font, fill='black')

    result_path = os.path.join(image_dir, 'result.png')
    bg.save(result_path, format='PNG')

    return result_path
