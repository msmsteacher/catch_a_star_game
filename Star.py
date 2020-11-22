import pygame

'''
Starクラス
    星本体のクラス
'''
class Star():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    '''
    当たり判定メソッド
    '''
    def hit(self, rect_player, hit_range):
        # プレイヤーが星の中心から縦横hit_range以内であればTrueを返す
        if rect_player.centery - hit_range < self.y + 25 < rect_player.centery + hit_range and \
            rect_player.centerx - hit_range < self.x + 25 < rect_player.centerx + hit_range:
            return True
        else:
            return False