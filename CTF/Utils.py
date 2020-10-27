import os.path

SPRITES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'Sprites'
)

LOAD_IMG = lambda img: os.path.join(SPRITES_DIR, img)