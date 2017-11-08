from __future__ import unicode_literals

from ..en import Provider as AddressProvider

'''
Based on https://github.com/missbossy/Faker/tree/singapore
'''


class Provider(AddressProvider):
    city_prefixes = ()

    city_suffixes = ()

    building_number_formats = ('#####', '####', '###')
    postcode_formats = ('######',)

    city_formats = (
        '{{city_prefix}} {{first_name}}{{city_suffix}}',
        '{{city_prefix}} {{first_name}}',
        '{{first_name}}{{city_suffix}}',
        '{{last_name}}{{city_suffix}}'
    )

    street_suffixes = (
    'Avenue', 'Avenue North', 'Center', 'Circle', 'Court', 'Crescent', 'Drive', 'Estate', 'Field', 'Gate', 'Garden',
    'Green', 'Heights', 'Hill', 'Junction', 'Lane', 'Park', 'Point', 'Road', 'Terrace', 'View', 'Vista', 'Walk')

    street_name_formats = ('{{town}} {{street_suffix}}',)

    street_address_formats = (
        '{{block}} {{lorong}} {{town}} {{flat_number_prefix}}-{{flat_number_suffix}}',
        '{{block}} {{major_estate}} {{sg_street}} {{flat_number_prefix}}-{{flat_number_suffix}}',
        '{{block}} {{major_estate}} {{sg_street}} {{flat_number_prefix}}-{{flat_number_suffix}}',
        '{{block}} {{major_estate}} {{sg_street}} {{flat_number_prefix}}-{{flat_number_suffix}}',
        '{{street_number}} Jalan {{jalan_place}}',
        '{{street_number}} {{street_name}} {{flat_number_prefix}}-{{flat_number_suffix}}',
        '{{street_number}} {{street_name}}',
        '{{street_number}}',
        '{{street_name}}'
    )
    address_formats = ("{{street_address}}",)

    def flat_number_prefix(self):
        from random import randint
        flatnum = str(randint(1, 18))
        if flatnum < 10:
            flatnum = "0" + flatnum
        return '#' + flatnum

    def flat_number_suffix(self):
        from random import randint
        flatnum = str(randint(1, 18))
        if flatnum < 10:
            flatnum = "0" + flatnum
        return flatnum

    blocks = ('Blk 1##', 'Blk 2##', 'Blk 3##', 'Blk 4##', 'Blk 1#', 'Blk 2#', 'Blk 3#', 'Blk 4#')
    sg_streets = ('Street 1#', 'Street 2#', 'Street 3#', 'Street 7#', 'Street 8#')
    street_numbers = (
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '1#', '2#', '3#', '4#', '5#', '6#', '7#', '8#', 'Blk 1##')
    lorongs = (
    'Lorong 1', 'Lorong 1#', 'Lorong 2', 'Lorong 3', 'Lorong 4', 'Lorong 5', 'Lorong 6', 'Lorong 7', 'Lorong 8')
    major_estates = (
    'Aljunied', 'Ang Mo Kio', 'Bedok', 'Boon Lay', 'Bukit Merah', 'Bukit Panjang', 'Clementi', 'Geylang',
    'Geylang East', 'Hougang', 'Jurong Central', 'Jurong East', 'Jurong West', 'Kallang', 'Marine Parade', 'Pasir Ris',
    'Sengkang', 'Serangoon Gardens', 'Serangoon North', 'Tampines', 'Toa Payoh', 'Woodlands', 'Yishun')
    sg_towns = ('Admiralty', 'Aljunied', 'Ang Mo Kio', 'Anson Road', 'Balestier', 'Bartley', 'Bedok', 'Bedok Reservoir',
                'Bencoolen', 'Bidadari', 'Boon Keng', 'Boon Keng', 'Boon Lay', 'Buangkok', 'Bugis', 'Bukit Batok',
                'Bukit Gombak', 'Bukit Ho Swee', 'Bukit Merah', 'Bukit Panjang', 'Bukit Purmei', 'Bukit Timah',
                'Buona Vista', 'Cairnhill', 'Caldecott', 'Cheng San', 'Chin Bee', 'Choa Chu Kang', 'Chong Boon',
                'Chong Pang', 'Clementi', 'Commonwealth', 'Dover', 'Dunearn', 'Farrer', 'Fidelio', 'Frankel',
                'Gek Poh Ville', 'Geylang', 'Geylang East', 'Ghim Moh', 'Hillview', 'Hougang', 'Innova', 'Joo Koon',
                'Jurong', 'Jurong Central', 'Jurong East', 'Jurong West', 'Kallang', 'Kembangan', 'Lavender',
                'Lim Chu Kang', 'Lok Yang', 'MacPherson', 'Mandai', 'Marine Parade', 'Marsiling', 'Mattar', 'Nanyang',
                'Novena', 'Orchard Road', 'Pandan Valley', 'Pasir Panjang', 'Pasir Ris', 'Paya Lebar', 'Pioneer',
                'Potong Pasir', 'Punggol', 'Queenstown', 'Rochor', 'Seletar', 'Sengkang', 'Sennett', 'Serangoon',
                'Serangoon Gardens', 'Serangoon North', 'Shunfu', 'Simei', 'Simpang', 'Sin Ming', 'Somerset',
                'Sungei Gedong', 'Tai Seng', 'Tampines', 'Tanglin', 'Tanjong Pagar', 'Teck Ghee', 'Telok Blangah',
                'Tengah', 'Thomson', 'Tiong Bahru', 'Toa Payoh', 'Watten', 'Woodgrove', 'Woodlands', 'Yew Tee',
                'Yishun', 'Yuhua')
    jalan_places = (
    'Adat', 'Afifi', 'Ahmad Ibrahim', 'Ampang', 'Ampas', 'Anak Bukit', 'Anak Patong', 'Anggerek', 'Angin Laut', 'Antoi',
    'Arif', 'Ariff', 'Arnap', 'Aruan', 'Asas', 'Asuhan', 'Awan', 'Awang', 'Ayer', 'Azam', 'Bahagia', 'Bahar', 'Bahasa',
    'Bahtera', 'Baiduri', 'Bangau', 'Bangket', 'Bangsawan', 'Batai', 'Batalong', 'Batu', 'Batu Nilam', 'Belangkas',
    'Belibas', 'Bena', 'Benaan Kapal', 'Beringin', 'Berjaya', 'Berseh', 'Berseri', 'Besar', 'Besar Plaza', 'Besar Road',
    'Besut', 'Bilal', 'Binchang', 'Bingka', 'Binja', 'Bintang Tiga', 'Boon Lay', 'Bukit Merah', 'Bukit Anak',
    'Bukit Ho Swee', 'Bukit Merah', 'Buloh Perindu', 'Bumbong', 'Bunga', 'Bunga Rampai', 'Bunga Raya', 'Bungai Rampai',
    'Buroh', 'Chegar', 'Chelagi', 'Chempadek', 'Chempah', 'Chempaka Kuning', 'Chempaka Puteh', 'Chempedak', 'Chengam',
    'Chengkek', 'Cherah', 'Chermai', 'Chermat', 'Cherpen', 'Chorak', 'Chulek', 'Daliah', 'Damai', 'Damansara', 'Datoh',
    'Daud', 'Demak', 'Dermawan', 'Derum', 'Dinding', 'Dua', 'Dusan', 'Dusun', 'Dusun Road', 'Elok', 'Emas Urai',
    'Empat', 'Enam', 'Eunos', 'Gaharu', 'Gajus', 'Gali Batu', 'Gapis', 'Gelam', 'Gelegar', 'Gelenggang', 'Gemala',
    'Gembira', 'Gendang', 'Geneng', 'Girang', 'Greja', 'Grisek', 'Gumilang', 'Haji Alias', 'Haji Salam', 'Hajijah',
    'Hang Jebat', 'Hari Raya', 'Harom Setangkai', 'Harum', 'Hiboran', 'Hikayat', 'Hitam Manis', 'Hock Chye', 'Hussein',
    'Hwi Yoh', 'Ibadat', 'Ikan Merah', 'Ilmu', 'Inggu', 'Insaf', 'Intan', 'Ishak', 'Ismail', 'Isnin', 'Istimewa',
    'Jamal', 'Jambo Ayer', 'Jambu Ayer', 'Jambu Batu', 'Jambu Mawar', 'Janggus', 'Jarak', 'Jati', 'Jelita', 'Jendela',
    'Jentera', 'Jermin', 'Jeruju', 'Jintan', 'Jitong', 'Joran', 'Jumbu Mawar', 'Jurong Kechil', 'Kakatua', 'Kalapa',
    'Kampong Chantek', 'Kandis', 'Kapal', 'Kasau', 'Kathi', 'Kayu', 'Kayu Estate', 'Kayu Manis', 'Kebaya',
    'Kebun Limau', 'Kechil', 'Kechot', 'Kechubong', 'Kelabu Asap', 'Kelawar', 'Kelempong', 'Keli', 'Kelichap',
    'Kelulut', 'Kemajuan', 'Kemaman', 'Kembang Melati', 'Kembangan', 'Kemboja', 'Kemuning', 'Kenarah', 'Kerayong',
    'Keria', 'Keris', 'Keruing', 'Kesoma', 'Ketumbit', 'Khairuddin', 'Khamis', 'Kilang', 'Kilang Barat', 'Kilang Timor',
    'Klapa', 'Kledek', 'Klinik', 'Korban', 'Korma', 'Krian', 'Kuak', 'Kuala', 'Kuang', 'Kubor', 'Kukoh', 'Kumia',
    'Kuning', 'Kupang', 'Kuras', 'Kurnia', 'Kwok Min', 'Labu', 'Labu Ayer', 'Labu Manis', 'Labu Merah', 'Lady Maxwell',
    'Lakum', 'Lam Huat', 'Lam Sam', 'Lana', 'Langgar Bedok', 'Lanjut', 'Lapang', 'Lateh', 'Leban', 'Lebat Daun',
    'Legundi', 'Lekar', 'Lekub', 'Lembah Bedok', 'Lembah Kallang', 'Lempeng', 'Lengkok Sembawang', 'Lengkong Tiga',
    'Lepas', 'Lim Tai', 'Lim Tai See', 'Limau Bali', 'Limau Balli', 'Limau Kasturi', 'Limau Manis', 'Limau Nipis',
    'Limau Purut', 'Limbok', 'Lokam', 'Loyang Besar', 'Lye Kwee', 'Ma\'mor', 'Machang', 'Mahir', 'Malu Malu', 'Mamor',
    'Manis', 'Mariam', 'Marican', 'Marzuki', 'Mas Kuning', 'Mas Kunning', 'Mas Merah', 'Mas Puteh', 'Mashhor', 'Masjib',
    'Masjid', 'Mastuli', 'Mat Jambol', 'Mata Ayer', 'Mawal', 'Mawar', 'Mayaanam', 'Melati', 'Melor', 'Membina',
    'Membina Barat', 'Menarong', 'Mengkudu', 'Meragi', 'Merah Saga', 'Merbok', 'Merdu', 'Merlimau', 'Mesin', 'Mesra',
    'Minggu', 'Minyak', 'Miutiara', 'Molek', 'Muhibbah', 'Mulia', 'Murai', 'Mutiara', 'Mydin', 'Naga Sari', 'Nallur',
    'Nam Seng', 'Naung', 'Nipah', 'Nira', 'Novena', 'Novena Barat', 'Novena Selatan', 'Novena Timor', 'Novena Utara',
    'Nuri', 'Pacheli', 'Pakis', 'Pandan', 'Papan', 'Paras', 'Pari Burong', 'Pari Dedap', 'Pari Kikis', 'Pari Unak',
    'Pasar Baru', 'Pasir Ria', 'Pasiran', 'Payoh Lai', 'Pelajau', 'Pelangi', 'Pelatina', 'Pelatok', 'Pelepah',
    'Pelikat', 'Pemimpin', 'Peminpin', 'Penjara', 'Peradun', 'Perahu', 'Pergam', 'Pernama', 'Pesawat', 'Piala',
    'Pinang', 'Pintau', 'Piring', 'Pisang', 'Pokok Serunai', 'Punai', 'Puteh Jerneh', 'Puteh Jula', 'Puyoh', 'Rabu',
    'Rahmat', 'Raja Udang', 'Rajah', 'Rajah Road', 'Rajawali', 'Rama Rama', 'Rama Rama', 'Ramaja', 'Ramis', 'Rasok',
    'Rasok Park', 'Raya', 'Rebana', 'Redop', 'Remaja', 'Remis', 'Rendang', 'Rengas', 'Rengkam', 'Resak', 'Ria', 'Riang',
    'Rimau', 'Rindu', 'Rukam', 'Rumah Tinggi', 'Rumbia', 'Rumia', 'Sahabat', 'Sajak', 'Salang', 'Samarinda', 'Sampurna',
    'Samulun', 'Sankam', 'Sappan', 'Satu', 'Saudara Ku', 'Sayang', 'Seaview', 'Sedap', 'Segam', 'Seh Chuan', 'Sejarah',
    'Selamat', 'Selangat', 'Selanting', 'Selasah', 'Selaseh', 'Selendang Delima', 'Selimang', 'Sembilang', 'Semerbak',
    'Sempadan', 'Senang', 'Sendudok', 'Seni', 'Sentosa', 'Senyum', 'Serene', 'Serengam', 'Seruling', 'Setia', 'Shaer',
    'Siantan', 'Siap', 'Sikudangan', 'Simpang Bedok', 'Sinar Bintang', 'Sinar Bulan', 'Sindor', 'Singa', 'Songket',
    'Soo Bee', 'Suasa', 'Suka', 'Sukachita', 'Sultan', 'Sungei', 'Sungei Poyan', 'Surau', 'Tabur', 'Tai See', 'Taman',
    'Tamban', 'Tambur', 'Tampang', 'Tan Tock Seng', 'Tanah Puteh', 'Tanah Rata', 'Tani', 'Tanjong', 'Tapisan',
    'Tari Dulang', 'Tari Lilin', 'Tari Piring', 'Tari Serimpi', 'Tari Zapin', 'Tarum', 'Teban', 'Teck Kee', 'Teck Whye',
    'Tekad', 'Tekukor', 'Telang', 'Telawi', 'Telipok', 'Teliti', 'Tembusu', 'Tempua', 'Tenaga', 'Tenang', 'Tenggiri',
    'Tenon', 'Tenteram', 'Tepong', 'Terang Bulan', 'Terang Bulan, Opera Estate', 'Terap', 'Terentang', 'Terubok',
    'Terusan', 'Tiga', 'Tiga Ratus', 'Todak', 'Tua Kong', 'Tukang', 'Tumpu', 'Tupai', 'Turi', 'Ubi', 'Uji',
    'Ulu Seletar', 'Ulu Sembawang', 'Ulu Siglap', 'Unggas', 'Usaha', 'Wajek', 'Wak Selat', 'Wakaff', 'Wangi',
    'Waringin', 'Warkaff', 'Woodbridge', 'Yasin', 'Yasin', 'Zamrud')

    def block(self):
        return self.numerify(self.random_element(self.blocks))

    def sg_street(self):
        return self.numerify(self.random_element(self.sg_streets))

    def street_number(self):
        return self.numerify(self.random_element(self.street_numbers))

    def lorong(self):
        return self.numerify(self.random_element(self.lorongs))

    def major_estate(self):
        return self.random_element(self.major_estates)

    def town(self):
        return self.random_element(self.sg_towns)

    def jalan_place(self):
        return self.random_element(self.jalan_places)
