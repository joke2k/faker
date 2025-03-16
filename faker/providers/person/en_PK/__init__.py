from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ("{{first_name}} {{last_name}}",)

    # First names are from
    #   https://mummyname.net/pakistani-boy-names/
    # Last names are from https://mummyname.net/pakistani-boy-names/

    first_names = (
        "Ali",
        "Arham",
        "Aryan",
        "Ayaan",
        "Faizan",
        "Hamza",
        "Huzaifa",
        "Rayan",
        "Rohaan",
        "Atfat",
        "Atheel",
        "Attaf",
        "Auraq",
        "Awadil",
        "Awamil",
        "Awamiri",
        "Awan",
        "Awani",
        "Awj",
        "Awlya",
        "Awmar",
        "Awrad",
        "Ayamin",
        "Aysar",
        "Ayyubi",
        "Azban",
        "Azeeb",
        "Baashir",
        "Badawi",
        "Bairbel",
        "Bambad",
        "Berezat",
        "Birousk",
        "Bizhan",
        "Buraid",
        "Chamali",
        "Changaz",
        "Charlesh",
        "Chashida",
        "Chawish",
        "Cheragh",
        "Darain",
        "Dastageer",
        "Dayyaan",
        "Durab",
        "Ejlaal",
        "Elaf",
        "Esfandyar",
        "Etizaaz",
        "Fahmi",
        "Fazli",
        "Fidvi",
        "Ghazanfer",
        "Gulfaam",
        "Guney",
        "Harnail",
        "Hazeem",
        "Kachela",
        "Khaan",
        "Mizhir",
        "Mourib",
        "Muhallil",
        "Muhazzim",
        "Muzdahir",
        "Muzhir",
        "Rusul",
        "Ruwaihim",
        "Samama",
        "Souma",
        "Tadeen",
        "Tafazal",
        "Tahmaseb",
        "Tahoor",
        "Taial",
        "Taisir",
        "Tarfaan",
        "Tawkeel",
        "Tirdad",
        "Tishk",
        "Urrab",
        "Vahar",
        "Xobeen",
        "Yadid",
        "Yafir",
        "Yamar",
        "Yashem",
        "Yazan",
        "Yazeed",
        "Yeraz",
        "Yergha",
        "Yesoob",
        "Yureed",
        "Zabir",
        "Zahaar",
        "Zahri",
        "Zahrun",
        "Zahur",
        "Zarar",
        "Zauqi",
        "Zaweel",
        "Zayan",
        "Zayyir",
        "Zerdad",
        "Zewad",
        "Zimran",
        "Zuwayhir",
        "Adil",
        "Aaaqil",
        "Aaban",
        "Aabid",
        "Aabid",
        "Aadam",
        "Aadil",
        "Aadil",
        "Aadil",
        "Aafiya",
        "Aahil",
        "Aalam",
        "Aalam",
        "Aalee",
        "Aalim",
        "Aamil",
        "Aamir",
        "Aamir",
        "Aamir",
        "Aamirah",
        "Aaqil",
        "Aarif",
        "Aarif",
        "Aarif",
        "Aariz",
        "Aaryan",
        "Aashif",
        "Aashir",
        "Aasif",
        "Aasif",
        "Aasim",
        "Aasim",
        "Aasim",
        "Aatif",
        "Aatiq",
        "Aaus",
        "Aayan",
        "Aazim",
        "Abaan",
        "Baahir",
        "Baaizeed",
        "Baaqee",
        "Baaqir",
        "Baaree",
        "Baasim",
        "Baasit",
        "Babar",
        "Baber",
        "Badr",
        "Badr Udeen",
        "Baha",
        "Baha Udeen",
        "Bahaa",
        "Bahiy Udeen",
        "Baleegh",
        "Baqar",
        "Baqir",
        "Barr",
        "Barraq",
        "Basaam",
        "Baseer",
        "Basel",
        "Basem",
        "Bashaar",
        "Bashaarat",
        "Bashar",
        "Basharat",
        "Basheer",
        "Basheerah",
        "Basil",
        "Basim",
        "Basir",
        "Bassam",
        "Batal",
        "Batool",
        "Bazam",
        "Bilaal",
        "Bilal",
        "Dawud",
        "Daamin",
        "Daanish",
        "Daanyaal",
        "Daawood",
        "Dabbah",
        "Dabir",
        "Daghfal",
        "Daiyaan",
        "Dakhil",
        "Dameer",
        "Damurah",
        "Daniel",
        "Danish",
        "Eesaa",
        "Ehan",
        "Ehsaas",
        "Ehsan",
        "Eijaz",
        "Ejaz",
        "El-Amin",
        "Emran",
        "Eshan",
        "Ghaalib",
        "Ghaazi",
        "Ghaffaar",
        "Ghafoor",
        "Ghaith",
        "Ghalib",
        "Ghanee",
        "Ghanem",
        "Ghannam",
        "Ghasaan",
        "Ghauth",
        "Ghauth",
        "Ghawth",
        "Ghayoor",
        "Ghazalan",
        "Ghazanfar",
        "Ghazawan",
        "Ghazi",
        "Ghazzal",
        "Ghiyaath",
        "Ghiyath",
        "Ghufran",
        "Ghulaam",
        "Ghulam",
        "Ghunayn",
        "Ghusharib",
        "Ghusun",
        "Ghutayf",
        "Gohar",
        "Gulab",
        "Gulfam",
        "Gulshan",
        "Gulzar",
        "Izaaz",
        "Ibaad",
        "Ibn",
        "Ibraaheem",
        "Ibraheem",
        "Ibrahim",
        "Idrees",
        "Idrees",
        "Idris",
        "Iesa",
        "Iftikhaar",
        "Iftikhar",
        "Ihab",
        "Ihsaan",
        "Ihsaan",
        "Ihsan",
        "Ihtesham",
        "Ihtiram",
        "Ihtishaam",
        "Ihtsham",
        "Ijli",
        "Ikhlaas",
        "Ikraam",
        "Ikramah",
        "Ikrimah",
        "Ikrimah",
        "Ilan",
        "Jafar",
        "Jaabir",
        "Jaabir",
        "Jaafar",
        "Jaan",
        "Jabbaar",
        "Jabir",
        "Jabr",
        "Jad",
        "Jafar",
        "Jaffer",
        "Jahangir",
        "Jahanzeb",
        "Jahdami",
        "Jahdari",
        "Jahiz",
        "Jahm",
        "Jalaal",
        "Jalaal",
        "Jalal",
        "Jalees",
        "Jalil",
        "Jamaal",
        "Jamaal",
        "Jamaal Udeen",
        "Jamal",
        "Jameel",
        "Jameel",
        "Kaamil",
        "Kaamil",
        "Kaamil",
        "Kaashif",
        "Kaazim",
        "Kabeer",
        "Kabeer",
        "Kafeel",
        "Kaiser",
        "Kajji",
        "Kalbi",
        "Kaleem",
        "Kaleem",
        "Kaleema",
        "Kamal",
        "Kamal",
        "Kamil",
        "Kamran",
        "Karaamat",
        "Karam",
        "Kareem",
        "Kareem",
        "Karim",
        "Kasam",
        "Kashan",
        "Kashif",
        "Kasim",
        "Kauthar",
        "Kawkab",
        "Kawthar",
        "Kaysan",
        "Kazi",
        "Kazim",
        "Keyaan",
        "Khaalid",
        "Laeeq",
        "Labeeb",
        "Labeeb",
        "Labib",
        "Lahiah",
        "Laiq",
        "Laith",
        "Lajlaj",
        "Laqeet",
        "Lateef",
        "Lateef",
        "Latif",
        "Layth",
        "Liban",
        "Limazah",
        "Liyaaqat",
        "Liyaqat",
        "Loot",
        "Luay",
        "Luqmaan",
        "Luqmaan",
        "Luqman",
        "Lut",
        "Lutf",
        "Lutf",
        "Lutfi",
        "Lutfi",
        "Maawiya",
        "Mad",
        "Mamun",
        "Man",
        "Man",
        "Maroof",
        "Maahir",
        "Maajid",
        "Maalik",
        "Maaz",
        "Maazin",
        "Mabad",
        "Madani",
        "Madiyan",
        "Madyan",
        "Mahad",
        "Mahaz",
        "Mahbeer",
        "Mahboob",
        "Mahbub",
        "Mahdee",
        "Mahdi",
        "Mahdy",
        "Maheen",
        "Maher",
        "Mahfooz",
        "Mahfuj",
        "Mahfuz",
        "Mahja",
        "Mahmood",
        "Mahmoud",
        "Mahmud",
        "Majd",
        "Majd",
        "Majd Udeen",
        "Majdi",
        "Majdy",
        "Majeed",
        "Makeen",
        "Nail",
        "Naail",
        "Naadir",
        "Naadir",
        "Naajy",
        "Naasih",
        "Naasir",
        "Naathim",
        "Naazhim",
        "Nabeeh",
        "Nabeel",
        "Nabeel",
        "Nabeel",
        "Nabhan",
        "Nabhan",
        "Nabigh",
        "Nabih",
        "Nabil",
        "Nadeem",
        "Nadeem",
        "Nadhir",
        "Nadim",
        "Nadir",
        "Nadr",
        "Naeem",
        "Naeem",
        "Nafasat",
        "Nafees",
        "Nafees",
        "Nafesa",
        "Nafis",
        "Naib",
        "Naim",
        "Najair",
        "Najam",
        "Najam",
        "Najeeb",
        "Najeeb",
        "Najeeb",
        "Obaid",
        "Omair",
        "Omar",
        "Omar",
        "Omeir",
        "Omran",
        "Osama",
        "Ossama",
        "Owais",
        "Parsa",
        "Parvez",
        "Pervaiz",
        "Qaadir",
        "Qaadir",
        "Qaasim",
        "Qabeel",
        "Qadar",
        "Qadeer",
        "Qadeer",
        "Qadi",
        "Qadim",
        "Qahtan",
        "Qaim",
        "Qais",
        "Qamar",
        "Qani",
        "Qanit",
        "Qareeb",
        "Qaseem",
        "Qasid",
        "Qasif",
        "Qasim",
        "Qatadah",
        "Qatadah",
        "Qawee",
        "Qawee",
        "Qay-yoom",
        "Qays",
        "Quadir",
        "Qudamah",
        "Qudamah",
        "Quddoos",
        "Qudoos",
        "Qurban",
        "Qusay",
        "Qutaybah",
        "Qutaybah",
        "Qutb",
        "Qutub",
        "Raed",
        "Raid",
        "Raaghib",
        "Raahil",
        "Raakin",
        "Raamis",
        "Raamiz",
        "Raamiz",
        "Raashid",
        "Raashid",
        "Raatib",
        "Rabah",
        "Rabah",
        "Rabar",
        "Rabb",
        "Rabbaanee",
        "Rabbani",
        "Rabee",
        "Rabee",
        "Rabiah",
        "Rabit",
        "Radhee",
        "Radi",
        "Raees",
        "Rafan",
        "Rafay",
        "Rafee",
        "Rafee",
        "Rafeek",
        "Rafeeq",
        "Rafi",
        "Rafiq",
        "Ragheb",
        "Raghib",
        "Rahat",
        "Raheel",
        "Raheem",
        "Sad",
        "Sadan",
        "Said",
        "Saim",
        "Sair",
        "Sairah",
        "Saood",
        "Saabir",
        "Saabir",
        "Saad",
        "Saad",
        "Saadat",
        "Saadiq",
        "Saafir",
        "Saahir",
        "Saahir",
        "Saaiq",
        "Saajid",
        "Saajid",
        "Saal",
        "Saalih",
        "Saalim",
        "Saaqib",
        "Saariyah",
        "Sabah",
        "Sabahat",
        "Sabbir",
        "Sabeeh",
        "Sabeeh",
        "Sabeeh",
        "Sabil",
        "Sabiq",
        "Sabir",
        "Saboor",
        "Sabur",
        "Saburah",
        "Sadan",
        "Sadaqat",
        "Sadeed",
        "Taahaa",
        "Taahir",
        "Taahir",
        "Taaj",
        "Taalib",
        "Taamir",
        "Taanish",
        "Taariq",
        "Taban",
        "Tabassum",
        "Tabassum",
        "Tabish",
        "Taha",
        "Tahaw-wur",
        "Tahawwur",
        "Taheem",
        "Tahir",
        "Tahmeed",
        "Tahmid",
        "Tahseen",
        "Taimur",
        "Taj",
        "Tajammal",
        "Tajammul",
        "Tajammul",
        "Tajudinn",
        "Talal",
        "Talal",
        "Talat",
        "Talha",
        "Talha",
        "Talhah",
        "Talhah",
        "Tali",
        "Talib",
        "Tamam",
        "Tamanna",
        "Ubaadah",
        "Ubaadah",
        "Ubaadah",
        "Ubaadah",
        "Ubadah",
        "Ubadah",
        "Ubaid",
        "Ubaid",
        "Ubaidah",
        "Ubaidah",
        "Ubay",
        "Ubay",
        "Ubayd",
        "Ubayd",
        "Ubaydullah",
        "Ubaydullah",
        "Uhban",
        "Uhban",
        "Ulfat",
        "Ulfat",
        "Ulfat",
        "Umaarah",
        "Umaarah",
        "Umair",
        "Umair",
        "Umair",
        "Umair",
        "Umar",
        "Umar",
        "Umar",
        "Umar",
        "Umar",
        "Waail",
        "Waail",
        "Waahid",
        "Waahid",
        "Waajid",
        "Wadee",
        "Wadi",
        "Wadood",
        "Wafa",
        "Wafeeq",
        "Wafi",
        "Wafiq",
        "Wahab",
        "Wahb",
        "Wahban",
        "Waheed",
        "Waheed",
        "Wahhaab",
        "Wahhaaj",
        "Yaaseen",
        "Yafi",
        "Yaghnam",
        "Yahya",
        "Yahyaa",
        "Yaman",
        "Yaman",
        "Yameen",
        "Yaqeen",
        "Yaqoot",
        "Yaqub",
        "Yar",
        "Yasaar",
        "Yaseen",
        "Yasin",
        "Yasir",
        "Yasir",
        "Yathrib",
        "Yawar",
        "Yawer",
        "Zaafir",
        "Zaahid",
        "Zaahid",
        "Zaahir",
        "Zaahir",
        "Zaahir",
        "Zaakir",
        "Zackariya",
        "Zaeem",
        "Zafar",
        "Zafar",
        "Zafeer",
        "Zafir",
        "Zafrul",
        "Zaheer",
        "Zaheer",
        "Zaheer",
        "Zahi",
        "Zahir",
        "Zaib",
    )

    last_names = (
        "Lajlaj",
        "Aarif",
        "Urrab",
        "Tabassum",
        "Ubadah",
        "Daniel",
        "Umaarah",
        "Omair",
        "Jalil",
        "Aatiq",
        "Karaamat",
        "Lut",
        "Karam",
        "Aasif",
        "Aadam",
        "Mahbeer",
        "Saalim",
        "Ubayd",
        "Naail",
        "Mahfuz",
        "Ghazzal",
        "Aamir",
        "Ubaydullah",
        "Umaarah",
        "Rabiah",
        "Maawiya",
        "Yasir",
        "Raaghib",
        "Daamin",
        "Rabb",
        "Bashaar",
        "Taanish",
        "Yafir",
        "Baaree",
        "Talib",
        "Rafi",
        "Luqman",
        "Qaasim",
        "Ubaidah",
        "Saajid",
        "Yaman",
        "Ubaadah",
        "Baaqir",
        "Sadan",
        "Zarar",
        "Saafir",
        "Zafar",
        "Mahmoud",
        "Zayyir",
        "Ubay",
        "Fidvi",
        "Mahfuj",
        "Awmar",
        "Yawer",
        "Ayaan",
        "Taimur",
        "Rabbani",
        "Ayyubi",
        "Waahid",
        "Ijli",
        "Baleegh",
        "Bilaal",
        "Radi",
        "Ali",
        "Tadeen",
        "Souma",
        "Layth",
        "Kashif",
        "Labeeb",
        "Talhah",
        "Sabir",
        "Dabir",
        "Yaghnam",
        "Zackariya",
        "Ibrahim",
        "Rafeek",
        "Qadeer",
        "Luqmaan",
        "Jahdari",
        "Qabeel",
        "Kaamil",
        "Ilan",
        "Omeir",
        "Ubaid",
        "Majd",
        "Aadil",
        "Ghafoor",
        "Zahrun",
        "Tabassum",
        "Lutf",
        "Aamir",
        "Iftikhaar",
        "Naeem",
        "Ghauth",
        "Eshan",
        "Raid",
        "Qasif",
        "Ihsaan",
        "Bambad",
        "Aaaqil",
        "Nabeel",
        "Jamaal",
        "Awj",
        "Wahhaaj",
        "Nabih",
        "Jalaal",
        "Yahyaa",
        "Aalam",
        "Ghayoor",
        "Aarif",
        "Tahir",
        "Batal",
        "Talha",
        "Uhban",
        "Aryan",
        "Najam",
        "Darain",
        "Qusay",
        "Vahar",
        "Aabid",
        "Ihtiram",
        "Umar",
        "Mahbub",
        "Qaim",
        "Saajid",
        "Owais",
        "Maheen",
        "Raashid",
        "Limazah",
        "Zaafir",
        "Wadood",
        "Aariz",
        "Aalam",
        "Ihab",
        "Umair",
        "Zahri",
        "Aazim",
        "Jad",
        "Omar",
        "Majeed",
        "Qaseem",
        "Rafay",
        "Ghanee",
        "Gulshan",
        "Babar",
        "Baasim",
        "Ghunayn",
        "Jaabir",
        "Nadeem",
        "Lahiah",
        "Sair",
        "Saaqib",
        "Esfandyar",
        "Zaheer",
        "Sabil",
        "Qutaybah",
        "Azban",
        "Zafrul",
        "Awani",
        "Tajammul",
        "Auraq",
        "Man",
        "Tafazal",
        "Raed",
        "Baseer",
        "Quadir",
        "Dawud",
        "Talal",
        "Sabah",
        "Baashir",
        "Damurah",
        "Ibraaheem",
        "Faizan",
        "Zaakir",
        "Ghutayf",
        "Ehsaas",
        "Sadeed",
        "Mad",
        "Jabir",
        "Mourib",
        "Aamil",
        "Sabeeh",
        "Bizhan",
        "Barr",
        "Basaam",
        "Ghasaan",
        "Nail",
        "Kasim",
        "Taaj",
        "Omran",
        "Madiyan",
        "Taheem",
        "Saad",
        "Kamal",
        "Raatib",
        "Taj",
        "Yadid",
        "Basheerah",
        "Aasim",
        "Zahur",
        "Saabir",
        "Kasam",
        "Naeem",
        "Tawkeel",
        "Ghannam",
        "Tahmaseb",
        "Awadil",
        "Liyaaqat",
        "Tahaw-wur",
        "Tamanna",
        "Zafir",
        "Ghauth",
        "Ubay",
        "Zaahid",
        "Awamil",
        "Talat",
        "Maalik",
        "Qadar",
        "Waajid",
        "Aamirah",
        "Ayamin",
        "Kamran",
        "Kaleem",
        "Wadi",
        "Zaahid",
        "Umar",
        "Bashaarat",
        "Saal",
        "Najeeb",
        "Kachela",
        "Sabur",
        "Buraid",
        "Rabee",
        "Najeeb",
        "Yar",
        "Umar",
        "Ossama",
        "Tahawwur",
        "Zaahir",
        "Raashid",
        "Tali",
        "Batool",
        "Umair",
        "Ihsaan",
        "Majd Udeen",
        "Kaamil",
        "Raheel",
        "Abaan",
        "Rabah",
        "Jameel",
        "Gohar",
        "Aabid",
        "Zuwayhir",
        "Sadan",
        "Idris",
        "Qais",
        "Sadaqat",
        "Barraq",
        "Ejlaal",
        "Luay",
        "Jahdami",
        "Wafeeq",
        "Wafa",
        "Rabar",
        "Aasif",
        "Dakhil",
        "Jalaal",
        "Gulfam",
        "Saahir",
        "Maroof",
        "Baasit",
        "Kabeer",
        "Jameel",
        "Latif",
        "Badr Udeen",
        "Qahtan",
        "Liyaqat",
        "Jabr",
        "Kaleema",
        "Fazli",
        "Huzaifa",
        "Man",
        "Rohaan",
        "Ubadah",
        "Saburah",
        "Saariyah",
        "Kaysan",
        "Raakin",
        "Sabiq",
        "Saboor",
        "Zahaar",
        "Jaabir"
    )
