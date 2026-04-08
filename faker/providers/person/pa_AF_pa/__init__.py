
from faker.providers.person import Provider as PersonProvider
import random
"""
Afghanistan Pashto (English Transliteration) Locale for Faker

This package provides Afghan Pashto and Tajik personal names written in English
transliteration, including support for male and female first names, last names,
prefixes, and suffixes.
"""


class Provider(PersonProvider):
    # ------------------------ PREFIXES ------------------------
    # Pashto honorifics / titles for male and female names
    # د نارینه او ښځینه نومونو لپاره پښتو لقبونه / احترامتي ټکي

    prefixes_male = [
        "مولوي", "الحاج", "قاري", "سردار", "خان",
        "حاجي", "ملا", "استاد", "حاج", "امیر", "نجيب", "غلام", "ظاهر", "سيد", "ملک"
    ]

    prefixes_female = [
        "آغلې", "محترمه", "بی بی", "میرمنه", "ښایسته",
        "ډاکټرې", "اغلې", "بی بي", "محترمه خانم", "محترمه بي بي"
    ]


    pashto_male_first_names = [
        'احمد', 'محمد', 'عبدالله', 'نورالله', 'خالد', 'رحیم', 'فرید', 'ناصر', 'جمال',
        'طارق','ولي', 'يوسف', 'ظاهر', 'بشير',
        'داود', 'فیصل', 'گل', 'حمید', 'اسماعیل', 'جاوید',
        'کریم', 'لطیف', 'مسعود', 'نور', 'عمر', 'قادر', 'رشید', 'صافی', 'طالب', 'واحد',
        'بریالی', 'سپین', 'تور', 'زمرد', 'خوستی', 'وزیر', 'میران', 'سنجر', 'شینواری', 'غلجی',
        'امان الله', 'عزیز', 'بشیر', 'داوود', 'احسان', 'فهیم', 'غلام', 'حبیب', 'ابراهیم', 'جلال',
        'کبیر', 'لطف الله', 'منصور', 'نعیم', 'عبید', 'پاچا', 'قیس', 'رحمت', 'ستار', 'تواب',
        'عمر', 'ولي', 'ویس', 'یعقوب', 'ذبی', 'عبدال', 'عطاالله', 'بسم الله', 'چمن', 'دستگیر',
        'عزت', 'فروز', 'غوث', 'حافظ', 'عنایت', 'جهان', 'خلیل', 'لال', 'متین', 'نظر',
        'عمر', 'پیر', 'قربان', 'رحیم', 'سامی', 'طاهر', 'عبید', 'وکیل', 'ولي', 'یار',
        'زمان', 'امین', 'باز', 'چنار', 'دلور', 'احسان الله', 'فضل', 'گلزار', 'حاجی', 'الیاس',
        'جمعه', 'خال', 'لاله', 'ملا', 'نیک', 'امید', 'پاچا', 'قادر', 'رحمن', 'صادق',
        'طالب',   'وفادار', 'وزیر', 'یونس', 'زبیر', 'عاشق', 'بدر', 'چراغ', 'دریا',
        'عید', 'فیض', 'گوهر', 'حکیم', 'اقبال', 'جمیل', 'خان', 'لیاقت', 'مؤمن', 'نواب',
        'عبیدالله', 'پیمان', 'قاسم', 'رفیق', 'صاحب', 'تاج', 'عثمان', 'وکیل', 'وطن', 'یفتلی',
        'زرداد', 'اسد', 'بهرام', 'چمن', 'دوست', 'ایباد', 'فتح', 'غوث الدین', 'هدایت', 'اسحاق',
        'جواد', 'کمال', 'لطف', 'میران', 'نور', 'عبید', 'پرویز', 'قدرت', 'رحیم الله', 'صابر',
        'توفیق', 'عمر', 'وداد', 'وهاب', 'یحیی', 'زلمی', 'ایمل', 'بابر', 'چنار', 'دل',
        'ایمل', 'فرهاد', 'گلب الدین', 'حاجی', 'عرفان', 'جهانگیر', 'خالد', 'لال', 'میران', 'نیک',
        'عمر', 'پاچا', 'قیس', 'رحمت الله', 'ساحل', 'طاهر', 'عبیدالله', 'وسیف', 'ولي الله', 'یحیی',
        'زکی', 'عارف', 'بلال', 'چمن الله', 'داود', 'احسان', 'فضل الله', 'گل', 'حکیم', 'ابراهیم',
        'جمشید', 'خلیل الله', 'لطیف الله', 'مؤمن', 'نظیر', 'عبید', 'پیر', 'قربان', 'رحیم', 'سمیع الله',
        'تاج الدین', 'عثمان', 'وکیل', 'وارث', 'یاسین', 'ذبیح', 'اسلم', 'بسم الله','خیرالله','سپين گل', 'تور گل'
        ,'چنار', 'سپين زر','گلبهار',

        'اباسين', 'عبد ال', 'احمد', 'اېمل', 'علي', 'عالم', 'عالم زيب', 'امېل', 'امو', 'اندام', 'انګار', 'ارمغان',
        'ارمان', 'ارسلان', 'آرئين', 'اسفند', 'اسفنديار', 'اتل', 'اتڅک', 'اورنگ', 'اول مير', 'ازلان', 'ازمرې', 'بابک',
        'بابرک', 'باچا', 'بادام', 'بهرام', 'بهره مند', 'بهرور', 'بخت', 'بخت روان', 'ختور', 'بلاڅ', 'بلی', 'برلاس',
        'بريال', 'بريالې', 'بصير', 'باټور', 'باز', 'بازګر', 'بازير', 'بهروذ', 'بېلتون', 'چارګل', 'چنار', 'ډګر', 'دراب',
        'درمان', 'دروېش', 'دريا', 'درياب', 'دولت', 'دوړ', 'ديار', 'دلاور', 'درون', 'ايلام', 'فرهنګ', 'فريدون', 'ګهېز',
        'ګېډئ', 'غېرت', 'غښتالې', 'غلجي', 'غمې', 'غرڅنې', 'غټول', 'غزن', 'غزين', 'غورزنګ', 'غونچه ګل', 'غورغشت', 'ګوګل',
        'غوربت', 'ګران', 'ګل', 'ګلباز', 'ګل جان', 'ګل مست', 'ګل رنګ', 'ګل يار', 'ګل زمان', 'ګلاب', 'ګلزار', 'هسک',
        'هېلمند', 'هېواد', 'حکم', 'عزت', 'جانان', 'جنت ګل', 'جنډول', 'کاکې', 'کرلاڼي', 'کارمل', 'کاروان', 'ښاغلې',
        'ښائسته', 'خاک', 'خالو', 'خان', 'خاندور', 'خيالې', 'خوږ', 'خوشال', 'خوش دل', 'خوزون', 'خيبر', 'کوچې', 'کوشان',
        'لاجبر', 'لښکر', 'لعل', 'لؤنګ', 'لونګين', 'لمر', 'لېوال', 'ميړانې', 'ميوند', 'ملنګ', 'ملوک', 'ماليار', 'منان',
        'منګل', 'مرغوز', 'مرجان', 'مړوند', 'مشال', 'متين', 'مهتر', 'منت بار', 'مير ويس', 'ميرزل', 'موهمبر', 'محمّد',
        'محمود', 'ننګ', 'ننګيالې', 'نوميالې', 'نفېل', 'اولس', 'اولس يار  اولسيار', 'پېمان', 'پامير', 'پشتون', 'پاڅون',
        'پاڅون', 'پتنګ', 'پاتمن', 'پټوال', 'پتيال', 'پيوستون', 'پېلابو', 'پېرزو', 'پوهاند', 'پور دل', 'پونده', 'سپرلې',
        'قجير ګل', 'قلندر', 'رحم دل', 'رنګين', 'ړيدې', 'ريشتين', 'روشان  روښان', 'رستم', 'سباون', 'سادين', 'سحر',
        'سحر ګل', 'سهيم', 'سېفور', 'سالار', 'سمندر', 'سمون', 'سمسور', 'سنګر', 'سنګين', 'سنګرېز', 'سنوبر', 'سرابن',
        'سرباز', 'سردار', 'سرتور', 'سائل', 'سيلاب', 'سېلاني', 'شاه سوار', 'شاه زر', 'شمال', 'شمشاد', 'شیر', 'شير دل',
        'شېرين', 'شين ګل', 'شيندي ګل', 'شينو', 'شپول', 'شپون', 'شجاء', 'صبغت الله', 'صفت', 'سکندر', 'سهراب', 'سپرلې',
        'سپېڅلې', 'سپين', 'سپين ګل', 'سپين زر', 'ستورې', 'سور ګل', 'سوئېل', 'تعبان', 'تنيم', 'تړون', 'تاؤس', 'ټيري',
        'طوفان', 'ټولواک', 'تور ګل', 'توريال', 'طوطي', 'توران', 'توريالې', 'ودان', 'وېس', 'واکدار', 'واکمن', 'ولي',
        'يمه', 'يون', 'زعفران', 'ځلان', 'ځلند  ځلاند', 'زلمې', 'زپران', 'زر ګل', 'زرولي', 'زرک', 'زرم', 'زرنګ', 'زربت',
        'زرداب', 'زرداد', 'زرګر', 'زرغون', 'زړور', 'زړګې', 'زرين', 'زرکاڼې', 'زرلېش', 'زرمست', 'زرنوش', 'زرياب', 'زوار',
        'ژور', 'زږرد', 'زيار', 'زيار مل', 'زيګر', 'زمرک', 'زمرې', 'زورک', 'زورور', 'ځواک', 'ژوندون',
    ]

    pashto_female_first_names = [
        'مريم', 'فاطمه', 'زهرا', 'ليلى', 'ناديه', 'صبرينه', 'ثريا', 'پروين', 'شکريه', 'فرشته',
        'هاديه', 'جميله', 'کميله', 'نرگس', 'رضيه', 'صافيه', 'تمنّا', 'وجيهه', 'ياسمين', 'زرمنه',
        'گل الای', 'ميرمن', 'سپين گل', 'تور پیکۍ', 'وږمه', 'شمسیه', 'نغمه', 'مشعل', 'سنګه', 'زرغونه',
        'عایشه', 'بی بی', 'چمن', 'دل افروز', 'ایمان', 'فرحناز', 'گل', 'هدیه', 'ارم', 'جهان آرا',
        'خديجه', 'لال زری', 'مهناز', 'نبيله', 'عذرا', 'پروانه', 'قمر', 'رحیله', 'سحر', 'تبسم',
        'عظمی', 'ویدا', 'وحیده', 'یلدا', 'زينب', 'افسانه', 'بخت', 'چمن', 'دردانه', 'ارم',
        'فوزيه', 'گلشن', 'حوا', 'عفت', 'جمیله', 'کلثوم', 'ليلى', 'معصومه', 'نجیبه', 'عمره',
        'پلوشه', 'قُبره', 'رحيمه', 'سکينه', 'طاهره', 'عروج', 'ویدا', 'وجمه', 'یاسره', 'زرقه',
        'عقيله', 'بشری', 'چنار', 'دل ربا', 'ایشل', 'فريال', 'گلنار', 'هينا', 'عنایت', 'جوهره',
        'کاوش', 'لمر', 'منيره', 'نسرين', 'امید', 'پریسا', 'قدسیه', 'رضيه', 'صدف', 'تسلیمه',
        'اميره', 'وسيله', 'وزيره', 'یمنه', 'ذبیحه', 'انیسه', 'بهر', 'چين', 'دریا', 'الهام',
        'فرخنده', 'گلرخ', 'هرا', 'اقراء', 'جوید', 'کيران', 'لیلما', 'مهره', 'نازيه', 'اورانه',
        'پری', 'قرأت', 'رحمت', 'صائمه', 'طاهره', 'عظمی', 'ویدا', 'ورثه', 'یاسمین', 'ذولفقه',
        'عروج', 'بانو', 'چمن آرا', 'دلشاد', 'ایمان', 'فرزانه', 'گلبانو', 'هما', 'ارم', 'جنت',
        'کشمله', 'لیلی', 'مهوش', 'نرگس', 'امیمه', 'پیمان', 'قمريه', 'روشنه', 'صغری', 'تارا',
        'علفت', 'ویدا', 'وحیده', 'ياسمين', 'زاره', 'عاليه', 'بهر', 'چمن', 'دلبر', 'ایما',
        'فهيمه', 'گلبهار', 'هینه', 'ارم', 'جویریه', 'خالده', 'ليلى', 'مهيره', 'نسیم', 'اميده',
        'پری زاد', 'قدسیه', 'رخساره', 'صبا', 'تسنيم', 'عروسه', 'وسيمه', 'وجدان', 'ياسمين', 'زارين',
        'امینه', 'بی بی', 'چمن', 'دردانه', 'ارم', 'فوزيه', 'گل', 'حوا', 'عفت', 'جمیله',
        'کلثوم', 'ليلى', 'معصومه', 'نجیبه', 'عمره', 'پلوشه', 'قُبره', 'رحيمه', 'سکينه', 'طاهره',
        'عروج', 'ویدا', 'وجمه', 'یاسره', 'زرقه', 'عقيله', 'بشری', 'چنار', 'دل ربا', 'ایشل',
        'فريال', 'گلنار', 'هينا', 'عنایت', 'جوهره', 'کاوش', 'لمر', 'منيره', 'نسرين', 'امید',
        'پریسا', 'قدسیه', 'رضيه', 'صدف', 'تسلیمه', 'اميره', 'وسيله', 'وزيره', 'یمنه', 'ذبیحه',
        'انیسه', 'بهر', 'چين', 'دریا', 'الهام', 'فرخنده', 'گلرخ', 'هرا', 'اقراء', 'جوید',
        'کيران', 'لیلما', 'مهره', 'نازيه', 'اورانه', 'پری', 'قرأت', 'رحمت', 'صائمه', 'طاهره', 'عفيه',
        'اغله', 'عمبرين', 'انګېزه', 'آپانه', 'اريانه', 'عفيه', 'اغله', 'عمبرين', 'انګېزه', 'آپانه', 'اريانه',
        'بدري', 'بختوره', 'بلبله', 'بنفشه', 'برساله',  'بي بي', 'روښانه', 'بريښنا', 'ډيوه', 'درخانيي',
        'فرشته', 'ګبينه', 'ګلې', 'غټوله', 'غوټې', 'غونچه', 'ګرانه',   'بانو ګل', 'غوټې',   'لښته',
        'ګل مکي ', 'مينه', 'ګل پاڼه', 'ګل', 'څانګه', 'ګل', 'ورين', 'ګلالي', 'ګلچين', 'ګلنار', 'هاله',
        'هيلي', 'هليه', 'حنه', 'هوسي', 'کشماله', 'ښايسته', 'ښاپېري', 'ښارو', 'خاټول', 'ښکلې', 'خوږه',
        'کوچې', 'کونتره', 'ليلۍ', 'ليلومه', 'لخته', 'للمه', 'لال', 'زاري', 'لمبه', 'لونګه', 'ليمه',
        'ماه جبين ', ' ماه نور', 'نور ماه', 'ځاله', 'ملالي', 'ملغلره', 'مينه', 'مکيي', 'مرچکې', 'مسکا',
        'نغمه', 'ننګيالي', 'نارنجه', 'نتکې', 'نؤياته', 'نازنينه', 'نازدانه', 'نازو', 'نيازمينه', 'اوربخته',
        'اورژاله', 'پلوشه', 'پاڼه', 'پرغونډه', 'پشمينه', 'پتاسه', 'پېغره', 'پرخه', 'پوخله', 'رڼا', 'رايان',
        'ريښمينه', 'ريښتينه', 'روشينه', 'صبا', 'سندره', 'څانګه', 'سنګينه', 'سينزله', 'شاغلې', 'شاهې',
        'لاليي', 'شميره', 'شمله', 'شاندانه', 'شانزي', 'شاپېري', 'شاستيي', 'شازمينه', 'شېرين', 'شينکي',
        'شينوګيي', 'شوغله', 'سيلي', 'سپرغي', 'سپوږمي', 'سپوژمي', 'ستوري', 'تعبانه', 'تلوسه',
        'تورپيکي', 'اوګي', 'ودانه', 'وږمه', 'وحيده', 'وجيه', 'ورده', 'واورينه', 'وړنګه', 'ورېشمين',
        'زېن',   'زېتونه', 'زکيه', 'ژاله', 'ځالنده', 'زمده','بي بي زره ', 'زره بي بي', 'زر', 'مسته',
        'زرمينه', 'زرورين', 'زره',
        'باحه', 'زرينه', 'زريش', 'زرغونه', 'زرکه', 'زرلښته', 'زرسانګه', 'زرتاج', 'ژالي', 'زهل', 'زفاش'

        ,
        'انګېزه', 'انار', 'آرا', 'آپانه', 'اريانه', 'بدري', 'بختوره', 'بله نشته', 'بلبله', 'بنفشه', 'برساله', 'بزيره',
        'ںېنظيره', 'بي بي', 'بي بي روښانه', 'بريښنا', 'ډيوه', 'درخانئي', 'فرشته', 'ګبينه', 'ګلې', 'غټوله', 'غورشکه',
        'غوټې', 'غونچه', 'ګورګوره', 'ګرانه', 'ګل بانو', 'ګل غوټې', 'ګل لښته', 'ګل مکئ', 'ګل مينه', 'ګل پاڼه',
        'ګل څانګه', 'ګل ورين', 'ګلالئ', 'ګلچين', 'ګلنار', 'هاله', 'هيلئ', 'هليه', 'حنه', 'هوسئ', 'کشمالہ', 'ښائسته',
        'ښاپېرئ', 'ښارو', 'خاټول', 'ښکلې', 'خوش بخته', 'خوږه', 'کوچې', 'کونتره', 'ليلۍ', 'ليلومه', 'لخته', 'للمه',
        'لال زاري', 'لمبه', 'لونګه', 'ليمه', 'ماه جبين', 'ماه نور', 'ماه ځاله', 'ملالئ', 'ملغلره', 'مینا', 'مکئي',
        'منؤره', 'مرچکې', 'مسکا', 'نغمه', 'ننګيالئ', 'نارنجه', 'نتکې', 'نؤياته', 'نازنينه', 'نازدانه', 'نازو',
        'نيازمينه', 'اوربخته', 'اوربله', 'اورژاله', 'پلوشه', 'پاڼه', 'پرغونډه', 'پريورش', 'پرخه', 'پشمينه', 'پتاسه',
        'پېغره', 'پرخه', 'پوخله', 'رڼا', 'رايان', 'ريښمينه', 'ريښتينه', 'روشينه', 'صبا', 'سلګئ', 'سندره', 'څانګه',
        'سنګينه', 'سيلئ', 'سينزله', 'شاغلې', 'شاهې', 'شاه لالئي', 'شمله', 'شاندانه', 'شانزئ', 'شاپېرئ', 'شاستئي',
        'شازمينه', 'شېرين', 'شينکئ', 'شينوګئي', 'شوغله', 'سپلمئ', 'سپرغئ', 'سپېځله', 'سپوژمئ  سپوږمئ', 'ستورئ',
        'تعبانه', 'تل وسه', 'تنيمه', 'تور پيکائ', 'اوګئ', 'ودانه', 'وږمه', 'وحيده', 'وجيه', 'ورده', 'واورينه', 'وړنګه',
        'ورېشمين', 'زېن با', 'زېتونه', 'زکيه', 'ژاله', 'ځالنده', 'ځلوبه', 'زمده', 'زر بي بي', 'زر مسته', 'زرمينه',
        'زرورين', 'زر باحه', 'زرينه', 'زريش', 'زرغونه', 'زرقه', 'زرلښته', 'زرسانګه', 'زرشاله', 'زرتاج', 'ژاله', 'ژالئ',
        'زهل', 'زفاش'
    ]


    last_names = [
        "دراني",
        "پوپلزي",
        "بارکزي",
        "الکوزي",
        "اڅکزي",
        "غلجي",
        "هوتک",
        "توخي",
        "ناصر",
        "خروټي",
        "سولېمان خېل",
        "علي خېل",
        "ابراهيم خېل",
        "يوسفزي",
        "مومند",
        "افريدي",
        "شينواري",
        "محسود",
        "وزير",
        "داور",
        "بانوڅي",
        "خټک",
        "اورکزي",
        "ترين",
        "کاکړ",
        "ماندر",
        "شرني",
        "منګل",
        "زدران",
        "چمکني",
        "تاني",
        "احمدزي",
        "نورزي",
        "لودهي",
        "مروټ",
        "نيازي",
        "سور",
        "اندړ",
        "گګياڼي",
        "خليل",
        "داؤدزي",
        "چمکني",
        "بابي",
        "ګدون",
        "ملاګوري",
        "اتمان خېل",
        "توري",
        "بنګښ",
        "ساپي",
        "جاجي",
        "خوګياڼي",
        "وتر",
        "پڼي",
        "ستوري",
        "مرکي",
        "لوني",
        "احمدي","رحيمي","عزيزي","نورزاي","تاجک","هوتک","زيارت","خټک","افغان","نورستاني",
                                                                                     "زند", "پښتون", "میوند", "کوچی",
        "اڅکزی", "مومند", "غور", "هزاره", "اشرف", "کندهاري",
        "قندهار", "یوسفزی", "زمر", "زوی", "شينواری", "مير", "قريشي", "سعيد", "نيازي", "فرزند",
        "ګل", "صافي", "شيراني", "کريم", "احمدزاده", "شاه", "خليل", "بهادر", "مرتضي", "ناصر",
        "حکيم", "جهانګير", "ظاهر", "جلال", "لطيف", "بابر", "فاروق", "عمر", "قاسم", "جمال", "فريد",
        "شکيبا", "نسرين", "زينب", "مريم", "فاطمه", "ليلا", "زهرا", "عایشه", "نرگس", "فرشته",
        "نجمه", "لاله", "شيرين", "گوهر", "ګلزار", "بشير", "غلام", "نور", "شيرزاد", "مومن", "طالب",
        "امين", "فقير", "امير", "زمان", "يوسف", "احمدشاه", "سردار", "ملا"

    ]



    # ================ Email section =====================

    last_names_email = [
        'Khan', 'Ahmadzai', 'Mohammadi', 'Karimi', 'Hussaini', 'Rahmani', 'Sadiqi', 'Yousafzai', 'Popal', 'Ghilzai',
        'Durrani', 'Barakzai', 'Noori', 'Alkozai', 'Stanikzai', 'Zazai', 'Wardak', 'Kharoti', 'Hotak', 'Taraki',
        'Ahmadi', 'Alami', 'Balkhi', 'Danish', 'Ebrahimi', 'Faruqi', 'Ghani', 'Hakimi', 'Ibrahimi', 'Jami',
        'Arsalai', 'Atmar', 'Azizi', 'Bakhtari', 'Charkhi', 'Dost', 'Ehsas', 'Faqiri', 'Gul', 'Haidari',
        'Ismail', 'Jabarkhel', 'Kakar', 'Lodin', 'Mangal', 'Niazi', 'Omar', 'Paktin', 'Qaderi', 'Rasuli',
        'Safi', 'Tani', 'Umar', 'Wafa', 'Yaftali', 'Zadran', 'Achakzai', 'Babrakzai', 'Chamkani', 'Dawlatzai',
        'Esmat', 'Fahim', 'Ghafor', 'Habibi', 'Ishaqzai', 'Jalalzai', 'Kandahari', 'Lakanwal', 'Mahmood', 'Nazar',
        'Obaidullah', 'Parwani', 'Qaisrani', 'Rohani', 'Sangin', 'Tarakai', 'Usmani', 'Waziri', 'Yaqubi', 'Zabuli',
        'Afridi', 'Bangash', 'Chitrali', 'Daudzai', 'Eid', 'Farooz', 'Ghalib', 'Hassanzai', 'Ibrahimkhel', 'Jalalabad',
        'Khattak', 'Lashkari', 'Marwat', 'Nangarhar', 'Orakzai', 'Peshawari', 'Qandahari', 'Rahim', 'Shinwari', 'Turi',
        'Uthmanzai', 'Wazir', 'Yousuf', 'Zakhil', 'Amin', 'Babar', 'Chaman', 'Dawood', 'Eidgah', 'Farooq',
        'Ghaznavi', 'Habibullah', 'Ilyas', 'Jamal', 'Khalil', 'Latif', 'Miran', 'Nek', 'Obaid', 'Pacha',
        'Qais', 'Rahimullah', 'Sahib', 'Taj', 'Ubaid', 'Vakil', 'Wali', 'Yar', 'Zaman', 'Aminullah',
        'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas', 'Juma', 'Khal',
        'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq', 'Talib', 'Ustad',
        'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya', 'Eid', 'Faiz',
        'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab', 'Obaidullah', 'Paiman',
        'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali', 'Zardad', 'Asad',
        'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq', 'Jawad', 'Kamal',
        'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir', 'Tawfiq', 'Umar',
        'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil', 'Emal', 'Farhad',
        'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek', 'Omar', 'Pacha',
        'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya', 'Zaki', 'Arif',
        'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim', 'Jamshed', 'Khalilullah',
        'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah', 'Tajuddin', 'Usman',
        'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar', 'Eid', 'Farooz',
        'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar', 'Obaidullah', 'Pacha',
        'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar', 'Zaman', 'Aminullah',
        'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas', 'Juma', 'Khal',
        'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq', 'Talib', 'Ustad',
        'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya', 'Eid', 'Faiz',
        'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab', 'Obaidullah', 'Paiman',
        'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali', 'Zardad', 'Asad',
        'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq', 'Jawad', 'Kamal',
        'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir', 'Tawfiq', 'Umar',
        'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil', 'Emal', 'Farhad',
        'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek', 'Omar', 'Pacha',
        'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya', 'Zaki', 'Arif',
        'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim', 'Jamshed', 'Khalilullah',
        'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah', 'Tajuddin', 'Usman',
        'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar', 'Eid', 'Farooz',
        'Herati', 'Kabuli', 'Mazar', 'Nangarhari', 'Panjshiri', 'Parwani', 'Samarqandi', 'Wardaki', 'Badakhshi',
        'Balkhi',
        'Dari', 'Farsi', 'Ghazni', 'Hazarajat', 'Istalif', 'Jowzjan', 'Kunar', 'Logar', 'Maimana', 'Nimruz',
        'Oruzgan', 'Parwan', 'Qandahar', 'Rostaq', 'Sarobi', 'Takhar', 'Uruzgan', 'Waras', 'Yawan', 'Zaranj',
        'Ahmadi', 'Alavi', 'Bahrami', 'Davlat', 'Emami', 'Farahi', 'Gulistani', 'Hashemi', 'Ibrahimi', 'Jafari',
        'Kazemi', 'Lahori', 'Mahdavi', 'Nasiri', 'Omidi', 'Parvizi', 'Qasemi', 'Rahimi', 'Sadeghi', 'Tavakoli',
        'Vahidi', 'Wahidi', 'Yazdani', 'Zamani', 'Abidi', 'Barani', 'Chaman', 'Danesh', 'Esfahani', 'Fahim',
        'Gharibi', 'Hosseini', 'Izadi', 'Jalali', 'Kermani', 'Lashgari', 'Mashhadi', 'Nadiri', 'Omidvar', 'Pour',
        'Qobadi', 'Rashidi', 'Shirazi', 'Tabrizi', 'Vahedi', 'Wahdat', 'Yaghoubi', 'Zahedi', 'Abbasi', 'Bonyadi',
        'Chitsaz', 'Dehqani', 'Eftekhari', 'Fouladi', 'Gorgani', 'Hamidi', 'Isfandiyari', 'Javan', 'Karimi', 'Lari',
        'Mojaddedi', 'Nabawi', 'Ostadi', 'Pahlavan', 'Qazvini', 'Ranjbar', 'Saberi', 'Tehrani', 'Vaziri', 'Waseqi',
        'Yasini', 'Zand', 'Ashna', 'Bahar', 'Choubineh', 'Daryaee', 'Ebrahimi', 'Farrokh', 'Golestani', 'Hakimi',
        'Iraj', 'Javanmard', 'Khorasani', 'Lavasan', 'Mirdamadi', 'Nouri', 'Ostad', 'Pirzadeh', 'Qomi', 'Rostami',
        'Safavi', 'Tousi', 'Vafaei', 'Wahhabi', 'Yousefi', 'Zarrabi', 'Abrishami', 'Bakhtiari', 'Chamran', 'Dolatabadi',
        'Eshghi', 'Faramarzi', 'Goudarzi', 'Hamedani', 'Imani', 'Jahan', 'Kashani', 'Lahijani', 'Mofidi', 'Nazari',
        'Olia', 'Pishva', 'Qashqai', 'Rahmani', 'Safari', 'Taba', 'Vahdati', 'Wahdat', 'Yazdi', 'Zarif',
        'Amini', 'Bozorg', 'Cheraghi', 'Darvish', 'Eskandari', 'Fars', 'Ghasemi', 'Hekmat', 'Ishraqi', 'Javid',
        'Khalaj', 'Lashkari', 'Moghadam', 'Nazemi', 'Oveisi', 'Pouya', 'Qahraman', 'Rashid', 'Sajjadi', 'Tajik',
        'Vafadar', 'Wafai', 'Yaghouti', 'Zakeri', 'Akbari', 'Bijan', 'Chooka', 'Daneshvar', 'Eshraghi', 'Fazeli',
        'Gilan', 'Haghighi', 'Irani', 'Jalili', 'Khomeini', 'Lotfi', 'Moshiri', 'Nadimi', 'Ostad', 'Parsi',
        'Qavami', 'Ranjbar', 'Salami', 'Tavassoli', 'Vaziri', 'Wafadar', 'Yazdan', 'Zarghami', 'Ardabili', 'Bahar',
        'Chitsaz', 'Deilami', 'Ebrahimi', 'Farahani', 'Gilan', 'Hosseinzadeh', 'Izadi', 'Jahanbin', 'Kashani',
        'Lashgari',
        'Mansouri', 'Nadimi', 'Ostad', 'Pahlavi', 'Qazvini', 'Rahnavard', 'Sadegh', 'Tabatabaei', 'Vahidi', 'Wahdat',
        'Yazdani', 'Zamani', 'Ahmadi', 'Bani', 'Chaman', 'Dari', 'Esfandiari', 'Farrokh', 'Gholami', 'Hashemi',
        'Imani', 'Jafari', 'Kazemi', 'Lahori', 'Mahdavi', 'Nasiri', 'Omidi', 'Parvizi', 'Qasemi', 'Rahimi',
        'Sadeghi', 'Tavakoli', 'Vahidi', 'Wahidi', 'Yazdani', 'Zamani', 'Abidi', 'Barani', 'Chaman', 'Danesh',
        'Esfahani', 'Fahim', 'Gharibi', 'Hosseini', 'Izadi', 'Jalali', 'Kermani', 'Lashgari', 'Mashhadi', 'Nadiri',
        'Omidvar', 'Pour', 'Qobadi', 'Rashidi', 'Shirazi', 'Tabrizi', 'Vahedi', 'Wahdat', 'Yaghoubi', 'Zahedi',
        'Abbasi', 'Bonyadi', 'Chitsaz', 'Dehqani', 'Eftekhari', 'Fouladi', 'Gorgani', 'Hamidi', 'Isfandiyari', 'Javan',
        'Karimi', 'Lari', 'Mojaddedi', 'Nabawi', 'Ostadi', 'Pahlavan', 'Qazvini', 'Ranjbar', 'Saberi', 'Tehrani',
        'Vaziri', 'Waseqi', 'Yasini', 'Zand', 'Ashna', 'Bahar', 'Choubineh', 'Daryaee', 'Ebrahimi', 'Farrokh',
        'Golestani', 'Hakimi', 'Iraj', 'Javanmard', 'Khorasani', 'Lavasan', 'Mirdamadi', 'Nouri', 'Ostad', 'Pirzadeh',
        'Qomi', 'Rostami', 'Safavi', 'Tousi', 'Vafaei', 'Wahhabi', 'Yousefi', 'Zarrabi', 'Abrishami', 'Bakhtiari',
        'Chamran', 'Dolatabadi', 'Eshghi', 'Faramarzi', 'Goudarzi', 'Hamedani', 'Imani', 'Jahan', 'Kashani', 'Lahijani',
        'Mofidi', 'Nazari', 'Olia', 'Pishva', 'Qashqai', 'Rahmani', 'Safari', 'Taba', 'Vahdati', 'Wahdat',
        'Yazdi', 'Zarif', 'Amini', 'Bozorg', 'Cheraghi', 'Darvish', 'Eskandari', 'Fars', 'Ghasemi', 'Hekmat',
        'Ishraqi', 'Javid', 'Khalaj', 'Lashkari', 'Moghadam', 'Nazemi', 'Oveisi', 'Pouya', 'Qahraman', 'Rashid',
        'Sajjadi', 'Tajik', 'Vafadar', 'Wafai', 'Yaghouti', 'Zakeri', 'Akbari', 'Bijan', 'Chooka', 'Daneshvar',
        'Eshraghi', 'Fazeli', 'Gilan', 'Haghighi', 'Irani', 'Jalili', 'Khomeini', 'Lotfi', 'Moshiri', 'Nadimi',
        'Ostad', 'Parsi', 'Qavami', 'Ranjbar', 'Salami', 'Tavassoli', 'Vaziri', 'Wafadar', 'Yazdan', 'Zarghami'
    ]

    male_first_names = [
        'Ahmad', 'Mohammad', 'Abdullah', 'Noorullah', 'Khalid', 'Rahim', 'Farid', 'Nasir', 'Jamal', 'Tariq',
        'Wali', 'Yusuf', 'Zahir', 'Bashir', 'Daoud', 'Faisal', 'Gul', 'Hamid', 'Ismail', 'Javed',
        'Karim', 'Latif', 'Massoud', 'Noor', 'Omar', 'Qadir', 'Rashid', 'Safi', 'Talib', 'Wahid',
        'Baryalai', 'Spin', 'Tor', 'Zmarak', 'Khostai', 'Wazir', 'Miran', 'Sangar', 'Shinwari', 'Ghilzai',
        'Amanullah', 'Aziz', 'Bashir', 'Dawood', 'Ehsan', 'Fahim', 'Ghulam', 'Habib', 'Ibrahim', 'Jalal',
        'Kabeer', 'Lutfullah', 'Mansoor', 'Naim', 'Obaid', 'Pacha', 'Qais', 'Rahmat', 'Sattar', 'Tawab',
        'Umar', 'Valli', 'Wais', 'Yaqub', 'Zabi', 'Abdul', 'Ataullah', 'Bismillah', 'Chaman', 'Dastagir',
        'Ezat', 'Farooz', 'Ghaus', 'Hafiz', 'Inayat', 'Jahan', 'Khalil', 'Lal', 'Matin', 'Nazar',
        'Omar', 'Pir', 'Qurban', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
        'Zaman', 'Amin', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
        'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
        'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
        'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
        'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
        'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
        'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
        'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
        'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek',
        'Omar', 'Pacha', 'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya',
        'Zaki', 'Arif', 'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim',
        'Jamshed', 'Khalilullah', 'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah',
        'Tajuddin', 'Usman', 'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar',
        'Eid', 'Farooz', 'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar',
        'Obaidullah', 'Pacha', 'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
        'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
        'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
        'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
        'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
        'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
        'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
        'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
        'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
        'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek',
        'Omar', 'Pacha', 'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya',
        'Zaki', 'Arif', 'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim',
        'Jamshed', 'Khalilullah', 'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah',
        'Tajuddin', 'Usman', 'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar',
        'Eid', 'Farooz', 'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar',
        'Obaidullah', 'Pacha', 'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
        'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
        'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
        'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
        'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
        'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
        'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
        'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
        'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
        'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek',
        'Omar', 'Pacha', 'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya',
        'Zaki', 'Arif', 'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim',
        'Jamshed', 'Khalilullah', 'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah',
        'Tajuddin', 'Usman', 'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar',
        'Eid', 'Farooz', 'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar',
        'Obaidullah', 'Pacha', 'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
        'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
        'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
        'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
        'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
        'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
        'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
        'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
        'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
        'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek',
        'Omar', 'Pacha', 'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya',
        'Zaki', 'Arif', 'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim',
        'Jamshed', 'Khalilullah', 'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah',
        'Tajuddin', 'Usman', 'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar',
        'Eid', 'Farooz', 'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar',
        'Obaidullah', 'Pacha', 'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
        'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
        'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
        'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
        'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
        'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
        'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
        'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
        'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
        'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek',
        'Omar', 'Pacha', 'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya',
        'Zaki', 'Arif', 'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim',
        'Jamshed', 'Khalilullah', 'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah',
        'Tajuddin', 'Usman', 'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar',
        'Eid', 'Farooz', 'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar',
        'Obaidullah', 'Pacha', 'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
        'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
        'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
        'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
        'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
        'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
        'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
        'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
        'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
        'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek',
        'Omar', 'Pacha', 'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya',
        'Zaki', 'Arif', 'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim',
        'Jamshed', 'Khalilullah', 'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah',
        'Tajuddin', 'Usman', 'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar',
        'Eid', 'Farooz', 'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar',
        'Obaidullah', 'Pacha', 'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
        'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas','Abasin', 'Abdul',
        'Ahmed', 'Aimal', 'Ali', 'Alam', 'Alamzeb', 'Amail', 'Amu', 'Andam', 'Angar', 'Armaghan', 'Arman', 'Arsalan',
        'Aryan', 'Asfand', 'Asfandyar', 'Atal', 'Atsak', 'Aurang', 'Awalmir', 'Azlan', 'Azmaray', 'Babak', 'Babrak',
        'Bacha', 'Badam', 'Bahram', 'Bahramand', 'Bahrawar', 'Bakht', 'Bakht Rawan', 'Bakht Awar', 'Balach', 'Balay',
        'Barlas', 'Baryal', 'Baryalai', 'Baseer', 'Batoor', 'Baz', 'Bazgar', 'Bazir', 'Behroz', 'Beltoon', 'Beroj',
        'Chargul', 'Chinar', 'Dagar', 'Darab', 'Darman', 'Darwesh', 'Darya', 'Daryab', 'Daulat', 'Dawar', 'Diar',
        'Dilawar', 'Droon', 'Elam', 'Farhang', 'Farihund', 'Gahez', 'Gedi', 'Ghairat', 'Ghakhtalay', 'Ghalji', 'Ghamay',
        'Gharsanay', 'Ghatool', 'Ghazan', 'Ghazin', 'Ghorzang', 'Ghunchagul', 'Ghurghusht', 'Gogal', 'Gorbat', 'Grant',
        'Gul', 'Gul Baz', 'Gul Jan', 'Gul Mast', 'Gul Rang', 'Gul Yar', 'Gul Zaman', 'Gulab', 'Gulzar', 'Hask',
        'Helmand', 'Hewand', 'Hukam', 'Izat', 'Janan', 'Janat Gul', 'Jandol', "Kakay'", 'Karlani', 'Karmal', 'Karwan',
        'Khagalay', 'Khaista', 'Khak', 'Khalo', 'Khan', 'Khandawar', 'Khialay', 'Khog', 'Khushal', 'Khushdil',
        'Khwazun', 'Khyber', 'Kochai', 'Kushan', 'Lajbar', 'Lashkar', 'Lal', 'Lawang', 'Lawangin', 'Lmar', 'Liwal',
        'Mairanay', 'Maiwand', 'Malang', 'Malook', 'Malyar', 'Manan', 'Mangal', 'Marghoz', 'Marjan', 'Marwand',
        'Mashal', 'Mateen', 'Mehtar', 'Minatbar', 'Mirwais', 'Mirzal', 'Mohambar', 'Muhammad', 'Nang', 'Nangial',
        'Noomyalay', 'Nufail', 'Olas', 'Olasyar', 'Paiman', 'Pamir', 'Pashtoon', 'Pason', 'Pasoon', 'Patang', 'Patman',
        'Patwal', 'Patyal', 'Paywastun', 'Pelabo', 'Perzo', 'Pohand', 'Pordal', 'Powneda', 'Psarlay', 'Qajeer Gul',
        'Qalandar', 'Rahamdil', 'Rangeen', 'Reday', 'Reshteen', 'Roshan', 'Rustam', 'Sabawoon', 'Sadin', 'Sahar',
        'Sahar Gul', 'Sahim', 'Saifur', 'Salar', 'Samandar', 'Samoon', 'Samsor', 'Sangar', 'Sangin', 'Sangrez',
        'Sanobar', 'Sarban', 'Sarbaz', 'Sardar', 'Sartor', 'Sayel', 'Selab', 'Selani', 'Shahsawar', 'Shahzar', 'Shamal',
        'Shamshad', 'Sher', 'Sherdil', 'Sherin', 'Shin Gul', 'Shindi Gul', 'Shino', 'Shpol', 'Shpoon', 'Shuja',
        'Sibghatullah', 'Sifat', 'Sikandar', 'Sohrab', 'Sparlay', 'Spetselay', 'Spin', 'Spin Gul', 'Spinzar', 'Storay',
        'Sur Gul', 'Suweil', 'Syal', 'Taban', 'Tanim', 'Taroon', 'Tawas', 'Teri', 'Tofan', 'Tolwak', 'Tor Gul',
        'Toryal', 'Toti', 'Turan', 'Turialai', 'Wadaan', 'Wais', 'Wakdar', 'Wakman', 'Wali', 'Yama', 'Yaqut', 'Yoon',
        'Zafran', 'Zalaan', 'Zaland', 'Zalmay', 'Zapran', 'Zar Gul', 'Zarwali', 'Zarak', 'Zaram', 'Zarang', 'Zarbat',
        'Zardab', 'Zardad', 'Zargar', 'Zarghun', 'Zarhawar', 'Zarhgay', 'Zarin', 'Zarkanay', 'Zarlesh', 'Zarmast',
        'Zarnosh', 'Zaryab', 'Zawaar', 'Zawar', 'Zgard', 'Ziar', 'Ziarmal', 'Zigar', 'Zmarak', 'Zmaray', 'Zorak',
        'Zorawar', 'Zwak', 'Zwandun', 'Afia', 'Aghala', 'Ambrin', 'Angeza', 'Anar', 'Ara', 'Apana', 'Aryana', 'Badrai',
        'Bakht Awara', 'Bala Nashta', 'Balbala', 'Banafsha', 'Barsala', 'Bazira', 'Benazira', 'Bibi', 'Bibi Rokhana',
        'Brekhna', 'Diwa', 'Durkhanai', 'Farishta', 'Gabina', 'Galai', 'Ghatola', 'Ghorashka', 'Ghotai', 'Ghuncha',
        'Gorgora', 'Grana', 'Gul Bano', 'Gul Ghotai', 'Gul Lakhta', 'Gul Makai', 'Gul Mina', 'Gul Panrha', 'Gul Sangha',
        'Gul Warin', 'Gulalai', 'Gulchin', 'Gulnar', 'Hala', 'Helai', 'Hila', 'Hina', 'Husay', 'Kashmala', 'Khaista',
        'Khaperai', 'Kharo', 'Khatol', 'Khkulay', 'Khush Bakhta', 'Khwaga', 'Kochai', 'Kontara', 'Laila', 'Lailuma',
        'Lakhta', 'Lalma', 'Lalzari', 'Lamba', 'Lawanga', 'Lema', 'Mahjabin', 'Mahnur', 'Mahzala', 'Malalai',
        'Malghalara', 'Mina', 'Mukai', 'Munawara', 'Murchakai', 'Muska', 'Naghma', 'Nangialai', 'Narenja', 'Natkai',
        'Nawyata', 'Nazanina', 'Nazdana', 'Nazo', 'Niazmina', 'Orbakhta', 'Orbala', 'Orzala', 'Palwasha', 'Panra',
        'Parghunda', 'Pariwash', 'Parkha', 'Pashmina', 'Patasa', 'Peghra', 'Perkha', 'Pokha', 'Ranrha', 'Rayan',
        'Rekhmina', 'Reshtina', 'Roshina', 'Saba', 'Salgay', 'Sandara', 'Sanga', 'Sangina', 'Selai', 'Senzela',
        'Shahgalay', 'Shahay', 'Shahlalai', 'Shamla', 'Shandana', 'Shanzai', 'Shaperai', 'Shastai', 'Shazmina',
        'Sherin', 'Shinkai', 'Shinogai', 'Shughla', 'Spalmay', 'Sparghai', 'Spezala', 'Spozmai', 'Storai', 'Tabana',
        'Talwasa', 'Tanima', 'Tor Pikai', 'Ugay', 'Wadaana', 'Wagma', 'Wahida', 'Wajia', 'Warda', 'Wawrina', 'Wranga',
        'Wreshmin', 'Zainba', 'Zaituna', 'Zakia', 'Zala', 'Zalanda', 'Zaloba', 'Zamba', 'Zar Bibi', 'Zar Masta',
        'Zar Mina', 'Zar Wareen', 'Zarbaha', 'Zareena', 'Zareesh', 'Zarghuna', 'Zarka', 'Zar Lakhta', 'Zar Sanga',
        'Zarshala', 'Zartaj', 'Zhala', 'Zhalai', 'Zohal', 'Zufash'
    ]

    female_first_names = [
        'Mariam', 'Fatima', 'Zahra', 'Laila', 'Nadia', 'Sabrina', 'Soraya', 'Parwin', 'Shukria', 'Fereshta',
        'Hadia', 'Jamila', 'Kamila', 'Nargis', 'Razia', 'Safia', 'Tamanna', 'Wajiha', 'Yasmin', 'Zarmina',
        'Gulalai', 'Mairman', 'SpinGul', 'Torpekai', 'Wazhma', 'Shamsia', 'Naghma', 'Mishal', 'Sanga', 'Zarghuna',
        'Aisha', 'Bibi', 'Chaman', 'Dilafroz', 'Emaan', 'Farahnaz', 'Gul', 'Hadiya', 'Iram', 'Jahanara',
        'Khadija', 'Lalzari', 'Mahnaz', 'Nabila', 'Ozra', 'Parwana', 'Qamar', 'Rahila', 'Sahar', 'Tabasum',
        'Uzma', 'Vida', 'Wahida', 'Yalda', 'Zainab', 'Afsana', 'Bakht', 'Chaman', 'Durdana', 'Eram',
        'Fauzia', 'Gulshan', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah',
        'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa',
        'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara',
        'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid', 'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima',
        'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba', 'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham',
        'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya', 'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana',
        'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera', 'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha',
        'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman', 'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat',
        'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima', 'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara',
        'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara', 'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema',
        'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria', 'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah',
        'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem', 'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen',
        'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram', 'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah',
        'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah', 'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira',
        'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa', 'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal',
        'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara', 'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid',
        'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima', 'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba',
        'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham', 'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya',
        'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana', 'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera',
        'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha', 'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman',
        'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat', 'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima',
        'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara', 'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara',
        'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema', 'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria',
        'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah', 'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem',
        'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen', 'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram',
        'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah',
        'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa',
        'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara',
        'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid', 'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima',
        'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba', 'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham',
        'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya', 'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana',
        'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera', 'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha',
        'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman', 'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat',
        'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima', 'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara',
        'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara', 'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema',
        'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria', 'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah',
        'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem', 'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen',
        'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram', 'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah',
        'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah', 'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira',
        'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa', 'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal',
        'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara', 'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid',
        'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima', 'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba',
        'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham', 'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya',
        'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana', 'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera',
        'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha', 'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman',
        'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat', 'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima',
        'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara', 'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara',
        'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema', 'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria',
        'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah', 'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem',
        'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen', 'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram',
        'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah',
        'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa',
        'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara',
        'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid', 'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima',
        'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba', 'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham',
        'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya', 'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana',
        'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera', 'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha',
        'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman', 'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat',
        'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima', 'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara',
        'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara', 'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema',
        'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria', 'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah',
        'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem', 'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen',
        'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram', 'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah',
        'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah', 'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira',
        'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa', 'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal',
        'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara', 'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid',
        'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima', 'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba',
        'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham', 'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya',
        'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana', 'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera',
        'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha', 'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman',
        'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat', 'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima',
        'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara', 'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara',
        'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema', 'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria',
        'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah', 'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem',
        'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen', 'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram',
        'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah',
        'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa',
        'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara',
        'Afia', 'Badrai', 'Diwa', 'Farishta', 'Gabina', 'Hala', 'Kashmala', 'Laila', 'Mahjabin',
        'Naghma', 'Orbakhta', 'Palwasha', 'Ranrha', 'Saba', 'Tabana', 'Ugay', 'Wadaana', 'Zainba'
    ]



    domains = [
        "gmail.com", "yahoo.com", "outlook.com", "afghanmail.com", "mail.com"
    ]




    # ---------- BASIC PARTS ----------
    def username(self, gender=None):
        """Random Afghan-style username"""
        if self.first_names == "ښځينه":
            first = random.choice(self.female_first_names).lower()
        elif gender == "نارينه":
            first = random.choice(self.male_first_names).lower()
        else:
            first = random.choice(self.male_first_names + self.female_first_names).lower()

        last = random.choice(self.last_names_email).lower()
        number = str(random.randint(1, 999))
        return f"{first}.{last}{number}"

    def email(self, gender=None):
        """Full email address"""
        return f"{self.username(gender)}@{random.choice(self.domains)}"

        # =================End of the email section ==============

    def first_name_male(self):
        first = random.choice(self.pashto_male_first_names)
        return first

    def first_name_female(self):
        firstFemale = random.choice(self.pashto_female_first_names)
        return firstFemale

    def last_name(self):
        last = random.choice(self.last_names)
        return last

    def first_name(self):
        return random.choice([self.first_name_male(), self.first_name_female()])

    # ---------- FULL NAME ----------

    def name(self):


        firstName = self.first_name()

        if firstName in self.pashto_male_first_names:
            prefix = random.choice(self.prefixes_male)
            first = firstName
        else:
            prefix = random.choice(self.prefixes_female)
            first = firstName

        last = self.last_name()

        return f"{prefix} {first} {last} "








