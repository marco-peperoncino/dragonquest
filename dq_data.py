import math

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
    '”', '゜', '－', '　'
)

# 文字と文字コード対応表
str_code = {
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

# ぶき
weapon_list = (
    ('なし', 0),
    ('たけざお', 2),
    ('こんぼう', 4),
    ('どうのつるぎ', 10),
    ('てつのおの', 15),
    ('はがねのつるぎ', 20),
    ('ほのおのつるぎ', 28),
    ('ロトのつるぎ', 40),
)

# よろい
armor_list = (
    ('なし', 0),
    ('ぬののふく', 2),
    ('かわのふく', 4),
    ('くさりかたびら', 10),
    ('てつのよろい', 16),
    ('はがねのよろい', 24),
    ('まほうのよろい', 24),
    ('ロトのよろい', 28),
)

# たて
shield_list = (
    ('なし', 0),
    ('かわのたて', 4),
    ('てつのたて', 10),
    ('みかがみのたて', 20),
)

# アイテム
item_list = ('なし', 'たいまつ', 'せいすい', 'キメラのつばさ', 'りゅうのうろこ', 'ようせいのふえ', 'せんしのゆびわ', 'ロトのしるし',
             'おうじょのあい', 'のろいのベルト', 'ぎんのたてごと', 'しのくびかざり', 'たいようのいし', 'あまぐものつえ', 'にじのしずく')

# レベルとステータスの対応表 上位→下位
# ちから,すばやさ,HP,MP,必要EXP
lv_status = (
    (4, 4, 15, 0, 0),
    (5, 4, 22, 0, 7),
    (7, 6, 24, 5, 23),
    (7, 8, 31, 16, 47),
    (12, 10, 35, 20, 110),
    (16, 10, 38, 24, 220),
    (18, 17, 40, 26, 450),
    (22, 20, 46, 29, 800),
    (30, 22, 50, 36, 1300),
    (35, 31, 54, 40, 2000),
    (40, 35, 62, 50, 2900),
    (48, 40, 63, 58, 4000),
    (52, 48, 70, 64, 5500),
    (60, 55, 78, 70, 7500),
    (68, 64, 86, 72, 10000),
    (72, 70, 92, 95, 13000),
    (72, 78, 100, 100, 17000),
    (85, 84, 115, 108, 21000),
    (87, 86, 130, 115, 25000),
    (92, 88, 138, 128, 29000),
    (95, 90, 149, 135, 33000),
    (97, 90, 158, 146, 37000),
    (99, 94, 165, 153, 41000),
    (103, 98, 170, 161, 45000),
    (113, 100, 174, 161, 49000),
    (117, 105, 180, 168, 53000),
    (125, 107, 189, 175, 57000),
    (130, 115, 195, 180, 61000),
    (135, 120, 200, 190, 65000),
    (140, 130, 210, 200, 65535),
)

# キャラクターのタイプ表
# 名前ポイントを16で割った余りと配列のインデックスが対応
# HP, MP, ちから, すばやさ, ボーナスポイント
# ボーナスポイント以外は1が通常、0の場合ステータス×0.9+ボーナスポイント
chara_type = (
    (1, 1, 0, 0, 0),
    (1, 0, 1, 0, 0),
    (0, 1, 0, 1, 0),
    (0, 0, 1, 1, 0),
    (1, 1, 0, 0, 1),
    (1, 0, 1, 0, 1),
    (0, 1, 0, 1, 1),
    (0, 0, 1, 1, 1),
    (1, 1, 0, 0, 2),
    (1, 0, 1, 0, 2),
    (0, 1, 0, 1, 2),
    (0, 0, 1, 1, 2),
    (1, 1, 0, 0, 3),
    (1, 0, 1, 0, 3),
    (0, 1, 0, 1, 3),
    (0, 0, 1, 1, 3),
)


class SaveData:
    # 0
    # 1番目のアイテム 4bit 0～14
    # 2番目のアイテム 4bit 0～14

    # 1
    # フラグ せんしのゆびわを装備しているか 1bit
    # 名前2文字目 6bit 0～63
    # フラグ りゅうのうろこを装備したことがあるか 1bit

    # 2
    # 経験値上位 8bit

    # 3
    # 5番目のアイテム 4bit 0～14
    # 6番目のアイテム 4bit 0～14

    # 4
    # やくそう個数 4bit 0～6
    # かぎ個数 4bit 0～6

    # 5
    # ゴールド上位 8bit

    # 6
    # たて 2bit 0～3
    # よろい 3bit 0～7
    # ぶき 3bit 0～7

    # 7
    # 名前4文字目 6bit 0～63
    # フラグ ドラゴンを倒したか 1bit
    # 暗号化キー1 1bit

    # 8
    # 7番目のアイテム 4bit 0～14
    # 8番目のアイテム 4bit 0～14

    # 9
    # 暗号化キー2 1bit
    # フラグ ゴーレムを倒したか 1bit
    # 名前1文字目 6bit 0～63

    # 10
    # ゴールド下位 8bit

    # 11
    # 3番目のアイテム 4bit 0～14
    # 4番目のアイテム 4bit 0～14

    # 12
    # 名前3文字目 6bit 0～63
    # フラグ しのくびかざりを入手したことがあるか 1bit
    # 暗号化キー3 1bit

    # 13
    # 経験値下位 8bit

    # 14
    # CRC 8bit

    def __init__(self):

        # セーブデータ15byte分
        self.savedata = [0] * 15
        # ふっかつのじゅもん20文字分
        # けせいなの　へごべううつに　はほめよれ　よごぜ
        # self.word = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 0, 4, 8, 12, 16]
        # self.word = [8, 13, 1, 20, 24, 28, 48, 62, 2, 2, 17, 21, 25, 29, 36, 37, 41, 37, 48, 52]

        self.item = [0] * 8

    def crc(self):
        cd = 0x8000  # 1000 0000 0000 0000
        for i in range(15):
            for j in range(8):
                if cd & 0x8000:
                    cd = (cd << 1) ^ 0x1021  # 0001 0000 0010 0001
                else:
                    cd <<= 1

    def load(self, pswd):
        data = [0] * 20

        self.word = self.pswd_to_code(pswd)

        # self.word = self.pswd_to_code('おさべつにはほわげげだどべうきさそさには')
        # self.word = self.pswd_to_code('ふるいけやかわずとびこむみずのおとばしや')
        # self.word = self.pswd_to_code('ほりいゆうじえにつくすどらごくえすとだよ')
        # self.word = self.pswd_to_code('さいきようもちものですたあとしたいのだよ')
        # self.word = self.pswd_to_code('どらくえはねとげになつてつまらないあうと')
        # self.word = self.pswd_to_code('かそじへむるがむゆおふるがごぜづびちれぎ')

        self.decrypt(data)
        self.savedata = self.convert_6to8(data)

        self.name = self.get_name()
        self.exp = self.get_exp()
        self.level = self.get_level()
        self.gold = self.get_gold()
        self.weapon = self.get_weapon()
        self.armor = self.get_armor()
        self.shield = self.get_shield()
        self.herbs = self.get_herbs()
        self.keys = self.get_keys()
        self.item = self.get_item()
        self.flg = self.get_flg()
        self.get_status()

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

    # なまえ取得
    def get_name(self):
        name = name_code[(self.savedata[9] >> 2) & 0x3F]
        name += name_code[(self.savedata[1] >> 1) & 0x3F]
        name += name_code[self.savedata[12] & 0x3F]
        name += name_code[self.savedata[7] & 0x3F]
        return name

    # ゴールド取得
    def get_gold(self):
        return self.savedata[5] << 8 | self.savedata[10]

    # 経験値取得
    def get_exp(self):
        return self.savedata[2] << 8 | self.savedata[13]

    # ぶき取得
    def get_weapon(self):
        return (self.savedata[6] >> 5) & 0x07

    # よろい取得
    def get_armor(self):
        return (self.savedata[6] >> 2) & 0x07

    # たて取得
    def get_shield(self):
        return self.savedata[6] & 0x03

    # アイテム取得
    def get_item(self):
        item = [0] * 8
        item[0] = item_list[self.savedata[0] & 0x0F]
        item[1] = item_list[(self.savedata[0] >> 4) & 0x0F]
        item[2] = item_list[self.savedata[11] & 0x0F]
        item[3] = item_list[(self.savedata[11] >> 4) & 0x0F]
        item[4] = item_list[self.savedata[3] & 0x0F]
        item[5] = item_list[(self.savedata[3] >> 4) & 0x0F]
        item[6] = item_list[self.savedata[8] & 0x0F]
        item[7] = item_list[(self.savedata[8] >> 4) & 0x0F]
        return item

    # やくそう取得
    def get_herbs(self):
        return self.savedata[4] & 0x0F

    # かぎ取得
    def get_keys(self):
        return (self.savedata[4] >> 4) & 0x0F

    # フラグ
    def get_flg(self):
        flg = [0] * 5
        # せんしのゆびわを装備しているか
        flg[0] = self.savedata[1] & 0x01
        # りゅうのうろこを装備したことがあるか
        flg[1] = (self.savedata[1] >> 7) & 0x01
        # ドラゴンを倒したか
        flg[2] = (self.savedata[7] >> 6) & 0x01
        # ゴーレムを倒したか
        flg[3] = (self.savedata[9] >> 1) & 0x01
        # しのくびかざりを入手したことがあるか
        flg[4] = (self.savedata[12] >> 6) & 0x01
        return flg

    # レベル取得
    def get_level(self):
        for i, t in enumerate(tuple(reversed(lv_status))):
            if self.exp >= t[4]:
                break

        return 30 - i

    # HP, MP, ちから, すばやさを計算して設定
    def get_status(self):
        # まず名前点計算
        # 名前用文字コードを16で割った余りの合計
        point = 0
        for s in self.get_name():
            point += name_code.index(s) % 16

        # それぞれのスタータスの基本値をセット
        self.hp = lv_status[self.level - 1][2]
        self.mp = lv_status[self.level - 1][3]
        self.power = lv_status[self.level - 1][0]
        self.speed = lv_status[self.level - 1][1]

        # 名前点数のボーナス補正
        # 名前点数を更に16で割った余りがキャラクタータイプに対応
        point %= 16
        self.hp = self.hp if chara_type[point][0] else math.floor(
            self.hp * 0.9) + chara_type[point][4]
        self.mp = self.mp if chara_type[point][1] else math.floor(
            self.mp * 0.9) + chara_type[point][4]
        self.power = self.power if chara_type[point][2] else math.floor(
            self.power * 0.9) + chara_type[point][4]
        self.speed = self.speed if chara_type[point][3] else math.floor(
            self.speed * 0.9) + chara_type[point][4]

    # ふっかつのじゅもん文字列から文字コード表取得
    def pswd_to_code(self, pswd):
        code = []

        for s in pswd:
            code.append(str_code[s])

        return code
