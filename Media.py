import pygame
import os
import glob
import sys

'''
Mediaクラス
    画像や音楽などを読み込むクラス
'''
class Media():
    def __init__(self):
        # 背景画像
        back_list = glob.glob(self.resource_path("*.jpg")) # 末尾が.jpgのものをすべて取得
        back_list.sort()
        self.bg = [pygame.image.load(self.resource_path(img)).convert_alpha() for img in back_list]
        # プレイヤー画像
        chara_list = glob.glob(self.resource_path("chara*.png")) # chara〇.pngのものをすべて取得
        chara_list.sort()
        self.player_anim = [pygame.image.load(self.resource_path(chara)).convert_alpha() for chara in chara_list]
        # 星の画像
        self.star = pygame.image.load(self.resource_path("star.png")).convert_alpha() 
        # 効果音
        self.button1 = pygame.mixer.Sound(self.resource_path("button1.wav"))
        self.button2 = pygame.mixer.Sound(self.resource_path("button2.wav"))
        self.kirakira = pygame.mixer.Sound(self.resource_path("kirakira.wav"))
        self.hit = pygame.mixer.Sound(self.resource_path("hit.wav"))
        # ランキング保存テキスト(個人のフォルダに書き残すためにファイルパスはそのまま)
        self.ranking_txt = 'Save\\ranking.txt'
        try:
            os.mkdir("Save/")
        except FileExistsError:
            pass

    def play_bgm(self, num):        
        pygame.mixer.init(frequency = 44100)
        pygame.mixer.music.load(self.resource_path("music{0}.mp3").format(num))
        pygame.mixer.music.play(-1)


    '''
    exe化したとき画像等が_MEIPASSに展開されるためそれを参照する
    '''
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)