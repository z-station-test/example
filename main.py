# -*- coding: utf-8 -*-
import logging
from utils import conf, consts


logging.basicConfig(
    filename=conf.LOG_PATH,
    format=conf.LOG_FORMAT,
    level=logging.DEBUG if conf.DEBUG else logging.INFO,
)


class Boy(object):

    def __init__(self, name: str):
        self.name = name
        self.health = consts.START_HEALTH
        self.defence = consts.START_DEFENCE

        self.logger = logging.getLogger('class Boy')
        self.logger.info(f'Инициализация нового объекта: "{name}"')

    def __str__(self):
        return self.name


if __name__ == '__main__':
    boy = Boy(name='Archer')
    father = Boy(name='Berserker')
