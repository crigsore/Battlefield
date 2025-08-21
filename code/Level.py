#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WHITE, WIN_HEIGHT, BLACK, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('BG'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 60000                                       # Level time (60 seconds)
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
                 if event.type == EVENT_ENEMY:
                     choice = random.choice(('EnemyH1', 'EnemyH2'))
                     self.entity_list.append(EntityFactory.get_entity(choice))

            # Printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', BLACK, (10,5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', BLACK, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entity: {len(self.entity_list)}', BLACK, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Comic Sans MS', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
