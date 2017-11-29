# coding=utf-8

"""
Created on 2017-11-29
@author: Palesnow

功能：解释器模式
网址：https://yq.aliyun.com/articles/71065?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&2017315&utm_content=m_13630

实例：模拟吉他

"""

# 谱
class PlayContext():
    play_text = None

# 解释器
class Expression():
    # 转译谱
    def interpret(self, context):
        if len(context.play_text) == 0:
            return
        else:
            play_segs = context.play_text.split(" ")
            for play_seg in play_segs:
                pos = 0
                for ele in play_seg:
                    if ele.isalpha():
                        pos += 1
                        continue
                    break
                play_chord = play_seg[0: pos]
                play_value = play_seg[pos:]
                self.execute(play_chord, play_value)

    # 演奏
    def execute(self, play_key, play_value):
        pass

# 吉他演奏
class NormGuitar(Expression):
    def execute(self, play_key, play_value):
        print("Normal Cuitar Playing -- Chord:%s Play Tune:%s" % (play_key, play_value))


if __name__ == "__main__":
    context = PlayContext()
    context.play_text = "C53231323 Em43231323 F43231323 G63231323"

    guitar = NormGuitar()
    guitar.interpret(context)