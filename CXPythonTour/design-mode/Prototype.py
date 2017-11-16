# coding=utf-8

"""
Created on 2017-11-13
@author: Palesnow

功能：原型模式实现
网址：https://yq.aliyun.com/articles/70451?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&utm_content=m_11964

"""

from copy import copy, deepcopy

class simpleLayer:
    background = [0, 0, 0, 0]
    content = "blank"
    def getContent(self):
        return self.content
    def getBackground(self):
        return self.background
    def paint(self, painting):
        self.content = painting
    def setParent(self, p):
        self.background[3] = p
    def fillBackground(self, back):
        self.background = back

    """
    浅拷贝：一般来说，浅拷贝会拷贝对象内容及其内容的引用或者子对象的引用，但不会拷贝引用的内容和子对象本身；
           浅拷贝只是对指针的拷贝，拷贝后两个指针指向同一个内存空间
    深拷贝：不仅拷贝了对象和内容的引用，也会拷贝引用的内容
           深拷贝不但对指针进行拷贝，而且对指针指向的内容进行拷贝，经深拷贝后的指针是指向两个不同地址的指针。
    """
    def clone(self):
        return copy(self)
    def deep_clone(self):
        return deepcopy(self)

if __name__ == "__main__":
    dog_layer = simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0, 0, 255, 0])
    print("Original Background:", dog_layer.getBackground())
    print("Original Painting:", dog_layer.getContent())

    another_dog_layer = dog_layer.deep_clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint("Puppy")
    print("Original Background:", dog_layer.getBackground())
    print("Original Painting:", dog_layer.getContent())
    print("Copy Background:", another_dog_layer.getBackground())
    print("Copy Painting:", another_dog_layer.getContent())