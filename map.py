import pygame
import pytmx
from pytmx.util_pygame import load_pygame

class MapManager:

    def __init__(self):
        load_pygame('assets\map\map.tmx')