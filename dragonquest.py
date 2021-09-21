# ドラゴンクエスト ふっかつのじゅもん
# 下記のページを大いに参考にさせていただいております。
# https://qiita.com/yoshi389111/items/29ade2f62483e9c095d9
# https://oscdis.hatenablog.com/entry/2014/03/30/225043
# https://kyokugen.info/dq1/


import pyxel
import dq_sub
import dq_data

SCENE_PASSWORD = 0
SCENE_DISP = 1

# 文字
str_list = (
    'あ', 'い', 'う', 'え', 'お', 'ま', 'み', 'む', 'め', 'も',
    'か', 'き', 'く', 'け', 'こ', 'が', 'ぎ', 'ぐ', 'げ', 'ご',
    'さ', 'し', 'す', 'せ', 'そ', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
    'た', 'ち', 'つ', 'て', 'と', 'だ', 'ぢ', 'づ', 'で', 'ど',
    'な', 'に', 'ぬ', 'ね', 'の', 'ら', 'り', 'る', 'れ', 'ろ',
    'は', 'ひ', 'ふ', 'へ', 'ほ', 'ば', 'び', 'ぶ', 'べ', 'ぼ',
    'や', 'ゆ', 'よ', 'わ',
)


# 入力した文字が表示される所の座標
str_pos = (
    (64, 48), (72, 48), (80, 48), (88, 48), (96, 48),
    (112, 48), (120, 48), (128, 48), (136, 48), (144, 48),
    (152, 48), (160, 48), (64, 72), (72, 72), (80, 72),
    (88, 72), (96, 72), (112, 72), (120, 72), (128, 72)
)


class App:
    def __init__(self):

        self.scene = SCENE_PASSWORD

        # 上段の入力した文字が表示されている所のカーソル位置
        self.pos = 0
        # 下段の文字を選択する所のカーソル位置 [x, y]
        self.cur = [0, 0]
        # 入力した文字
        # self.pwd = [0] * 20
        # self.pwd = list('ふるいけやかわずとびこむみずのおとばしや')
        # self.pwd = list('ほりいゆうじえにつくすどらごくえすとだよ')
        # self.pwd = list('さいきようもちものですたあとしたいのだよ')
        self.pwd = list('どらくえはねとげになつてつまらないあうと')

        # カーソルを点滅させるためのフラグ
        self.blink_flg = True

        pyxel.init(256, 240, caption='Dragon Quest ～ふっかつのじゅもん～')
        pyxel.load('my_resource.pyxres')

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.scene == SCENE_PASSWORD:
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
                    self.pwd[self.pos] = str_list[cur_pos]
                    if self.pos < 19:
                        self.pos += 1
                    elif self.pos == 19:
                        self.complete()

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
                    self.complete()

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

        elif self.scene == SCENE_DISP:
            self.win.update()
            self.win2.update()

    def draw(self):
        pyxel.cls(0)

        if self.scene == SCENE_PASSWORD:
            pyxel.bltm(0, 0, 0, 0, 0, 32, 30)

            # 三角カーソル
            if self.blink_flg:
                pyxel.blt(56 + self.cur[0] * 16, 104 + self.cur[1] * 16, 0, 0, 24, 8, 8)

            # 上段入力文字下のカーソル
            pyxel.blt(str_pos[self.pos][0], str_pos[self.pos][1] + 8, 0, 16, 32, 8, 8)

            # 入力したふっかつのじゅもん
            for i, p in enumerate(self.pwd):
                if p == 0:
                    dq_sub.text(str_pos[i][0], str_pos[i][1], '*')
                else:
                    dq_sub.text(str_pos[i][0], str_pos[i][1], self.pwd[i])

        elif self.scene == SCENE_DISP:
            self.win.disp()
            self.win2.disp()

    def complete(self):
        self.save_data = dq_data.SaveData()
        self.save_data.load(''.join(self.pwd))
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
            2, 12, 'こうげき力:'+str(self.save_data.power+dq_data.weapon_list[self.save_data.weapon][1]).rjust(4))
        self.win2.set_text(3, 14, 'しゅび力:'+str(self.save_data.speed//2 +
                                              dq_data.armor_list[self.save_data.armor][1] +
                                              dq_data.shield_list[self.save_data.shield][1] +
                                              self.save_data.flg[1]*2).rjust(4))
        self.win2.set_text(
            3, 16, 'ぶき:'+dq_data.weapon_list[self.save_data.weapon][0])
        self.win2.set_text(
            2, 18, 'よろい:'+dq_data.armor_list[self.save_data.armor][0])
        self.win2.set_text(
            3, 20, 'たて:'+dq_data.shield_list[self.save_data.shield][0])

        self.scene = SCENE_DISP


App()
