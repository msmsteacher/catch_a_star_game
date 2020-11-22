import pygame
from Control import Control
from Mode import Mode

'''
Menuクラス
    メニューを表示するクラス
'''
class Menu():
    def __init__(self, media):
        self.titlefont = pygame.font.SysFont('inkfree', 80)
        self.title = self.titlefont.render("Catch a star game!", True, (255,255,255))
        self.comment = pygame.font.SysFont('inkfree', 40)
        self.title_menu = [self.comment.render(st, True, (255,255,255)) for st in ["PLAY","SETTING","RANKING","BYE"]]
        self.choose = 0 # 現在の選択されている位置
        self.control = Control()
        self.media = media

    def main(self, screen, difficulty, rect_player):
        # タイトルと設定情報の描画
        screen.blit(self.title, (20,50))
        for i, me in enumerate(self.title_menu):
            screen.blit(me, (500,50*i+200))

        # コントロール操作
        con = self.control.control()
        if con == 'up':
            if self.choose > 0:
                self.media.button1.play()
                self.choose -= 1
        elif con == 'down':
            if self.choose < len(self.title_menu)-1:
                self.media.button1.play()
                self.choose += 1
        if con == 'return':
            if self.choose + 1 == Mode.PLAY:
                self.media.kirakira.play()
                self.media.play_bgm(2)
                rect_player.center = (100, 550)
                return Mode.PLAY
            elif self.choose + 1 == Mode.SETTING:
                self.media.kirakira.play()
                return Mode.SETTING
            elif self.choose + 1 == Mode.RANKING:
                self.media.kirakira.play()
                return Mode.RANKING
            elif self.choose + 1 == Mode.BYE:
                self.media.kirakira.play()
                return Mode.BYE
            else:
                rect_player.center = (450, 220 + self.choose*50)
                return Mode.MENU
        
        rect_player.center = (450, 220 + self.choose*50)
        return Mode.MENU