import pygame
from Control import Control
from Mode import Mode

# 規定値を定義
X = 0
Y = 1

'''
Settingクラス
    ゲームの難易度を設定するためのクラス
'''
class Setting():
    def __init__(self, media):
        self.titlefont = pygame.font.SysFont('inkfree', 80)
        self.title = self.titlefont.render("Setting", True, (255,255,255))
        self.comment = pygame.font.SysFont('inkfree', 40)
        self.choose = [1, 0] # 現在の選択されている位置
        self.control = Control()
        self.media = media
        self.menu_str = [["SIZE"," SMALL"," NORMAL"," BIG",""],
                         ["STARS"," FEW"," NORMAL"," MANY","EXIT"],
                         ["SPEED"," SLOW"," NORMAL"," FAST",""]]
    
    def main(self, screen, difficulty, rect_player):
        # タイトルと設定情報の描画
        screen.blit(self.title, (20,50))
        for j, strs in enumerate(self.menu_str):
            for i, st in enumerate(strs):
                if i == difficulty[j]:
                    screen.blit(self.comment.render(st+' <-', True, (255,255,255)), (200+300*j,150+50*i))
                else:
                    screen.blit(self.comment.render(st, True, (255,255,255)), (200+300*j,150+50*i))

        # コントロール操作
        con = self.control.control()
        if con == 'up':
            if self.choose[Y] > 0:
                self.media.button1.play()
                self.choose[Y] -= 1
        elif con == 'down':
            if self.choose[Y] < len(strs) - 2:
                self.media.button1.play()
                self.choose[Y] += 1
        elif con == 'left':
            if self.choose[X] > 0:
                self.media.button1.play()
                self.choose[X] -= 1
        elif con == 'right':
            if self.choose[X] < len(self.menu_str) - 1:
                self.media.button1.play()
                self.choose[X] += 1
        elif con == 'return':
            if self.choose[Y] == 3: #Exit
                self.media.kirakira.play()
                return Mode.MENU
            else:
                self.media.button2.play()
                difficulty[self.choose[X]] = self.choose[Y] + 1

        # 最下部を選択していたら中央になるようにする
        if self.choose[Y] == 3:
            self.choose[X] = 1

        # 実際の画面のサイズに応じた位置にカーソルを移動する
        rect_player.center = (150 + self.choose[X] * 300, 220 + self.choose[Y] * 50)

        return Mode.SETTING