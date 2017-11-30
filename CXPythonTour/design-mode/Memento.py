# coding=utf-8

"""
Created on 2017-11-29
@author: Palesnow

功能：备忘录模式
网址：https://yq.aliyun.com/articles/71199?spm=5176.100239.blogrightarea71065.21.539dde26dStcwa

实例：游戏进度保存

"""

from random import *

# 游戏角色
class GameCharactor():
    vitality = 0  # 生命值
    attack = 0  # 攻击值
    defense = 0  # 防御值
    def displayState(self):
        print("Current Values:")
        print("Life: %d" % self.vitality)
        print("Attack: %d" % self.attack)
        print("Defence: %d" % self.defense)
    def initState(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
    def saveState(self):
        return Memento(self.vitality, self.attack, self.defense)
    def recoverState(self, memento):
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense

class FightCharactor(GameCharactor):
    def fight(self):
        self.vitality -= randint(10, 99)

class Memento:
    vitality = 0
    attack = 0
    defense = 0
    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense

if __name__ == "__main__":
    game_chrctr = FightCharactor()
    game_chrctr.initState(100, 79, 60)
    game_chrctr.displayState()

    memento = game_chrctr.saveState()

    game_chrctr.fight()
    game_chrctr.displayState()

    game_chrctr.recoverState(memento)
    game_chrctr.displayState()
