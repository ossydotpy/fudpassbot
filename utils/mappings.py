import os

from utils import image_dir


def get_image(name):
    return os.path.join(image_dir, name)


role_image_dict = {
    'helpers': get_image('og.png'),  # for testing purposes
    'fudpassbot': get_image('demonpet.png'),  # for testing purposes
    'fudbudwhale': get_image('wale.png'),
    'fudbudcollector': get_image('collector.png'),
    'fudbudcertified': get_image('og.png'),
    'fudpetmaster': get_image('pet-master.png'),
    'fuddemon': get_image('demonpet.png'),
    'fuddino': get_image('dino.png'),
    'fudalien': get_image('cyclops.png'),
    'fuddaddy': get_image('cookie monster.png'),
    'fudbat': get_image('bat.png'),
    'fudduck': get_image('duck.png'),
    'fudmummy': get_image('mummy.png'),
    'fudbud': get_image('petog.png'),
    'fudape': get_image('fudape.png'),
    'fuddog': get_image('dog.png'),
    'fudbunny king': get_image('bunny.png'),
    'fudsquad': get_image('petskull.png'),
}
