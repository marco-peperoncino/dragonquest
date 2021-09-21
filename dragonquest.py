# ドラゴンクエスト ふっかつのじゅもん
# 下記のページを大いに参考にさせていただいております。
# https://qiita.com/yoshi389111/items/29ade2f62483e9c095d9
# https://oscdis.hatenablog.com/entry/2014/03/30/225043
# https://kyokugen.info/dq1/


import pyxel
import dq_sub
import dq_data

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

        self.save_data = dq_data.SaveData()
        self.save_data.load()

        pyxel.init(256, 240, caption='Dragon Quest ～ふっかつのじゅもん～')
        pyxel.load('my_resource.pyxres')

        self.win = dq_sub.Window(0, 32, 32, 8, 12, self.save_data.name)
        self.win.set_text(1, 2, 'レベル'+str(self.save_data.level).rjust(3))
        self.win.set_text(1, 4, 'HP '+str(self.save_data.hp).rjust(3))
        self.win.set_text(1, 6, 'MP '+str(self.save_data.mp).rjust(3))
        self.win.set_text(1, 8, 'G'+str(self.save_data.gold).rjust(5))
        self.win.set_text(1, 10, 'E'+str(self.save_data.exp).rjust(5))

        self.win2 = dq_sub.Window(1, 96, 48, 14, 22, 'つよさ')
        self.win2.set_text(4, 2, 'レベル:'+str(self.save_data.level).rjust(4))
        self.win2.set_text(4, 4, 'ちから:'+str(self.save_data.power).rjust(4))
        self.win2.set_text(3, 6, 'すばやさ:'+str(self.save_data.speed).rjust(4))
        self.win2.set_text(1, 8, 'さいだいHP:'+str(self.save_data.hp).rjust(4))
        self.win2.set_text(1, 10, 'さいだいMP:'+str(self.save_data.mp).rjust(4))
        self.win2.set_text(
            2, 12, 'こうげき力:'+str(self.save_data.power+dq_data.weapon_list[self.save_data.weapon][1]))
        self.win2.set_text(3, 14, 'しゅび力:'+str(self.save_data.speed//2 +
                                              dq_data.armor_list[self.save_data.armor][1] +
                                              dq_data.shield_list[self.save_data.shield][1] +
                                              self.save_data.flg[1]*2))
        self.win2.set_text(3, 16, 'ぶき:'+dq_data.weapon_list[self.save_data.weapon][0])
        self.win2.set_text(2, 18, 'よろい:'+dq_data.armor_list[self.save_data.armor][0])
        self.win2.set_text(3, 20, 'たて:'+dq_data.shield_list[self.save_data.shield][0])

        self.win.state = dq_sub.WINDOW_STATE_HIDE
        self.win2.state = dq_sub.WINDOW_STATE_HIDE

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

            print(pyxel.tilemap(0).get(self.cur[0] + 1, self.cur[1]))

            # if self.win2.state == dq_sub.WINDOW_STATE_SHOW or self.win2.state == dq_sub.WINDOW_STATE_OPEN:
            #     self.win2.state = dq_sub.WINDOW_STATE_CLOSE
            # elif self.win2.state == dq_sub.WINDOW_STATE_HIDE or self.win2.state == dq_sub.WINDOW_STATE_CLOSE:
            #     self.win2.state = dq_sub.WINDOW_STATE_OPEN

            # for p in self.pwd:
            #     print(f'{p}, ', end='')
            # print('')

        # カーソルを点滅させる
        if pyxel.frame_count % 4 == 0:
            self.blink_flg = False if self.blink_flg else True

        self.win.update()
        self.win2.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 32, 30)

        # 三角カーソル
        if self.blink_flg:
            pyxel.blt(56 + self.cur[0] * 16, 104 + self.cur[1] * 16, 0, 0, 24, 8, 8)

        # 上段入力文字下のカーソル
        pyxel.blt(pwd_pos[self.pos][0], pwd_pos[self.pos][1] + 8, 0, 16, 32, 8, 8)

        # 入力したふっかつのじゅもん
        for i, p in enumerate(self.pwd):
            if p == -1:
                pyxel.blt(pwd_pos[i][0], pwd_pos[i][1], 0, 248, 16, 8, 8)
            else:
                pyxel.blt(pwd_pos[i][0], pwd_pos[i][1] - 8, 0, 0 + p %
                          32 * 8, 16 + p // 32 * 16, 8, 16)

        self.win.disp()
        self.win2.disp()


App()
