# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_suffixes = ('ск', 'вль', 'град', 'поль', 'ин', 'ов', 'бург')
    street_suffixes = ('ул.', 'алл.', 'наб.', 'пр.', 'пер.', 'бул.', 'ш.')
    region_suffixes = ('респ.', 'обл.', 'край', 'АО')
    city_formats = ('{{city_prefix}} {{city_name}}', )
    street_address_formats = ('{{street_name}}, д. {{building_number}}',
                              '{{street_name}}, д. {{building_number}} к. {{building_number}}',
                              '{{street_name}}, д. {{building_number}} стр. {{building_number}}')
    address_formats = ('{{city}}, {{street_address}}, {{postcode}}', )
    postcode_formats = ('######',)
    building_number_formats = ('###', '##', '#', '#/#')

    city_prefixes = ('г.', 'п.', 'к.', 'с.', 'д.', 'клх', 'ст.')

    street_suffixes_masc = ('пр.', 'пер.', 'бул.')
    street_suffixes_fem = ('ул.', 'алл.', 'наб.')
    street_suffixes_neu = ('ш.', )

    street_titles = (
        'Советская', 'Молодежная', 'Центральная', 'Школьная', 'Новая',
        'Садовая', 'Лесная', 'Набережная', 'Октябрьская', 'Зеленая',
        'Комсомольская', 'Заречная', 'Первомайская', 'Полевая', 'Луговая',
        'Пионерская', 'Юбилейная', 'Северная', 'Пролетарская', 'Степная',
        'Южная', 'Колхозная', 'Рабочая', 'Солнечная', 'Железнодорожная',
        'Восточная', 'Заводская', 'Нагорная', 'Береговая', 'Кооперативная',
        'Красноармейская', 'Совхозная', 'Речная', 'Спортивная', 'Озерная',
        'Строительная', 'Парковая', 'Подгорная', 'Почтовая', 'Партизанская',
        'Вокзальная', 'Дорожная', 'Дачная', 'Западная', 'Московская',
        'Красная', 'Трудовая', 'Шоссейная', 'Коммунистическая', 'Сосновая',
        'Клубная', 'Березовая', 'Больничная', 'Интернациональная', 'Цветочная',
        'Трактовая', 'Горная', 'Весенняя', 'Коммунальная', 'Майская',
        'Привокзальная', 'Таежная', 'Транспортная', 'Овражная', 'Светлая',
        'Вишневая', 'Ключевая', 'Песчаная', 'Ленинградская', 'Профсоюзная',
        'Верхняя', 'Ленинская', 'Кирпичная', 'Мостовая', 'Станционная',
        'Уральская', 'Линейная', 'Фабричная', 'Магистральная', 'Сибирская',
        'Крестьянская', 'Российская', 'Тихая', 'Широкая', 'Нижняя',
        'Народная', 'Промышленная', 'Кольцевая', 'Дальняя', 'Базарная',
        'Целинная', 'Родниковая', 'Революционная', 'Социалистическая', 'Звездная',
        'Студенческая', 'Мирная', 'Кубанская', 'Гаражная', 'Фестивальная',
        'Гражданская', 'Песочная', 'Сиреневая', 'Сельская', 'Кузнечная',
        'Пушкинская', 'Крайняя', 'Гвардейская', 'Веселая', 'Загородная',
        'Олимпийская', 'Приозерная', 'Рябиновая', 'Заозерная', 'Боровая',
        'Урожайная', 'Торговая', 'Донская', 'Пограничная', 'Огородная',
        'Пригородная', 'Стадионная', 'Виноградная', 'Киевская', 'Индустриальная',
        'Красногвардейская', 'Волжская', 'Свободная', 'Кедровая', 'Подлесная',
        'Полярная', 'Раздольная', 'Карьерная', 'Мельничная', 'Украинская',
        'Шахтерская', 'Запрудная', 'Элеваторная', 'Театральная', 'Геологическая',
        'Болотная', 'Придорожная', 'Кленовая', 'Казачья', 'Малая',
        'Морская', 'Волгоградская', 'Средняя', 'Безымянная', 'Краснофлотская',
        'Братская', 'Тенистая', 'Учительская', 'Кавказская', 'Короткая',
        'Деповская', 'Амурская', 'Сенная', 'Поселковая', 'Прудовая',
        'Депутатская', 'Авиационная', 'Аэродромная', 'Большая', 'Приморская',
        'Алтайская', 'Тополиная', 'Ростовская', 'Тракторная', 'Мелиоративная',
        'Ольховая', 'Славянская', 'Радужная', 'Краснодарская', 'Стахановская',
        'Ярославская', 'Коллективная', 'Ангарская', 'Локомотивная', 'Ягодная',
        'Смоленская', 'Тепличная', 'Водопроводная', 'Республиканская', 'Осенняя',
        'Байкальская', 'Саратовская', 'Казанская', 'Воронежская', 'Брянская',
        'Производственная', 'Техническая', 'Енисейская', 'Севастопольская', 'Окружная',
        'Орловская', 'Хуторская', 'Тупиковая', 'Каштановая', 'Омская',
        'Привольная', 'Курортная', 'Ивановская', 'Выгонная', 'Крымская',
        'Путейская', 'Проезжая', 'Краснознаменная', 'Одесская', 'Логовая',
        'Высокая', 'Ясная', 'Портовая', 'Снежная', 'Санаторная',
        'Союзная', 'Ульяновская', 'Сахалинская', 'Горняцкая', 'Прибрежная',
        'Рыбацкая', 'Полтавская', 'Тамбовская', 'Красноярская', 'Новосельская',
        'Проточная', 'Черноморская', 'Минская', 'Главная', 'Вольная',
        'Хвойная', 'Космическая', 'Моховая', 'Курская', 'Курганная',
        'Угловая', 'Камская', 'Инженерная', 'Лесозаводская', 'Астраханская',
        'Белорусская', 'Заовражная', 'Азовская', 'Ручейная', 'Волочаевская',
        'Ставропольская', 'Слободская', 'Тульская', 'Харьковская', 'Петровская',
        'Владимирская', 'Высоковольтная', 'Лазурная', 'Покровская', 'Новгородская',
        'Ленская', 'Сплавная', 'Ударная', 'Калужская', 'Прудная',
        'Краснопартизанская', 'Ореховая', 'Таманская', 'Иркутская', 'Отрадная',
        'Большевистская', 'Троицкая', 'Лесхозная', 'Васильковая', 'Механическая',
        'Путевая', 'Кузнецкая', 'Физкультурная', 'Черемуховая', 'Флотская',
        'Угольная', 'Просторная', 'Поперечная', 'Городская', 'Абрикосовая',
        'Бульварная', 'Прохладная', 'Томская', 'Энергетическая', 'Литейная',
        'Медицинская', 'Заливная', 'Бригадная', 'Детская', 'Запорожская',
        'Дальневосточная', 'Балтийская', 'Февральская', 'Лунная', 'Высотная',
        'Рязанская', 'Малиновая',

    )

    street_titles_noflex = (
        'Ленина', 'Мира', 'Гагарина', 'Кирова', 'Пушкина', 'Калинина',
        'Чапаева', 'Строителей', 'Победы', 'Горького', 'Чкалова',
        'Мичурина', 'Дружбы', 'Лермонтова', 'Свободы', 'Маяковского',
        'Фрунзе', 'Дзержинского', 'Свердлова', 'Некрасова', 'Гоголя',
        'Чехова', 'Труда', 'Комарова', 'Матросова', 'Островского',
        'Куйбышева', 'Крупской', 'Карла Маркса', '8 Марта', 'Суворова',
        'Ломоносова', 'Космонавтов', 'Энергетиков', 'Шевченко', 'Механизаторов',
        '40 лет Победы', 'Энгельса', 'Чернышевского', 'Урицкого', 'Ворошилова',
        'Тургенева', 'Толстого', 'Буденного', 'Орджоникидзе', 'Герцена',
        'Щорса', 'Луначарского', 'Энтузиастов', 'Титова', 'Лазо',
        '50 лет Октября', 'Пугачева', 'Володарского', 'Кутузова', 'Чайковского',
        'Мелиораторов', 'Новоселов', 'Белинского', 'Тельмана', 'Тимирязева',
        'Котовского', '60 лет Октября', 'Есенина', 'К.Маркса', '40 лет Октября',
        'Крылова', 'Декабристов', '70 лет Октября', 'Фурманова', 'Гайдара',
        'Терешковой', 'Ватутина', 'Коммунаров', 'Гастелло', 'Жданова',
        'Радищева', 'Нефтяников', 'Осипенко', 'Нахимова', 'Жукова',
        'Павлова', 'Степана Разина', 'Попова', 'Жуковского', 'Королева',
        'Грибоедова', 'Менделеева', 'Достоевского', 'Репина', 'Циолковского',
        'Воровского', 'Максима Горького', 'Революции', 'Кошевого', 'Пархоменко',
        'Серова', 'Добролюбова', '50 лет Победы', 'Красина', 'Коминтерна',
        '30 лет Победы', 'Разина', 'Черняховского', 'Ветеранов', 'Пирогова',
        'Льва Толстого', 'Геологов', 'Димитрова', 'М.Горького', 'Розы Люксембург',
        'Маркса', 'Ушакова', 'Юности', 'Короленко', 'Шолохова',
        '50 лет ВЛКСМ', 'Черемушки', 'Кольцова', 'Плеханова', 'Макаренко',
        'Глинки', 'Специалистов', 'Халтурина', 'Морозова', 'Коммуны',
        'Красных Партизан', 'Зои Космодемьянской', 'Карбышева', 'Баумана', 'Марта 8',
        'Правды', 'Маркса Карла', 'Фадеева', '60 лет СССР', 'Челюскинцев',
        'Олега Кошевого', 'Новостройка', 'Шмидта', 'Кузнецова', 'Войкова',
        'Панфилова', 'Карла Либкнехта', 'Парижской Коммуны', 'Автомобилистов', 'Космодемьянской',
        'Седова', 'Блюхера', 'Демьяна Бедного', 'Спартака', 'Николаева',
        'Бабушкина', 'Октября', 'Щетинкина', 'Гончарова', 'Щербакова',
        'Азина', 'Сурикова', '9 Января', 'Подстанция', 'Волкова',
        'Никитина', 'Рылеева', 'Химиков', 'Курчатова', 'Микрорайон',
        'Докучаева', 'Просвещения', 'Смирнова', 'Макарова', 'Иванова',
        'Л.Толстого', 'Гафури', 'Высоцкого', 'Бажова', 'Кочубея',
        'Леонова', 'Надежды', 'Металлистов', 'Вавилова', 'Ульянова',
        'Павлика Морозова', 'Семашко', 'Шаумяна', 'Чайкиной', 'Ермака',
        'Дорожников', 'Советской Армии', 'Монтажников', 'Шишкина', 'Металлургов',
        'Беляева', 'Дружба', 'Серафимовича', 'Ильича', 'Мусы Джалиля',
        'Невского', 'Клары Цеткин', 'Леваневского', 'Водников', 'Вахитова',
        'Станиславского', 'Советов', 'Восьмого Марта', 'Пожарского', 'Папанина',
        'Победа', '8-е Марта', 'Журавлева', 'Культуры', 'Мая 1',
        'Минина', 'Машиностроителей', 'ДОС', 'Тюленина', 'Громова',
        'О.Кошевого', 'Р.Люксембург', 'Толбухина', 'Дарвина', 'З.Космодемьянской',
        '1 Мая', '9 мая', 'Тукая',
    )

    street_titles_irregular_masc = (
        'Полевой', 'Луговой', 'Степной', 'Заводской', 'Береговой',
        'Речной', 'Трудовой', 'Ключевой', 'Мостовой', 'Кольцевой',
        'Боровой', 'Донской', 'Морской', 'Сенной', 'Прудовой',
        'Большрй', 'Окружной', 'Хуторской', 'Логовой', 'Моховой',
        'Угловой', 'Слободской', 'Путевой', 'Городской', 'Рабочий',
        'Верхний', 'Тихий', 'Широкий', 'Нижний', 'Дальний',
        'Крайний', 'Казачий', 'Весенний', 'Средний', 'Короткий',
        'Осенний', 'Проезжий', 'Высокий',
    )

    street_titles_irregular_neu = (
        'Весеннее', 'Верхнее', 'Нижнее', 'Среднее', 'Дальнее',
        'Крайнее', 'Казачье', 'Рабочее', 'Осеннее', 'Проезжее',
    )

    city_names = (
        'Абакан', 'Абинск', 'Агата', 'Агинское (Забайк.)', 'Адлер', 'Адыгейск',
        'Азов (Рост.)', 'Алагир', 'Алапаевск', 'Алдан', 'Александров',
        'Александров Гай', 'Александровск', 'Александровск-Сахалинский',
        'Алексин', 'Амдерма', 'Амурск', 'Анадырь', 'Анапа', 'Ангарск',
        'Андреаполь', 'Анива', 'Апатиты', 'Апрелевка', 'Апшеронск', 'Аргаяш',
        'Ардон', 'Арзамас', 'Армавир', 'Арсеньев', 'Артем', 'Архангельск',
        'Архыз', 'Аршан (Бурят.)', 'Асбест', 'Асино', 'Астрахань', 'Ахтубинск',
        'Ачинск', 'Ачхой Мартан', 'Аша', 'Бавлы', 'Байкальск', 'Баксан',
        'Балашиха', 'Балашов', 'Балтийск', 'Баргузин', 'Барнаул', 'Батайск',
        'Белгород', 'Белогорск (Амур.)', 'Белокуриха', 'Беломорск', 'Белорецк',
        'Белореченск', 'Белоярский', 'Белый Яр (Томск.)', 'Березники',
        'Беслан', 'Бийск', 'Билибино', 'Биробиджан', 'Бирск',
        'Благовещенск (Амур.)', 'Богучар', 'Бодайбо', 'Бологое', 'Бомнак',
        'Борзя', 'Боровск', 'Братск', 'Бреды', 'Бронницы', 'Брянск',
        'Бугульма', 'Бугуруслан', 'Буденновск', 'Бузулук', 'Буйнакск',
        'Быково (метеост.)', 'Валаам', 'Валдай', 'Ведено', 'Великие Луки',
        'Великий Устюг', 'Вендинга', 'Верещагино (Перм.)', 'Верхнее Пенжино',
        'Верхний Баскунчак', 'Верхний Тагил', 'Верхний Уфалей', 'Верхотурье',
        'Верхоянск', 'Видное', 'Вилюйск', 'Витим', 'Владивосток',
        'Владикавказ', 'Владимир', 'Внуково (метеост.)', 'Волгоград',
        'Волгодонск', 'Вологда', 'Волоколамск', 'Волхов', 'Воркута',
        'Воронеж', 'Воскресенск', 'Воткинск', 'Всеволожск', 'Вуктыл', 'Выборг',
        'Вытегра', 'Вязьма', 'Гаврилов-Ям', 'Гагарин', 'Галич', 'Гатчина',
        'Гдов', 'Геленджик', 'Глазов', 'Голицыно', 'Горно-Алтайск',
        'Городовиковск', 'Горячий Ключ', 'Горячинск', 'Гремячинск (Бурят.)',
        'Гремячинск (Перм.)', 'Грозный', 'Губаха', 'Губкин', 'Губкинский',
        'Гудермес', 'Гусь-Хрустальный', 'Дагомыс', 'Далматово', 'Данков',
        'Двинской', 'Дербент', 'Джейрах', 'Джубга', 'Дзержинск', 'Дивногорск',
        'Диксон', 'Дмитров', 'Дно', 'Добрянка', 'Долинск', 'Домбай',
        'Домодедово', 'Дубна', 'Дудинка', 'Егорьевск', 'Ейск', 'Екатеринбург',
        'Елабуга', 'Елатьма', 'Елец', 'Ельня', 'Енисейск', 'Ербогачен',
        'Ершов', 'Ессентуки', 'Железногорск(Курск.)', 'Жиганск', 'Жигулевск',
        'Жуковский', 'Забайкальск', 'Заводоуковск', 'Завьялиха', 'Зарайск',
        'Звенигород', 'Зеленогорск (Ленин.)', 'Зеленоград', 'Златоуст',
        'Змеиногорск', 'Иваново', 'Ивдель', 'Игарка', 'Игнашино', 'Ижевск',
        'Избербаш', 'Инта', 'Ирбит', 'Иркутск', 'Истра', 'Ишим', 'Йошкар-Ола',
        'Кабанск', 'Кажим', 'Казань', 'Калач', 'Калач-на-Дону', 'Калачинск',
        'Калевала', 'Калининград', 'Калуга', 'Калязин', 'Каменномостский',
        'Каменск-Уральский', 'Каменск-Шахтинский', 'Камень-на-Оби', 'Камышин',
        'Камышлов', 'Кандалакша', 'Каневская', 'Канск', 'Карабудахкент',
        'Карабулак', 'Карачаевск', 'Каргасок', 'Каргополь', 'Карпинск',
        'Карталы', 'Касимов', 'Каспийск', 'Катав-Ивановск', 'Катайск',
        'Качканар', 'Кашира', 'Кашхатау', 'Кедровый', 'Кежма', 'Кемерово',
        'Кетченеры', 'Кижи', 'Кизел', 'Кизилюрт', 'Кизляр', 'Кимры',
        'Кингисепп', 'Кинешма', 'Киренск', 'Киржач', 'Кириши', 'Киров (Вятка)',
        'Кирово-Чепецк', 'Кировск (Мурм.)', 'Кировск (Ленин.)', 'Кисловодск',
        'Клин', 'Ковров', 'Когалым', 'Коломна', 'Колпашево',
        'Комсомольск-на-Амуре', 'Кондопога', 'Королев', 'Корсаков',
        'Костомукша', 'Кострома', 'Котельнич', 'Котлас', 'Кош-Агач',
        'Красная Поляна', 'Красновишерск', 'Красногорск (Моск.)', 'Краснодар',
        'Краснокамск', 'Красноселькуп', 'Краснотурьинск', 'Красноуральск',
        'Красноуфимск', 'Красноярск', 'Кропоткин (Краснод.)', 'Крымск',
        'Кудымкар', 'Кузнецк', 'Кулу', 'Кулунда', 'Кунгур', 'Курган',
        'Курганинск', 'Курильск', 'Курск', 'Куртамыш', 'Курумкан', 'Курчатов',
        'Кущевская', 'Кызыл', 'Кырен', 'Кыштым', 'Кяхта', 'Лабинск',
        'Лабытнанги', 'Лагань', 'Лазаревское', 'Лесной (Сверд.)', 'Липецк',
        'Листвянка (Иркут.)', 'Лодейное Поле', 'Лотошино', 'Луга', 'Луховицы',
        'Лысьва', 'Льгов', 'Любань', 'Люберцы', 'Лянтор', 'Магадан', 'Магас',
        'Магнитогорск', 'Майкоп', 'Макаров', 'Макушино', 'Малая Вишера',
        'Малгобек', 'Малоярославец', 'Махачкала', 'Медногорск',
        'Междуреченский', 'Мезень', 'Мелеуз', 'Меренга', 'Миасс',
        'Миллерово', 'Минеральные Воды', 'Минусинск', 'Мирный', 'Мичуринск',
        'Можайск', 'Можга', 'Моздок', 'Мокшан', 'Мончегорск', 'Морозовск',
        'Моршанск', 'Москва', 'Москва, МГУ', 'Мостовской', 'Муравленко',
        'Мураши', 'Мурманск', 'Муром', 'Мценск', 'Мыс Шмидта', 'Мытищи',
        'Набережные Челны', 'Надым', 'Назрань', 'Нальчик', 'Наро-Фоминск',
        'Нарткала', 'Нарым', 'Нарьян-Мар', 'Находка', 'Невельск',
        'Невинномысск', 'Невьянск', 'Неплюевка', 'Нерчинск', 'Нефедова',
        'Нефтегорск (Самар.)', 'Нефтекамск', 'Нефтеюганск', 'Нижневартовск',
        'Нижнекамск', 'Нижнеудинск', 'Нижний Новгород', 'Нижний Тагил',
        'Новая Игирма', 'Новгород Великий', 'Новокузнецк', 'Новомичуринск',
        'Новомосковск', 'Новороссийка', 'Новороссийск', 'Новосибирск',
        'Новочеркасск', 'Новый Оскол', 'Новый Уренгой', 'Ногинск (Моск.)',
        'Ноглики', 'Норильск', 'Ноябрьск', 'Нурлат', 'Нягань', 'Нязепетровск',
        'Обнинск', 'Обоянь', 'Объячево', 'Одинцово', 'Озеры', 'Оймякон',
        'Октябрьский (Башк.)', 'Октябрьское (Хант.)', 'Октябрьское (Челяб.)',
        'Оленегорск (Якут.)', 'Оленек', 'Омск', 'Онега', 'Орел', 'Оренбург',
        'Орехово-Зуево', 'Орск', 'Оса', 'Осташков', 'Оха', 'Охотск',
        'Павловская', 'Павловский Посад', 'Палана', 'Партизанск', 'Певек',
        'Пенза', 'Переславль-Залесский', 'Пермь', 'Петрозаводск',
        'Петропавловск-Камчатский', 'Петухово', 'Петушки', 'Печенга', 'Печора',
        'Пинега', 'Плес', 'Плесецк', 'Подольск', 'Поронайск', 'Поярково',
        'Приморско-Ахтарск', 'Приозерск', 'Прохладный', 'Псебай', 'Псков',
        'Пушкин', 'Пушкино (Моск.)', 'Пушкинские Горы', 'Пышма', 'Пятигорск',
        'Радужный', 'Раменское', 'Ребриха', 'Ревда (Сверд.)', 'Ржев',
        'Рославль', 'Россошь', 'Ростов', 'Ростов-на-Дону', 'Рубцовск', 'Руза',
        'Рыбинск', 'Рыльск', 'Ряжск', 'Рязань', 'Салават', 'Салехард',
        'Сальск', 'Самара', 'Санкт-Петербург', 'Саранск', 'Сарапул', 'Саратов',
        'Саров (Морд.)', 'Сасово', 'Саянск', 'Светлогорск (Калин.)',
        'Северо-Курильск', 'Северобайкальск', 'Северодвинск', 'Североморск',
        'Североуральск', 'Сеймчан', 'Семлячики', 'Серафимович',
        'Сергиев Посад', 'Серебряные Пруды', 'Середниково', 'Серов',
        'Серпухов', 'Сибай', 'Сковородино', 'Славгород', 'Славянск-на-Кубани',
        'Сладково', 'Слюдянка', 'Смирных', 'Смоленск', 'Снежинск',
        'Снежногорск (Мурм.)', 'Соболево', 'Советский', 'Соликамск',
        'Солнечногорск', 'Соловки', 'Соль-Илецк', 'Сорочинск', 'Сортавала',
        'Сосновый Бор', 'Сосногорск', 'Сосьва (Хант.)', 'Сочи', 'Ставрополь',
        'Старая Русса', 'Старый Оскол', 'Стерлитамак', 'Стрежевой', 'Ступино',
        'Суздаль', 'Сузун', 'Сунтар', 'Сургут (Хант.)', 'Сусуман', 'Сухиничи',
        'Сызрань', 'Сыктывкар', 'Тавда', 'Таганрог', 'Тайшет', 'Талдом',
        'Тамбей', 'Тамбов', 'Тарко-Сале', 'Таштагол', 'Тверь', 'Теберда',
        'Темрюк', 'Териберка', 'Терней', 'Терскол', 'Тикси', 'Тимашевск',
        'Тихвин', 'Тихорецк', 'Тобольск', 'Токма', 'Токсово', 'Тольятти',
        'Томари', 'Томпа', 'Томск', 'Торжок', 'Тосно', 'Тотьма',
        'Троицк (Челяб.)', 'Троицк (Моск.)', 'Троицко-Печорск', 'Туапсе',
        'Тула', 'Тулпан', 'Тулун', 'Тура', 'Туруханск', 'Тутаев', 'Тутончаны',
        'Тымовское', 'Тында', 'Тырныауз', 'Тюмень', 'Уварово', 'Углегорск',
        'Углич', 'Улан-Удэ', 'Ульяновск', 'Урай', 'Уренгой', 'Урус-Мартан',
        'Урюпинск', 'Усинск', 'Усмань', 'Усолье Сибирское', 'Уссурийск',
        'Усть-Баргузин', 'Усть-Джегута', 'Усть-Илимск', 'Усть-Ишим',
        'Усть-Калманка', 'Усть-Камчатск', 'Усть-Катав', 'Усть-Кулом',
        'Усть-Кут', 'Усть-Ордынский', 'Устюжна', 'Уфа', 'Ухта', 'Учалы',
        'Уэлен', 'Фатеж', 'Хабаровск', 'Ханты-Мансийск', 'Хасавюрт',
        'Хасан', 'Хатанга', 'Химки', 'Холмогоры', 'Холмск', 'Хоста',
        'Хужир', 'Цимлянск', 'Чайковский', 'Чебаркуль', 'Чебоксары',
        'Чегем', 'Челюскин', 'Челябинск', 'Черемхово', 'Череповец',
        'Черкесск', 'Чермоз', 'Черняховск', 'Черский', 'Черусти', 'Чехов',
        'Чикола', 'Чита', 'Чокурдах', 'Чулым', 'Чусовой', 'Шадринск', 'Шали',
        'Шамары', 'Шарья', 'Шатки', 'Шатой', 'Шатура', 'Шаховская', 'Шахты',
        'Шелагонцы', 'Шелехов', 'Шенкурск', 'Шерегеш', 'Шереметьево', 'Шилка',
        'Шумиха', 'Шуя', 'Щелково', 'Щельяюр', 'Элиста', 'Эльбрус', 'Эльтон',
        'Энгельс', 'Югорск', 'Южно-Курильск', 'Южно-Сахалинск', 'Южноуральск',
        'Юровск', 'Юрьев-Польский', 'Юрьевец (Иван.)', 'Юрюзань', 'Якутск',
        'Якша', 'Ялуторовск', 'Ямбург', 'Яр-Сале', 'Ярославль',
        'Ясный (Оренб.)', 'Яхрома', 'Яшалта', 'Яшкуль',
    )

    region_republics = (
        'Адыгея', 'Алтай', 'Башкортостан', 'Бурятия', 'Дагестан',
        'Ингушетия', 'Кабардино-Балкария', 'Калмыкия', 'Карачаево-Черкесия', 'Карелия',
        'Коми', 'Крым', 'Марий-Эл', 'Мордовия', 'Саха (Якутия)',
        'Северная Осетия - Алания', 'Татарстан', 'Тыва', 'Удмуртия', 'Хакасия',
        'Чечня', 'Чувашия',
    )

    region_krai = (
        'Алтайский', 'Забайкальский', 'Камчатский', 'Краснодарский', 'Красноярский',
        'Пермский', 'Приморский', 'Ставропольский', 'Хабаровский',
    )

    region_oblast = (
        'Амурская', 'Архангельская', 'Астраханская', 'Белгородская', 'Брянская',
        'Владимирская', 'Волгоградская', 'Вологодская', 'Воронежская', 'Ивановская',
        'Иркутская', 'Калининградская', 'Калужская', 'Кемеровская', 'Кировская',
        'Костромская', 'Курганская', 'Курская', 'Ленинградская', 'Липецкая',
        'Магаданская', 'Московская', 'Мурманская', 'Нижегородская', 'Новгородская',
        'Новосибирская', 'Омская', 'Оренбургская', 'Орловская', 'Пензенская',
        'Псковская', 'Ростовская', 'Рязанская', 'Самарская', 'Саратовская',
        'Сахалинская', 'Свердловская', 'Смоленская', 'Тамбовская', 'Тверская',
        'Томская', 'Тульская', 'Тюменская', 'Ульяновская', 'Челябинская',
        'Ярославская',
    )

    region_ao = (
        'Еврейская', 'Ханты-Мансийский', 'Чукотский', 'Ямало-Ненецкий', 'Ненецкий',
    )

    countries = (
        'Австралия', 'Австрия', 'Азербайджан', 'Албания',
        'Алжир', 'Ангола', 'Андорра', 'Антигуа и Барбуда',
        'Аргентина', 'Армения', 'Афганистан', 'Багамские Острова',
        'Бангладеш', 'Барбадос', 'Бахрейн', 'Белоруссия', 'Белиз',
        'Бельгия', 'Бенин', 'Болгария', 'Боливия', 'Босния и Герцеговина',
        'Ботсвана', 'Бразилия', 'Бруней', 'Буркина-Фасо', 'Бурунди',
        'Бутан', 'Вануату', 'Великобритания', 'Венгрия', 'Венесуэла',
        'Восточный Тимор', 'Вьетнам', 'Габон', 'Гаити', 'Гайана',
        'Гамбия', 'Гана', 'Гватемала', 'Гвинея', 'Гвинея-Бисау', 'Германия',
        'Гондурас', 'Гренада', 'Греция', 'Грузия', 'Дания', 'Джибути',
        'Доминика', 'Доминиканская Республика', 'Египет', 'Замбия',
        'Зимбабве', 'Израиль', 'Индия', 'Индонезия', 'Иордания',
        'Ирак', 'Иран', 'Ирландия', 'Исландия', 'Испания', 'Италия',
        'Йемен', 'Кабо-Верде', 'Казахстан', 'Камбоджа', 'Камерун',
        'Канада', 'Катар', 'Кения', 'Кипр', 'Киргизия', 'Кирибати',
        'Китай', 'Колумбия', 'Коморы', 'Республика Конго',
        'Демократическая Республика Конго', 'КНДР', 'Республика Корея',
        'Коста-Рика', 'Кот-д’Ивуар', 'Куба', 'Кувейт', 'Лаос', 'Латвия',
        'Лесото', 'Либерия', 'Ливан', 'Ливия', 'Литва', 'Лихтенштейн',
        'Люксембург', 'Маврикий', 'Мавритания', 'Мадагаскар', 'Малави',
        'Малайзия', 'Мали', 'Мальдивы', 'Мальта', 'Марокко', 'Маршалловы Острова',
        'Мексика', 'Мозамбик', 'Молдавия', 'Монако', 'Монголия', 'Мьянма',
        'Намибия', 'Науру', 'Непал', 'Нигер', 'Нигерия', 'Нидерланды',
        'Никарагуа', 'Новая Зеландия', 'Норвегия', 'ОАЭ', 'Оман', 'Пакистан',
        'Палау', 'Панама', 'Папуа', 'Парагвай', 'Перу', 'Польша', 'Португалия',
        'Россия', 'Руанда', 'Румыния', 'Сальвадор', 'Самоа', 'Сан-Марино',
        'Сан-Томе и Принсипи', 'Саудовская Аравия', 'Северная Македония',
        'Сейшельские Острова', 'Сенегал', 'Сент-Винсент и Гренадины',
        'Сент-Китс и Невис', 'Сент-Люсия', 'Сербия', 'Сингапур', 'Сирия',
        'Словакия', 'Словения', 'США', 'Соломоновы Острова', 'Сомали',
        'Судан', 'Суринам', 'Сьерра-Леоне', 'Таджикистан', 'Таиланд',
        'Танзания', 'Того', 'Тонга', 'Тринидад и Тобаго', 'Тувалу',
        'Тунис', 'Туркмения', 'Турция', 'Уганда', 'Узбекистан', 'Украина',
        'Уругвай', 'Федеративные Штаты Микронезии', 'Фиджи', 'Филиппины',
        'Финляндия', 'Франция', 'Хорватия', 'Центральноафриканская Республика',
        'Чад', 'Черногория', 'Чехия', 'Чили', 'Швейцария', 'Швеция',
        'Шри-Ланка', 'Эквадор', 'Экваториальная Гвинея', 'Эритрея',
        'Эсватини', 'Эстония', 'Эфиопия', 'ЮАР', 'Южный Судан', 'Ямайка', 'Япония',
    )

    def city_prefix(self):
        return self.random_element(self.city_prefixes)

    def city_name(self):
        return self.random_element(self.city_names)

    def country(self):
        return self.random_element(self.countries)

    def region(self):
        regions_suffix = self.random_element(self.region_suffixes)
        region_name = ''
        result = region_name + ' ' + regions_suffix
        if regions_suffix == 'респ.':
            region_name = self.random_element(self.region_republics)
            result = regions_suffix + ' ' + region_name
        elif regions_suffix == 'край':
            region_name = self.random_element(self.region_krai)
        elif regions_suffix == 'обл.':
            region_name = self.random_element(self.region_oblast)
        elif regions_suffix == 'АО':
            region_name = self.random_element(self.region_ao)
        return result

    def street_suffix(self):
        return self.random_element(self.street_suffixes)

    def street_title(self):
        return self.random_element(self.street_titles + self.street_titles_noflex)

    def street_name(self):
        suffix = self.street_suffix()
        street = self.street_title()
        stem = street[:-2]
        inflexion = ''
        result = street
        if street not in self.street_titles_noflex:
            if not (suffix in self.street_suffixes_fem and (stem in self.street_titles_irregular_masc
                                                            or stem in self.street_titles_irregular_neu)):
                if suffix in self.street_suffixes_masc:
                    result = stem + inflexion
                    inflexion = 'ый'
                    if stem.endswith('ск') or stem.endswith('цк'):
                        inflexion = 'ий'
                elif suffix in self.street_suffixes_neu:
                    inflexion = 'ое'
        return suffix + ' ' + result
