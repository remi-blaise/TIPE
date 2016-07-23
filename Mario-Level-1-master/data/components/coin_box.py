__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin


class Coin_box(pg.sprite.Sprite):
    """Coin box sprite"""
    def __init__(self, config, x, y, contents, group): # There was default values: contents='coin', group=None, unused
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']
        self.frames = []
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image) # Inutilisé ?
        self.animation_timer = 0
        self.first_half = True   # First half of animation cycle
        self.state = c.RESTING
        self.rest_height = y
        self.gravity = 1.2
        self.y_vel = 0
        self.contents = contents
        self.group = group
        self.config = config


    def get_image(self, x, y, width, height):
        """Extract image from sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def setup_frames(self):
        """Create frame list"""
        self.frames.append(
            self.get_image(384, 0, 16, 16))
        self.frames.append(
            self.get_image(400, 0, 16, 16))
        self.frames.append(
            self.get_image(416, 0, 16, 16))
        self.frames.append(
            self.get_image(432, 0, 16, 16))


    def update(self, game_info):
        """Update coin box behavior"""
        self.current_frame = game_info[c.CURRENT_FRAME]
        self.handle_states()


    def handle_states(self):
        """Determine action based on RESTING, BUMPED or OPENED
        state"""
        if self.state == c.RESTING:
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()


    def resting(self):
        """Action when in the RESTING state"""
        if self.first_half:
            if self.frame_index == 0:
                if (self.current_frame - self.animation_timer) > 375*self.config.fps/1000:
                    self.frame_index += 1
                    self.animation_timer = self.current_frame
            elif self.frame_index < 2:
                if (self.current_frame - self.animation_timer) > 125*self.config.fps/1000:
                    self.frame_index += 1
                    self.animation_timer = self.current_frame
            elif self.frame_index == 2:
                if (self.current_frame - self.animation_timer) > 125*self.config.fps/1000:
                    self.frame_index -= 1
                    self.first_half = False
                    self.animation_timer = self.current_frame
        else:
            if self.frame_index == 1:
                if (self.current_frame - self.animation_timer) > 125*self.config.fps/1000:
                    self.frame_index -= 1
                    self.first_half = True
                    self.animation_timer = self.current_frame

        self.image = self.frames[self.frame_index]


    def bumped(self):
        """Action after Mario has bumped the box from below"""
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y > self.rest_height + 5:
            self.rect.y = self.rest_height
            self.state = c.OPENED
            if self.contents == 'mushroom':
                self.group.add(powerups.Mushroom(self.config, self.rect.centerx, self.rect.y))
            elif self.contents == 'fireflower':
                self.group.add(powerups.FireFlower(self.config, self.rect.centerx, self.rect.y))
            elif self.contents == '1up_mushroom':
                self.group.add(powerups.LifeMushroom(self.config, self.rect.centerx, self.rect.y))


        self.frame_index = 3
        self.image = self.frames[self.frame_index]


    def start_bump(self, score_group):
        """Transitions box into BUMPED state"""
        self.y_vel = -6
        self.state = c.BUMPED

        if self.contents == 'coin':
            self.group.add(coin.Coin(self.config, self.rect.centerx,
                                     self.rect.y,
                                     score_group))
            setup.SFX['coin'].play()
        else:
            setup.SFX['powerup_appears'].play()


    def opened(self):
        """Placeholder for OPENED state"""
        pass











