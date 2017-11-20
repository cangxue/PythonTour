# coding=utf-8

"""
Created on 2017-11-20
@author: Palesnow

功能：适配器模式
网址：https://yq.aliyun.com/articles/70536?utm_campaign=wenzhang&utm_medium=article&utm_source=QQ-qun&utm_content=m_11967

"""

# =========接口类=========
# 媒体播放器
class MediaPlayer():
    def play(self, audioType, fileName):
        pass

# 高级媒体播放器
class AdvanceMediaPlayer():
    def playVlc(self, fileName):
        pass
    def playMp4(self, fileName):
        pass

# =========实体类=======
class VlcPlayer(AdvanceMediaPlayer):
    def playVlc(self, fileName):
        print("Playing vlc file. Name: %s" % fileName)
class Mp4Player(AdvanceMediaPlayer):
    def playMp4(self, fileName):
        print("Playing mp4 file. Name: %s" % fileName)

# ==========适配器类======
# MediaPlayer接口的适配器类
class MediaAdapter(MediaPlayer):
    advancePlayer = ""
    def __init__(self, audioType):
        if audioType == "vlc":
            self.advancePlayer = VlcPlayer()
        else:
            self.advancePlayer = Mp4Player()


    def play(self, audioType, fileName):
        if audioType == "vlc":
            self.advancePlayer.playVlc(fileName)
        else:
            self.advancePlayer.playMp4(fileName)

# ===========实体类========
# MediaPlayer接口的实体类
class AudioPlayer(MediaPlayer):
    mediaAdapter = ""
    def play(self, audioType, fileName):
        if audioType == "mp3":
            print("Playing mp3 file. Name: %s" % fileName)
        elif audioType == "vlc" or audioType == "mp4":
            self.mediaAdapter = MediaAdapter(audioType)
            self.mediaAdapter.play(audioType, fileName)
        else:
            print("Invalid media")


# 使用AudioPlayer播放
if __name__ == "__main__":
    audio_player = AudioPlayer()

    audio_player.play("mp3", "beynd the horzon.mp3")
    audio_player.play("mp4", "alone.mp4")
    audio_player.play("vlc", "far far away.vlc")
    audio_player.play("avi", "mind me.avi")

    media_adapter = MediaAdapter("mp4")
    media_adapter.play("mp4", "1111.mp4")



