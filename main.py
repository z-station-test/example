# -*- coding: utf-8 -*-
import logging
import random
from utils import conf, consts


logging.basicConfig(
    filename=conf.LOG_PATH,
    format=conf.LOG_FORMAT,
    level=logging.DEBUG if conf.DEBUG else logging.INFO,
)


class Member(object):

    """ Класс представляет сущность участника команды """

    def __init__(self):

        """ Аргумент name заполняется автоматически """

        self.name = self._get_rand_name()
        self.logger = logging.getLogger('class Member')
        self.logger.info(f'Инициализация нового объекта: "{self.name}"')

    @staticmethod
    def _get_rand_name() -> str:
        key = random.randint(1, len(consts.NAMES))
        return consts.NAMES[key]

    def __str__(self):
        return self.name


if __name__ == '__main__':
    member = Member()
