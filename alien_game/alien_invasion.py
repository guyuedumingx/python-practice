import pygame

from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    #初始化游戏并建立屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Ivasion")

    #创建一只飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于储存子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)

    #开始游戏循环
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)    
run_game()