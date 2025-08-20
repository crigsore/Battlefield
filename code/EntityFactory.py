#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: 'str', position=(0,0)):
        match entity_name:
            case 'BG1':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'BG1{i}', (0,0)))
                return list_bg
        return None
