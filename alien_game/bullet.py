import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): #Bullet类继承Sprite类
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        #在(0，0)处创建一个表示子弹的矩形，在设置其位置
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,
                    ai_settings.bullet_height)      #子弹不是图像，调用pygame.Rect()来创建矩形
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #使用小数点表示子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_facter = ai_settings.bullet_speed_facter

    def update(self):
        """向上移动子弹"""
        #更新子弹的位置
        self.y -= self.speed_facter
        #更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)