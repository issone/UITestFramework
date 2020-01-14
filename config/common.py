import os

BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

SCREENSHOT_DIR = os.path.join(BASE_PATH, 'data', 'screenshot')

if not os.path.exists(SCREENSHOT_DIR):
    os.mkdir(SCREENSHOT_DIR)
