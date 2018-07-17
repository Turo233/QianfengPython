import time
import pygame

#pip install pygame

#音乐路径
filePath = r"D:\CloudMusic\Acoustic Trench - 【指弹吉他】George Michael「Careless Whisper」.mp3"


#初始化
pygame.mixer.init()

#加载音乐
track = pygame.mixer.music.load(filePath)

#播放
pygame.mixer.music.play()

# 播放时间
time.sleep(5)
#暂停
pygame.mixer.music.pause()


#停止
pygame.mixer.music.stop()
