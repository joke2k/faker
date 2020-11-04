from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{last_name}} {{first_name_female}}',
    )

    formats_male = (
        '{{last_name}} {{first_name_male}}',
    )

    formats = formats_male + formats_female

    # link: http://dic.nicovideo.jp/a/日本人の名前一覧
    # link: http://www.meijiyasuda.co.jp/enjoy/ranking/
    first_names_female = (
        '明美', 'あすか', '香織', '加奈', 'くみ子', 'さゆり', '知実', '千代',
        '直子', '七夏', '花子', '春香', '真綾', '舞', '美加子', '幹',
        '桃子', '結衣', '裕美子', '陽子', '里佳',
    )

    # link: http://dic.nicovideo.jp/a/日本人の名前一覧
    # link: http://www.meijiyasuda.co.jp/enjoy/ranking/
    first_names_male = (
        '晃', '篤司', '治', '和也', '京助', '健一', '修平', '翔太',
        '淳', '聡太郎', '太一', '太郎', '拓真', '翼', '智也', '直樹',
        '直人', '英樹', '浩', '学', '充', '稔', '裕樹', '裕太',
        '康弘', '陽一', '洋介', '亮介', '涼平', '零',
    )

    first_names = first_names_male + first_names_female

    # based on: https://www2.nipponsoft.co.jp/bldoko/index.asp
    last_names = OrderedDict((
        ("佐藤", 366803),
        ("鈴木", 321135),
        ("高橋", 266782),
        ("田中", 245821),
        ("伊藤", 203357),
        ("渡辺", 200504),
        ("山本", 200134),
        ("中村", 195219),
        ("小林", 191819),
        ("加藤", 160283),
        ("吉田", 154461),
        ("山田", 151675),
        ("佐々木", 135927),
        ("山口", 119501),
        ("松本", 116490),
        ("井上", 111287),
        ("木村", 107446),
        ("林", 101826),
        ("斎藤", 101774),
        ("清水", 97826),
        ("山崎", 90781),
        ("阿部", 86833),
        ("森", 86507),
        ("池田", 84860),
        ("橋本", 82836),
        ("山下", 80588),
        ("石川", 77471),
        ("中島", 74106),
        ("前田", 72930),
        ("藤田", 72375),
        ("後藤", 71629),
        ("小川", 71179),
        ("岡田", 70347),
        ("長谷川", 69201),
        ("村上", 68606),
        ("近藤", 68297),
        ("石井", 67079),
        ("遠藤", 62620),
        ("斉藤", 62540),
        ("坂本", 62308),
        ("青木", 59516),
        ("藤井", 59204),
        ("西村", 58821),
        ("福田", 58714),
        ("太田", 58439),
        ("三浦", 58006),
        ("藤原", 57742),
        ("松田", 55883),
        ("岡本", 55539),
        ("中川", 55221),
    ))

    kana_formats = (
        '{{last_kana_name}} {{first_kana_name_female}}',
        '{{last_kana_name}} {{first_kana_name_male}}',
    )

    first_kana_names_female = (
        'アケミ', 'アスカ', 'カオリ', 'カナ',
        'クミコ', 'サユリ', 'サトミ', 'チヨ',
        'ナオコ', 'ナナミ', 'ハナコ', 'ハルカ',
        'マアヤ', 'マイ', 'ミカコ', 'ミキ',
        'モモコ', 'ユイ', 'ユミコ', 'ヨウコ',
        'リカ',
    )

    first_kana_names_male = (
        'アキラ', 'アツシ', 'オサム', 'カズヤ',
        'キョウスケ', 'ケンイチ', 'シュウヘイ', 'ショウタ',
        'ジュン', 'ソウタロウ', 'タイチ', 'タロウ',
        'タクマ', 'ツバサ', 'トモヤ', 'ナオキ',
        'ナオト', 'ヒデキ', 'ヒロシ', 'マナブ',
        'ミツル', 'ミノル', 'ユウキ', 'ユウタ',
        'ヤスヒロ', 'ヨウイチ', 'ヨウスケ', 'リョウスケ',
        'リョウヘイ', 'レイ',
    )

    first_kana_names = first_kana_names_male + first_kana_names_female

    last_kana_names = (
        'アオタ', 'アオヤマ', 'イシダ', 'イダカ',
        'イトウ', 'イノウエ', 'ウノ', 'エコダ',
        'オオガキ', 'カトウ', 'カノウ', 'キジマ',
        'キムラ', 'キリヤマ', 'クドウ', 'コイズミ',
        'コバヤシ', 'コンドウ', 'サイトウ', 'サカモト',
        'ササキ', 'サトウ', 'ササダ', 'スズキ',
        'スギヤマ', 'タカハシ', 'タナカ', 'タナベ',
        'ツダ', 'ナカジマ', 'ナカムラ', 'ナギサ',
        'ナカツガワ', 'ニシノソノ', 'ノムラ', 'ハラダ',
        'ハマダ', 'ヒロカワ', 'フジモト', 'マツモト',
        'ミヤケ', 'ミヤザワ', 'ムラヤマ', 'ヤマギシ',
        'ヤマグチ', 'ヤマダ', 'ヤマモト', 'ヨシダ',
        'ヨシモト', 'ワカマツ', 'ワタナベ',
    )

    romanized_formats = (
        '{{first_romanized_name_female}} {{last_romanized_name}}',
        '{{first_romanized_name_male}} {{last_romanized_name}}',
    )

    first_romanized_names_female = (
        'Akemi', 'Asuka', 'Kaori', 'Kana',
        'Kumiko', 'Sayuri', 'Satomi', 'Chiyo',
        'Naoko', 'Nanami', 'Hanako', 'Haruka',
        'Maaya', 'Mai', 'Mikako', 'Miki',
        'Momoko', 'Yui', 'Yumiko', 'Yoko',
        'Rika',
    )

    first_romanized_names_male = (
        'Akira', 'Atsushi', 'Osamu', 'Kazuya',
        'Kyosuke', 'Kenichi', 'Shohei', 'Shota',
        'Jun', 'Sotaro', 'Taichi', 'Taro',
        'Takuma', 'Tsubasa', 'Tomoya', 'Naoki',
        'Naoto', 'Hideki', 'Hiroshi', 'Manabu',
        'Mituru', 'Minoru', 'Yuki', 'Yuta',
        'Yasuhiro', 'Yoichi', 'Yosuke', 'Ryosuke',
        'Ryohei', 'Rei',
    )

    first_romanized_names = first_romanized_names_male \
        + first_romanized_names_female

    last_romanized_names = (
        'Aota', 'Aoyama', 'Ishida', 'Idaka',
        'Ito', 'Inoue', 'Uno', 'Ekoda',
        'Ogaki', 'Kato', 'Kano', 'Kijima',
        'Kimura', 'Kiriyama', 'Kudo', 'Koizumi',
        'Kobayashi', 'Kondo', 'Saito', 'Sakamoto',
        'Sasaki', 'Sato', 'Sasada', 'Suzuki',
        'Sugiyama', 'Takahashi', 'Tanaka', 'Tanabe',
        'Tsuda', 'Nakajima', 'Nakamura', 'Nagisa',
        'Nakatsugawa', 'Nishinosono', 'Nomura', 'Harada',
        'Hamada', 'Hirokawa', 'Fujimoto', 'Matsumoto',
        'Miyake', 'Miyagawa', 'Murayama', 'Yamagishi',
        'Yamaguchi', 'Yamada', 'Yamamoto', 'Yoshida',
        'Yoshimoto', 'Wakamatsu', 'Watanabe',
    )

    def kana_name(self):
        '''
        @example 'アオタ アキラ'
        '''
        pattern = self.random_element(self.kana_formats)
        return self.generator.parse(pattern)

    def first_kana_name(self):
        '''
        @example 'アキラ'
        '''
        return self.random_element(self.first_kana_names)

    def first_kana_name_female(self):
        return self.random_element(self.first_kana_names_female)

    def first_kana_name_male(self):
        return self.random_element(self.first_kana_names_male)

    def last_kana_name(self):
        '''
        @example 'アオタ'
        '''
        return self.random_element(self.last_kana_names)

    def romanized_name(self):
        '''
        @example 'Akira Aota'
        '''
        pattern = self.random_element(self.romanized_formats)
        return self.generator.parse(pattern)

    def first_romanized_name(self):
        '''
        @example 'Akira'
        '''
        return self.random_element(self.first_romanized_names)

    def first_romanized_name_female(self):
        return self.random_element(self.first_romanized_names_female)

    def first_romanized_name_male(self):
        return self.random_element(self.first_romanized_names_male)

    def last_romanized_name(self):
        '''
        @example 'Aota'
        '''
        return self.random_element(self.last_romanized_names)
