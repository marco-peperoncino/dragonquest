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

# 入力した文字が表示される所の座標
pwd_pos = (
    (64, 48), (72, 48), (80, 48), (88, 48), (96, 48),
    (112, 48), (120, 48), (128, 48), (136, 48), (144, 48),
    (152, 48), (160, 48), (64, 72), (72, 72), (80, 72),
    (88, 72), (96, 72), (112, 72), (120, 72), (128, 72)
)


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
                self.pwd[self.pos] = cur_pos
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

        # カーソルを点滅させる
        if pyxel.frame_count % 4 == 0:
            self.blink_flg = False if self.blink_flg else True

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 32, 30)

        # 三角カーソル
        if self.blink_flg:
            pyxel.blt(56 + self.cur[0] * 16, 104 + self.cur[1] * 16, 0, 96, 24, 8, 8)

        # 上段入力文字下のカーソル
        pyxel.blt(pwd_pos[self.pos][0], pwd_pos[self.pos][1] + 8, 0, 88, 16, 8, 8)

        # 入力したふっかつのじゅもん
        for i, p in enumerate(self.pwd):
            if p == -1:
                pyxel.blt(pwd_pos[i][0], pwd_pos[i][1], 0, 88, 24, 8, 8)
            else:
                pyxel.blt(pwd_pos[i][0], pwd_pos[i][1] - 8, 0, 0 + p %
                          10 * 8, 16 + p // 10 * 16, 8, 16)


App()
