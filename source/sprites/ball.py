import pygame as pg

class Ball(pg.sprite.Sprite):
    def __init__(self, path_list, width, height, speed, screen_width, screen_height):
        pg.sprite.Sprite.__init__(self)
        self.img_list = []

        img_size = [width, height]
        for i in path_list:
            img = pg.image.load(i).convert()
            img = pg.transform.scale(img, img_size)
            self.img_list.append(img)

        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.index = 0
        self.image = self.img_list[self.index]
        self.rect = self.image.get_rect()

    def update_colour(self):
        self.index = (self.index + 1) % 4
        self.image = self.img_list[self.index]

    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.speed[0] = -self.speed[0]
            self.update_colour()
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.speed[1] = -self.speed[1]
            self.update_colour()