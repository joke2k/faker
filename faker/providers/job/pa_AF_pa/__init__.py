# job_provider_ps_af.py  (Pashto - ps_AF)

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """Job provider for Pashto Afghanistan locale using standard and proper Pashto terms."""

    jobs = [
        "اداکار",          # Actor
        "کپتان",           # Captain
        "والي",            # Governor
        "خیاط",            # Tailor
        "شپون",            # Shepherd / Herdsman
        "باغبان",          # Gardener
        "مؤذن",            # Muezzin
        "ساربان",          # Camel driver
        "آشپز",            # Cook
        "د غاښونو ډاکټر",  # Dentist
        "ترکاڼ",           # Carpenter
        "شپون",            # Shepherd
        "کوروالۍ",         # Housewife
        "د شورا غړی",      # Council member
        "لیکوال",          # Writer
        "ګارسون",          # Waiter
        "استاد",           # Professor
        "پلورونکی",        # Salesperson
        "ګلیزیر",          # Glazier
        "مدیر",            # Manager
        "دیوال رنګوونکی",  # House painter
        "کشتۍ کوونکی",     # Boatman
        "کوڅه پاکوونکی",   # Street sweeper
        "وزیر",            # Minister
        "پایلټ",           # Pilot
        "حجام",            # Barber
        "ملا",             # Cleric
        "متخصص",           # Specialist
        "فوټبال لوبغاړی",  # Football player
        "قصاب",            # Butcher
        "ساعت جوړونکی",    # Watchmaker
        "بقال",            # Grocer
        "ټلیفون اپریټر",   # Telephone operator
        "سوداګر",          # Merchant
        "نظر پوه",         # Optician
        "خطاط",            # Calligrapher
        "ځنګل ساتونکی",    # Forester
        "ښوونکی",          # Teacher
        "انجنیر",          # Engineer
        "چلوونکی",         # Driver
        "سینګارګر",        # Decorator
        "پوځي",            # Military personnel
        "بیکر",            # Baker
        "والي",            # Governor
        "زده کوونکی",      # Student
        "محصل",            # University student
        "میخانیک",         # Mechanic
        "بزګر",            # Farmer
        "هنرمند",          # Artist
        "مرستیال",         # Deputy
        "بانکدار",         # Banker
        "لوهار",           # Blacksmith
        "رئیس",            # President
        "بریګیډیر",        # Brigadier
        "ساتونکی",         # Caretaker
        "کارکوونکی",       # Employee
        "روزونکی",         # Trainer
        "ډګروال",          # Colonel
        "غوطه خور",        # Diver
        "ډاکټر",           # Doctor
        "دروازه ساتونکی", # Doorman
        "اور وژونکی",      # Firefighter
        "کب نیونکی",       # Fisherman
        "میوه پلورونکی",   # Fruit seller
        "ساتونکی",         # Guard
        "پولیس",           # Police officer
        "قاضي",            # Judge
        "سلاكار",          # Lawyer
        "کارګر",           # Worker
        "ښاروال",          # Mayor
        "کان کیندونکی",    # Miner
        "نرس",             # Nurse
        "افسر",            # Officer
        "عکاس",            # Photographer
        "پلمبر",           # Plumber
        "لوبغاړی",         # Actor
        "وړونکی",         # Porter
        "جمهوررئیس",      # President
        "لومړی وزیر",      # Prime Minister
        "اروا پوه",        # Psychologist
        "خبریال",          # Journalist
        "تقاعد شوی",       # Retired
        "مجسمه جوړونکی",   # Sculptor
        "سرجنټ",           # Sergeant
        "دوکاندار",        # Shopkeeper
        "موسیقار",         # Musician
        "عسکر",            # Soldier
        "ویناوال",         # Speaker
        "جراح",            # Surgeon
        "پوټټر",           # Potter
        "سیلانی",          # Tourist
        "ویلډر",           # Welder
        "د سترګو ډاکټر",    # Ophthalmologist
        "راپورټر",         # Reporter
        "محاسب",           # Accountant
        "لوبغاړی",         # Actress (female actor)
        "مدافع",           # Advocate
        "اجنټ",            # Agent
        "معمار",           # Architect
        "لیلام کونکی",     # Auctioneer
        "حلوا",            # Confectioner
        "کانسټبل",         # Constable
        "قراردادي",        # Contractor
        "رنګ",             # Dyer
        "بریښنایی",        # Electrician
        "معاینه کونکی",    # Examiner
        "ګل پلورونکی",      # Florist
        "د ځمکې خاوند",     # Landlord
        "کتابتون",         # Librarian
        "ده ژوند محافظ",   # Lifeguard
        "جادوګر",          # Magician
        "کاریګر",          # Craftsman
        "نڅاګر",           # Dancer
        "د غاښونو ډاکټر",  # Dentist (repeated for variety)
        "ډیزاینر",         # Designer
        "ډرامه جوړونکی",   # Dramatist
        "درمل جوړونکی",    # Pharmacist
        "پیلوټ",           # Pilot (repeated)
        "شاعر",            # Poet
        "پوسته",           # Postman
        "پادری",           # Priest
        "خپرونکی",         # Publisher
        "نااخت",           # Sailor
        "ساینس پوه",       # Scientist
        "منشي",            # Secretary
        "تخم",             # Seedsman
        "بوټ جوړونکی",     # Shoemaker
        "د هټۍ مرستیال",    # Shop assistant
        "سیاستوال",        # Politician
        "ژباړن",           # Translator
        "خزانه دار",       # Treasurer
        "د سفر نماینده",   # Travel agent
        "وترنری ډاکټر",    # Veterinary doctor
        "چوبړوال",         # Waiter
        "مينځل",           # Washerman
        "څارګر",           # Watchman
        "اوبدل",           # Weaver
        "زیور",            # Jeweller
        "سوداګر",          # Merchant (repeated)
        "کولی",            # Coolie
        "پاکونکی",         # Cleaner
        "کلرک",            # Clerk
        "روزونکی",         # Coachman (repeated)
        "موچی",            # Cobbler
        "راټولونکی",       # Collector
        "کمپوزونکی",       # Compositor
        "کنډکټر",          # Conductor
        "مفتش",            # Inspector
        "خبر لوستونکی",    # News reader
        "ناول لیکونکی",     # Novelist
        "تیلوونکی",        # Oilman
        "انځورګر",         # Painter
        "چپراسی",          # Peon
        "عطر",             # Perfumer
        "مالک",            # Proprietor
        "پرچون پلورونکی",   # Retailer
        "ګرځونکی",         # Turner
        "واکسین کوونکی",    # Vaccinator
        "ویټریس",          # Waitress
        "مينځل",           # Washerwoman
        "کارګران",         # Workers
    ]