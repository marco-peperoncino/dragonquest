import pyxel


class App:
    def __init__(self):
        self.pos = 0  # 上段の入力した文字が表示されている所のカーソル位置
        self.cur = [0, 0]  # 下段の文字を選択する所のカーソル位置 [x, y]
        self.pwd = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -
                    1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.blink_flg = True

        pyxel.init(256, 240, caption='Dragon Quest')
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

        # カーソルを点滅させる
        if pyxel.frame_count % 4 == 0:
            self.blink_flg = False if self.blink_flg else True

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 32, 30)

        # 三角カーソル
        if self.blink_flg:
            pyxel.blt(56 + self.cur[0] * 16, 104 + self.cur[1] * 16, 0, 96, 24, 8, 8)

        pyxel.blt(64, 56, 0, 88, 16, 8, 8)

        # 入力したふっかつのじゅもん
        for i, p in enumerate(self.pwd):
            if p == -1:
                dx = 64 + i % 12 * 8
                if (i <= 11 and i >= 5) or i >= 17:
                    dx += 8
                pyxel.blt(dx, 48 + i // 12 * 24, 0, 88, 24, 8, 8)


App()
