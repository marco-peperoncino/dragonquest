# ドラゴンクエスト ふっかつのじゅもん
# 下記２つのページを大いに参考にさせていただいております。
# https://qiita.com/yoshi389111/items/29ade2f62483e9c095d9
# https://oscdis.hatenablog.com/entry/2014/03/30/225043


import pyxel

# 文字コード
str_code = (
    0, 1, 2, 3, 4, 30, 31, 32, 33, 34,
    5, 6, 7, 8, 9, 44, 45, 46, 47, 48,
    10, 11, 12, 13, 14, 49, 50, 51, 52, 53,
    15, 16, 17, 18, 19, 54, 55, 56, 57, 58,
    20, 21, 22, 23, 24, 38, 39, 40, 41, 42,
    25, 26, 27, 28, 29, 59, 60, 61, 62, 63,
    35, 36, 37, 43
)

# 文字と文字コード対応表
str_dic = {
    'あ': 0, 'い': 1, 'う': 2, 'え': 3, 'お': 4,
    'か': 5, 'き': 6, 'く': 7, 'け': 8, 'こ': 9,
    'さ': 10, 'し': 11, 'す': 12, 'せ': 13, 'そ': 14,
    'た': 15, 'ち': 16, 'つ': 17, 'て': 18, 'と': 19,
    'な': 20, 'に': 21, 'ぬ': 22, 'ね': 23, 'の': 24,
    'は': 25, 'ひ': 26, 'ふ': 27, 'へ': 28, 'ほ': 29,
    'ま': 30, 'み': 31, 'む': 32, 'め': 33, 'も': 34,
    'や': 35, 'ゆ': 36, 'よ': 37,
    'ら': 38, 'り': 39, 'る': 40, 'れ': 41, 'ろ': 42,
    'わ': 43,
    'が': 44, 'ぎ': 45, 'ぐ': 46, 'げ': 47, 'ご': 48,
    'ざ': 49, 'じ': 50, 'ず': 51, 'ぜ': 52, 'ぞ': 53,
    'だ': 54, 'ぢ': 55, 'づ': 56, 'で': 57, 'ど': 58,
    'ば': 59, 'び': 60, 'ぶ': 61, 'べ': 62, 'ぼ': 63,
}

# 入力した文字が表示される所の座標
pwd_pos = (
    (64, 48), (72, 48), (80, 48), (88, 48), (96, 48),
    (112, 48), (120, 48), (128, 48), (136, 48), (144, 48),
    (152, 48), (160, 48), (64, 72), (72, 72), (80, 72),
    (88, 72), (96, 72), (112, 72), (120, 72), (128, 72)
)

# 名前用文字
name_code = (
    '０', '１', '２', '３', '４',
    '５', '６', '７', '８', '９',
    'あ', 'い', 'う', 'え', 'お',
    'か', 'き', 'く', 'け', 'こ',
    'さ', 'し', 'す', 'せ', 'そ',
    'た', 'ち', 'つ', 'て', 'と',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ',
    'ら', 'り', 'る', 'れ', 'ろ',
    'わ', 'を', 'ん',
    'っ', 'ゃ', 'ゅ', 'ょ',
    '”', '゜', '－',
)


class SaveData:
    # ("item1", ctypes.c_ubyte, 4),       # 1番目のアイテム 4bit 0～14
    # ("item2", ctypes.c_ubyte, 4),       # 2番目のアイテム 4bit 0～14

    # ("flg2", ctypes.c_ubyte, 1),        # フラグ せんしのゆびわを装備しているか 1bit
    # ("name2", ctypes.c_ubyte, 6),       # 名前2文字目 6bit 0～63
    # ("flg1", ctypes.c_ubyte, 1),        # フラグ りゅうのうろこを装備したことがあるか 1bit

    # ("exp_hi", ctypes.c_ubyte, 8),      # 経験値上位 8bit

    # ("item5", ctypes.c_ubyte, 4),       # 5番目のアイテム 4bit 0～14
    # ("item6", ctypes.c_ubyte, 4),       # 6番目のアイテム 4bit 0～14

    # ("herbs", ctypes.c_ubyte, 4),       # やくそう個数 4bit 0～6
    # ("key", ctypes.c_ubyte, 4),         # かぎ個数 4bit 0～6

    # ("gold_hi", ctypes.c_ubyte, 8),     # ゴールド上位 8bit

    # ("shield", ctypes.c_ubyte, 2),      # たて 2bit 0～3
    # ("armor", ctypes.c_ubyte, 3),       # よろい 3bit 0～7
    # ("wepon", ctypes.c_ubyte, 3),       # ぶき 3bit 0～7

    # ("name4", ctypes.c_ubyte, 6),       # 名前4文字目 6bit 0～63
    # ("flg3", ctypes.c_ubyte, 1),        # フラグ ドラゴンを倒したか 1bit
    # ("crypt1", ctypes.c_ubyte, 1),      # 暗号化キー1 1bit

    # ("item7", ctypes.c_ubyte, 4),       # 7番目のアイテム 4bit 0～14
    # ("item8", ctypes.c_ubyte, 4),       # 8番目のアイテム 4bit 0～14

    # ("crypt2", ctypes.c_ubyte, 1),      # 暗号化キー2 1bit
    # ("flg4", ctypes.c_ubyte, 1),        # フラグ ゴーレムを倒したか 1bit
    # ("name1", ctypes.c_ubyte, 6),       # 名前1文字目 6bit 0～63

    # ("gold_low", ctypes.c_ubyte, 8),    # ゴールド下位 8bit

    # ("item3", ctypes.c_ubyte, 4),       # 3番目のアイテム 4bit 0～14
    # ("item4", ctypes.c_ubyte, 4),       # 4番目のアイテム 4bit 0～14

    # ("name3", ctypes.c_ubyte, 6),       # 名前3文字目 6bit 0～63
    # ("flg5", ctypes.c_ubyte, 1),        # フラグ しのくびかざりを入手したことがあるか 1bit
    # ("crypt3", ctypes.c_ubyte, 1),      # 暗号化キー3 1bit

    # ("exp_low", ctypes.c_ubyte, 8),     # 経験値下位 8bit

    # ("crc", ctypes.c_ubyte, 8),         # CRC 8bit

    def __init__(self):

        # セーブデータ15byte分
        self.savedata = [0] * 15
        # ふっかつのじゅもん20文字分
        # けせいなの　へごべううつに　はほめよれ　よごぜ
        self.word = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 0, 4, 8, 12, 16]
        # self.word = [8, 13, 1, 20, 24, 28, 48, 62, 2, 2, 17, 21, 25, 29, 36, 37, 41, 37, 48, 52]

    def crc(self):
        cd = 0x8000  # 1000 0000 0000 0000
        for i in range(15):
            for j in range(8):
                if cd & 0x8000:
                    cd = (cd << 1) ^ 0x1021  # 0001 0000 0010 0001
                else:
                    cd <<= 1

    def load(self):
        data = [0] * 20

        self.word = self.pswd_to_code('ふるいけやかわずとびこむみずのおとばしや')

        # for i in self.word:
        #     print(i, end=' ')
        # print('')

        self.decrypt(data)
        self.savedata = self.convert_6to8(data)
        print('なまえ', self.get_name())
        # for i in data:
        #     print(i)

    def decrypt(self, data):
        # まずふっかつのじゅもんのうしろの文字からひとつ前の文字を引いて、
        # さらにそこから４を引いた数字から6bit取り出す
        index = 19
        for i in range(index):
            data[index] = (self.word[index] - self.word[index - 1] - 4) & 0x3F  # 0011 1111
            index -= 1

        data[0] = (self.word[0] - 4) & 0x3F

    # ふっかつのじゅもんを数値化した物を後ろの6bitを前に8bitに切り分けながら並べ替え
    def convert_6to8(self, data):
        d = []
        index = 19
        for i in range(5):
            tmp = (data[index] << 18) | (data[index - 1] <<
                                         12) | (data[index - 2] << 6) | data[index - 3]
            d.append((tmp >> 16) & 0xFF)
            d.append((tmp >> 8) & 0xFF)
            d.append(tmp & 0xFF)
            index -= 4

        return d

    def get_name(self):
        name = name_code[(self.savedata[9] >> 2) & 0x3F]
        name += name_code[(self.savedata[1] >> 1) & 0x3F]
        name += name_code[self.savedata[12] & 0x3F]
        name += name_code[self.savedata[7] & 0x3F]

        return name

    def pswd_to_code(self, pswd):
        code = []

        for s in pswd:
            code.append(str_dic[s])

        return code


class App:
    def __init__(self):
        # 上段の入力した文字が表示されている所のカーソル位置
        self.pos = 0
        # 下段の文字を選択する所のカーソル位置 [x, y]
        self.cur = [0, 0]
        # 入力した文字番号 -1は＊
        self.pwd = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -
                    1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        # カーソルを点滅させるためのフラグ
        self.blink_flg = True

        self.save_data = SaveData()
        self.save_data.load()

        pyxel.init(256, 240, caption='Dragon Quest ～ふっかつのじゅもん～')
        pyxel.load('my_resource.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.cur[0] -= 1
            if self.cur[0] < 0:
                self.cur[0] = 0
            if self.cur[1] == 6 and (self.cur[0] == 5 or self.cur[0] == 7):
                self.cur[0] -= 1
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.cur[0] += 1
            if self.cur[0] > 9:
                self.cur[0] = 9
            if self.cur[1] == 6 and (self.cur[0] == 5 or self.cur[0] == 7):
                self.cur[0] += 1
            if self.cur[1] == 6 and self.cur[0] == 9:
                self.cur[0] -= 1
        elif pyxel.btnp(pyxel.KEY_UP):
            self.cur[1] -= 1
            if self.cur[1] < 0:
                self.cur[1] = 0
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.cur[1] += 1
            if self.cur[1] > 6:
                self.cur[1] = 6
            if self.cur[1] == 6 and (self.cur[0] == 5 or self.cur[0] == 7 or self.cur[0] == 9):
                self.cur[0] -= 1

        # スペースキーで文字決定
        if pyxel.btnp(pyxel.KEY_SPACE):
            # ピッピ音
            pyxel.play(0, 0)

            # 文字位置計算
            cur_pos = self.cur[0] + self.cur[1] * 10

            # 文字の場合
            if cur_pos <= 63:
                self.pwd[self.pos] = str_code[cur_pos]
                if self.pos < 19:
                    self.pos += 1
            # もどる
            elif cur_pos == 64:
                if self.pos > 0:
                    self.pos -= 1
            # すすむ
            elif cur_pos == 66:
                if self.pos < 19:
                    self.pos += 1
            # おわり
            elif cur_pos == 68:
                print('おわり')

            # for p in self.pwd:
            #     print(f'{p}, ', end='')
            # print('')

        # カーソルを点滅させる
        if pyxel.frame_count % 4 == 0:
            self.blink_flg = False if self.blink_flg else True

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 32, 30)

        # 三角カーソル
        if self.blink_flg:
            pyxel.blt(56 + self.cur[0] * 16, 104 + self.cur[1] * 16, 0, 16, 72, 8, 8)

        # 上段入力文字下のカーソル
        pyxel.blt(pwd_pos[self.pos][0], pwd_pos[self.pos][1] + 8, 0, 16, 64, 8, 8)

        # 入力したふっかつのじゅもん
        for i, p in enumerate(self.pwd):
            if p == -1:
                pyxel.blt(pwd_pos[i][0], pwd_pos[i][1], 0, 8, 72, 8, 8)
            else:
                pyxel.blt(pwd_pos[i][0], pwd_pos[i][1] - 8, 0, 0 + p %
                          32 * 8, 16 + p // 32 * 16, 8, 16)


App()
