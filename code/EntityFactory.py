#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'BG':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'BG{i}', (0,0)))
                    list_bg.append(Background(f'BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT /2))
            case 'EnemyH1':
                return Enemy('EnemyH1', (WIN_WIDTH  + 10,random.randint(25,470)))
            case 'EnemyH2':
                return Enemy('EnemyH2', (WIN_WIDTH + 10, random.randint(25, 470)))
            case 'EnemyT11':
                return Enemy('EnemyT11', (WIN_WIDTH + 10, random.randint(510, 530)))
