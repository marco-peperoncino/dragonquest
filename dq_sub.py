import pyxel

# ウィンドウに使うtilemap番号の最初の番号
WINDOW_TILEMAP = 1

# 文字コード(本命)
CHARA_DAKU = 1      # 濁点文字
CHARA_HANDAKU = 2   # 半濁点文字
character_code = {
    '　': (0, 0), ' ': (0, 0),
    'あ': (1, 0), 'い': (2, 0), 'う': (3, 0), 'え': (4, 0), 'お': (5, 0),
    'か': (6, 0), 'き': (7, 0), 'く': (8, 0), 'け': (9, 0), 'こ': (10, 0),
    'が': (6, CHARA_DAKU), 'ぎ': (7, CHARA_DAKU), 'ぐ': (8, CHARA_DAKU),
    'げ': (9, CHARA_DAKU), 'ご': (10, CHARA_DAKU),
    'さ': (11, 0), 'し': (12, 0), 'す': (13, 0), 'せ': (14, 0), 'そ': (15, 0),
    'ざ': (11, CHARA_DAKU), 'じ': (12, CHARA_DAKU), 'ず': (13, CHARA_DAKU),
    'ぜ': (14, CHARA_DAKU), 'ぞ': (15, CHARA_DAKU),
    'た': (16, 0), 'ち': (17, 0), 'つ': (18, 0), 'て': (19, 0), 'と': (20, 0),
    'だ': (16, CHARA_DAKU), 'ぢ': (17, CHARA_DAKU), 'づ': (18, CHARA_DAKU),
    'で': (19, CHARA_DAKU), 'ど': (20, CHARA_DAKU),
    'な': (21, 0), 'に': (22, 0), 'ぬ': (23, 0), 'ね': (24, 0), 'の': (25, 0),
    'は': (26, 0), 'ひ': (27, 0), 'ふ': (28, 0), 'へ': (29, 0), 'ほ': (30, 0),
    'ば': (26, CHARA_DAKU), 'び': (27, CHARA_DAKU), 'ぶ': (28, CHARA_DAKU),
    'べ': (29, CHARA_DAKU), 'ぼ': (30, CHARA_DAKU),
    'ぱ': (26, CHARA_HANDAKU), 'ぴ': (27, CHARA_HANDAKU), 'ぷ': (28, CHARA_HANDAKU),
    'ぺ': (29, CHARA_HANDAKU), 'ぽ': (30, CHARA_HANDAKU),
    'ま': (31, 0), 'み': (32, 0), 'む': (33, 0), 'め': (34, 0), 'も': (35, 0),
    'や': (36, 0), 'ゆ': (37, 0), 'よ': (38, 0),
    'ら': (39, 0), 'り': (40, 0), 'る': (41, 0), 'れ': (42, 0), 'ろ': (43, 0),
    'わ': (44, 0), 'を': (45, 0), 'ん': (46, 0),
    'っ': (47, 0), 'ゃ': (48, 0), 'ゅ': (49, 0),
    'イ': (50, 0), 'カ': (51, 0), 'ガ': (51, CHARA_DAKU), 'キ': (52, 0), 'ギ': (52, CHARA_DAKU),
    'コ': (53, 0), 'ゴ': (53, CHARA_DAKU), 'シ': (54, 0), 'ジ': (54, CHARA_DAKU),
    'ス': (55, 0), 'ズ': (55, CHARA_DAKU), 'タ': (56, 0), 'ダ': (56, CHARA_DAKU),
    'ト': (57, 0), 'ド': (70, 0),
    'ヘ': (58, 0), 'ベ': (58, CHARA_DAKU), 'ペ': (58, CHARA_HANDAKU),
    'ホ': (59, 0),  'ボ': (59, CHARA_DAKU), 'ポ': (59, CHARA_HANDAKU),
    'マ': (60, 0), 'ミ': (61, 0), 'ム': (62, 0), 'メ': (63, 0),
    'ラ': (64, 0), 'リ': (65, 0), 'ル': (66, 0), 'レ': (67, 0), 'ロ': (68, 0),
    'ン': (69, 0),
    '0': (71, 0), '０': (71, 0), '1': (72, 0), '１': (72, 0), '2': (73, 0), '２': (73, 0),
    '3': (74, 0), '３': (74, 0), '4': (75, 0), '４': (75, 0), '5': (76, 0), '５': (76, 0),
    '6': (77, 0), '６': (77, 0), '7': (78, 0), '７': (78, 0), '8': (79, 0), '８': (79, 0),
    '9': (80, 0), '９': (80, 0),
    'H': (81, 0), 'M': (82, 0), 'P': (83, 0), 'G': (84, 0), 'E': (85, 0),
    '。': (86, 0), '゛': (87, 0), '゜': (88, 0), ':': (89, 0), '?': (90, 0), '!': (91, 0), '・': (92, 0),
    '-': (93, 0), '「': (94, 0), '*': (95, 0),
    '力': (51, 0),
}


def text(x, y, str, lf=False, feed=0):

    dx = x

    for s in str:

        # 改行
        if lf and s == '\n':
            dx = x + feed * 8
            y += 16
            continue

        pyxel.blt(dx, y, 0, character_code[s][0] %
                  32 * 8,  character_code[s][0] // 32 * 8, 8, 8)
        if character_code[s][1] == CHARA_DAKU:
            pyxel.blt(dx, y - 8, 0, 184, 16, 8, 8)
        elif character_code[s][1] == CHARA_HANDAKU:
            pyxel.blt(dx, y - 8, 0, 176, 16, 8, 8)

        dx += 8


class Window:
    def __init__(self, no, x, y, w, h, title=''):
        self.no = WINDOW_TILEMAP + no
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.dw = 0

        self.title = title

        self.set()

    def set(self):

        d = []

        # 上列
        # 左上角
        s = '080'
        # 上ライン
        for i in range(self.w - 2):
            s += '082'
        # 右上角
        s += '083'
        d.append(s)

        # 高さ列
        for j in range(self.h - 2):
            # 左縦棒
            s = '0A0'
            for i in range(self.w - 2):
                s += '000'
            # 右縦棒
            s += '0A3'
            d.append(s)

        # 下ライン
        s = '0C0'
        # 上ライン
        for i in range(self.w - 2):
            s += '0C1'
        # 右上角
        s += '0C3'
        d.append(s)

        # ウィンドウタイトル有の場合
        if self.title != '':
            # ウィンドウのタイルマップデータを取得して
            # センター位置になる様にタイトル表示位置を計算
            # 計算した位置の文字列をタイトル文字に置き換える
            s = d[0]
            tx = (self.w - len(self.title)) // 2
            # *3は16進数が3桁だから
            s = s[:tx * 3] + self.get_text_tilemapdata(self.title) + s[(tx + len(self.title)) * 3:]
            d[0] = s

        pyxel.tilemap(self.no).set(0, 0, d)
        # pyxel.tilemap(1).refimg = 0

    # テキストを付加したtilemapデータ文字列を取得
    # type=1の時、濁点・半濁点取得用
    def get_text_tilemapdata(self, str, type=0):
        ts = ''
        for s in str:
            if type:
                if character_code[s][1] == CHARA_DAKU:
                    ts += format(character_code['゛'][0], '03x')
                elif character_code[s][1] == CHARA_HANDAKU:
                    ts += format(character_code['゜'][0], '03x')
                else:
                    ts += '000'
            else:
                ts += format(character_code[s][0], '03x')

        return ts

    def disp(self):
        pyxel.bltm(self.x, self.y, self.no, 0, 0, self.w, self.h)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_text(self, x, y, str):
        # 濁点、半濁点対応の為２行分用意
        d = ['', '']
        # テキストをセットする行のデータを取得
        # ただし枠の部分は取得しない
        for i in range(self.w - 2):
            d[0] += format(pyxel.tilemap(self.no).get(i + 1, y - 1), '03x')
            d[1] += format(pyxel.tilemap(self.no).get(i + 1, y), '03x')

        # テキストをセット
        d[0] = d[0][:(x - 1) * 3] + self.get_text_tilemapdata(str, 1) + d[0][(x + len(str)) * 3:]
        d[1] = d[1][:(x - 1) * 3] + self.get_text_tilemapdata(str) + d[1][(x + len(str)) * 3:]

        pyxel.tilemap(self.no).set(1, y - 1, d)
