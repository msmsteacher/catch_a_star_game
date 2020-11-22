import pygame
from Mode import Mode
from Control import Control

'''
Rankingクラス
    ランキングを管理するクラス
'''
class Ranking():
    def __init__(self, media):
        self.titlefont = pygame.font.SysFont('inkfree', 80)
        self.title = self.titlefont.render("Ranking", True, (255,255,255))
        self.comment = pygame.font.SysFont('inkfree', 40)
        self.control = Control()
        self.media = media
        self.ranking = []
        self.write_point = 0
        
    def main(self, screen, defficulty, rect_player):
        # タイトルと情報の描画
        screen.blit(self.title, (20,50))
        screen.blit(self.comment.render("EXIT", True, (255,255,255)), (580, 580))
        screen.blit(self.comment.render("Rank   Score    Name", True, (255,0,0)), (450, 0))
        try:
            with open(self.media.ranking_txt) as f:
                ranking_str = [s.strip() for s in f.readlines()]
                for i, row in enumerate(ranking_str):
                    score, name = row.split(",")
                    screen.blit(self.comment.render(str(i+1), True, (255,255,255)), (480, 50+i*50))
                    screen.blit(self.comment.render(score, True, (255,255,255)), (580, 50+i*50))
                    screen.blit(self.comment.render(name, True, (255,255,255)), (715, 50+i*50))
        except FileNotFoundError:
            pass # まだファイルが作成されていなければ何も表示しない

        # exitの位置に常に配置
        rect_player.center = (530, 600)

        # コントロール操作(exitのみ)
        con = self.control.control()
        if con == 'return':
            self.media.kirakira.play()
            return Mode.MENU

        return Mode.RANKING

    def read_ranking(self, get_star):
        try:
            with open(self.media.ranking_txt) as f:
                # テキストからランキング情報を読み込む
                # ランキングは"socre,name"というカンマ区切りで記述されている
                ranking_str = [s.strip() for s in f.readlines()]
                renew_ranking = False
                if len(ranking_str) != 0:
                    for i, row in enumerate(ranking_str):
                        score, name = row.split(",")
                        if int(score) <= get_star and renew_ranking == False:
                            self.ranking.append((str(get_star)+","))
                            renew_ranking = True
                            self.write_point = i
                        self.ranking.append(score + ',' + name)
                    if renew_ranking == False and i != 9: # ランキング最下位にまだ余裕があったら
                        self.ranking.append(str(get_star) + ',')
                        self.write_point = i + 1
                        renew_ranking = True
                    elif renew_ranking == True and i == 9: # ランキング満員で更新されたら
                        self.ranking.pop(10) # 一番下の人を取り除く
                else:
                    raise FileNotFoundError # テキストファイルが何も書かれていなかったら

        except FileNotFoundError: # テキストファイルが存在しないor何も書いていない場合
            self.ranking.append(str(get_star) + ',')
            self.write_point = 0
            renew_ranking = True
        
        return renew_ranking

    def write_ranking(self, your_name):
        self.ranking[self.write_point] += your_name
        with open(self.media.ranking_txt, 'w') as f:
            f.write('\n'.join(self.ranking))