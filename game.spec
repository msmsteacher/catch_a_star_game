# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['game.py'],
             pathex=['C:\\Users\\Amt_s\\Downloads\\game'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('1menu.jpg', '.\\1menu.jpg', 'DATA'),
            ('2main.jpg','.\\2main.jpg', 'DATA'),
            ('3setting.jpg','.\\3setting.jpg', 'DATA'),
            ('4ranking.jpg','.\\4ranking.jpg', 'DATA'),
            ('5bye.jpg','.\\5bye.jpg', 'DATA'),
            ('button1.wav','.\\button1.wav', 'DATA'),
            ('button2.wav','.\\button2.wav', 'DATA'),
            ('chara0.png','.\\chara0.png', 'DATA'),
            ('chara1.png','.\\chara1.png', 'DATA'),
            ('chara2.png','.\\chara2.png', 'DATA'),
            ('chara3.png','.\\chara3.png', 'DATA'),
            ('hit.wav','.\\hit.wav', 'DATA'),
            ('kirakira.wav','.\\kirakira.wav', 'DATA'),
            ('music1.mp3','.\\music1.mp3', 'DATA'),
            ('music2.mp3','.\\music2.mp3', 'DATA'),
            ('star.png','.\\star.png', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          name='game',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='game')
