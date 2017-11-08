# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .. import Provider as PersonProvider

'''
Based on https://github.com/missbossy/Faker/tree/singapore
'''


class Provider(PersonProvider):
    formats_female = (
        '{{english_name_female}} {{chinese_family_name}}',
        '{{english_name_female}} {{chinese_family_name}}',
        '{{english_name_female}} {{chinese_family_name}}',
        '{{english_name_female}} {{chinese_family_name}}',
        '{{english_name_female}} {{chinese_family_name}}',
        '{{english_name_female}} {{chinese_family_name}}',
        '{{english_name_female}} {{chinese_family_name}}',
        '{{chinese_family_name}} {{chinese_name_female}}',
        '{{chinese_family_name}} {{chinese_name_female}} {{english_name_female}}',
        '{{english_name_female}} {{chinese_family_name}} {{chinese_name_female}}',
        '{{malay_name_female}} {{malay_family_name}}',
        '{{english_name_female}} {{mixed_family_name}}',
    )

    formats_male = (
        '{{english_name_male}} {{chinese_family_name}}',
        '{{english_name_male}} {{chinese_family_name}}',
        '{{english_name_male}} {{chinese_family_name}}',
        '{{english_name_male}} {{chinese_family_name}}',
        '{{english_name_male}} {{chinese_family_name}}',
        '{{english_name_male}} {{chinese_family_name}}',
        '{{english_name_male}} {{chinese_family_name}}',
        '{{chinese_family_name}} {{chinese_name_male}} {{english_name_male}}',
        '{{english_name_male}} {{chinese_family_name}} {{chinese_name_male}}',
        '{{malay_name_male}} {{malay_family_name}}',
        '{{english_name_male}} {{mixed_family_name}}',
    )

    formats = formats_female + formats_male

    chinese_names_female = (
        'Ah Hoon', 'Ah Nooi', 'Ai Heng', 'Ai Hua', 'Ai Leng', 'Ai Mei', 'Bee Chin', 'Bee Choo', 'Bee Eng', 'Bee Huai',
        'Bee Kian', 'Bee Lan', 'Bee Lay', 'Bee Lay', 'Bee Leng', 'Bee Lian', 'Bee Mohd', 'Bee San', 'Bee Yian',
        'Beh-Li',
        'Beng Choo', 'Beng Mooi', 'Bok Ai', 'Boon Ping', 'Caiwen', 'Chai Hoon', 'Chai Leng', 'Chai Ling', 'Chan Lee',
        'Chay Koon', 'Chee Lin', 'Chen Chee', 'Chen Yong', 'Cheng Hoon', 'Cheng Lei', 'Cheng Moy', 'Cheow Lan',
        'Chern May',
        'Chern Nee', 'Chet Yoke', 'Chew Yam', 'Chi Chien', 'Chia Hui', 'Chia Ming', 'Chiew Pieng', 'Chiew Sze',
        'Ching Wi',
        'Choi Sin', 'Choo Neo', 'Choo Tin', 'Choo Tuan', 'Choon Sim', 'Chor Ping', 'Choy Eng', 'Chui Hong', 'Chui Lan',
        'Chun Lan', 'Chwee Har', 'Dai See', 'Ee Lam', 'Eew Hwong', 'Eng Neo', 'Eng Yan', 'Eng Yeo', 'Fong Keow',
        'Foong Lim', 'Gait Hong', 'Gek Choo', 'Gek Eng', 'Gek Kim', 'Gek Lian', 'Gek Neo', 'Gek Noi', 'Gek Poh',
        'Geok Cheok', 'Geok Har', 'Geok Kim', 'Geok Leng', 'Gia Hoang', 'Goay Ee', 'Guat Cheng', 'Gui Fang', 'Han',
        'Hiang Hwee', 'Hiau Mui', 'Hon Teng', 'Hoo Pin Lick', 'Hoon Audrey', 'Hua Cheng', 'Hua Hong', 'Huay Keng',
        'Huei-Ling', 'Huey Lih', 'Hui Hoon', 'Hui Kai', 'Hui Shien', 'Hui Sian', 'Hui Sin', 'Hui Tsu', 'Hui Yen',
        'Hui Yu',
        'Hung Yuen', 'Hwee Gek', 'Hwee Hoon', 'Hwee Lan', 'Hwee Nak', 'Hwee Peng', 'Hwee Yi', 'Ijen', 'Ji Lien',
        'Jia Li',
        'Jing Hui', 'Jing Wen', 'Jit Tian', 'Joo Ee', 'Joo Mee', 'Juan Ze', 'Jue Ting', 'Jun Hui', 'Jun Yu', 'Kah Nee',
        'Kam Ching', 'Kar Kuan', 'Kay Nio', 'Khim Tiang', 'Khor Kit', 'Khor Quin', 'Khor Soo', 'Kim Choo', 'Kim Eng',
        'Kim Hiang', 'Kim Kee', 'Kim Moi', 'Kim Neo', 'King Guat', 'Kit Ying', 'Koon Chyn', 'Koon Hian', 'Kum Lee',
        'Kum Leng', 'Kwee Choo', 'Lai Hah', 'Lai Khan', 'Lai Meng', 'Lai Wan', 'Lai Wen', 'Lai Yoke', 'Lain Koon',
        'Lay Bee', 'Lay Ching', 'Lay Choo', 'Lay Gim', 'Lay Hean', 'Lay Hoon', 'Lay Kheng', 'Lay Khim', 'Lay Kin',
        'Lay Kwan', 'Lee Bui', 'Lee Hin', 'Lee Hwee', 'Lee Jiang', 'Lee Keang', 'Lee Lee', 'Lee Meng', 'Lee Siang',
        'Lei Thoh', 'Leng Poh', 'Li Ching', 'Li Choo', 'Li Huang', 'Li Khoon', 'Li Lin', 'Li Ling', 'Li Song',
        'Lian Choo',
        'Lijuan', 'Limin', 'Lin Hsia', 'Ling Ghim', 'Lingyi', 'Li-ping', 'Li-Ping', 'Lye Kim', 'Mae Lyn', 'Man Eng',
        'Man Qin', 'May Giok', 'Mee Chooi', 'Mee Mee', 'Mee Saw', 'Mei Fang', 'Mei Horng', 'Mei Kum', 'Mei Lin',
        'Mei Ling',
        'Mei Ling', 'Mei Shan', 'Mei Ying', 'Mei Yun', 'Meiyi', 'Meng Eng', 'Meng Lee', 'Mi Kyung', 'Mi Ling',
        'Miaw Phio',
        'Min Ai', 'Min Li', 'Min Qi', 'Min Wei', 'Ming E', 'Mui Cheng', 'Mui Chew', 'Mui Fong', 'Mui Lan', 'Mui Ling',
        'Mun Yue', 'Mun-wei', 'Nang Hiang', 'Ning Ning', 'Peck Sian', 'Pei Chi', 'Pei Ngee', 'Pei Pei', 'Pei Xin',
        'Pei Yun', 'Peishan', 'Pek Ching', 'Pek Har', 'Pek Kay', 'Pek Yuen', 'Peng Mei', 'Phui Kuen', 'Pin Pin',
        'Png Sim',
        'Po Lyn', 'Poey Ling', 'Poh Chan', 'Poh Choo', 'Poh Choo', 'Poh Eng', 'Poh Fun', 'Poh Gek', 'Poh Wan',
        'Poh Yen',
        'Puay Sian', 'Pui Lim', 'Pui Yee', 'Qing Jing', 'Qing Yi', 'Quee Lan', 'Ruo Fan', 'Sai Huay', 'Sai Yang',
        'Say Pin',
        'See Chin', 'See Hui', 'See Kew', 'See Ngoh', 'See Ping', 'Seen Kwun', 'Seok Eng', 'Seok Hui', 'Seok Keim',
        'Seow Cheng', 'Seow Leng', 'Shan Li', 'Shi Hmin', 'Shiwen', 'Shu-Ting', 'Shwu Fen', 'Si En', 'Si Qi', 'Si Ting',
        'Si Ting', 'Sidhu', 'Sie May', 'Siew Cheng', 'Siew Girk', 'Siew Hong', 'Siew Hoon', 'Siew Hui', 'Siew Ing',
        'Siew Ju', 'Siew Kheng', 'Siew Kim', 'Siew Li', 'Siew Lian', 'Siew Mee', 'Siew Mee', 'Siew Ping', 'Siew Wei',
        'Sim Nam', 'Sing Kee', 'Siok Hoon', 'Siow Nee', 'Sock Hiang', 'Soek Ngee', 'Soh Hoon', 'Soh Hua', 'Soi Moi',
        'Sok Hong', 'Sok Huay', 'Soo Ching', 'Soo Hoon', 'Soo Hoon', 'Soo Hwang', 'Soo Leng', 'Soo Mui', 'Soo Ngoh',
        'Soo See', 'Sook Meng', 'Sou Phaik', 'Sow Tin', 'Su En', 'Su Hui', 'Su Wei', 'Su Yen', 'Su Yin', 'Sue Lynn',
        'Suet Hong', 'Suet Teng', 'Sui Ling', 'Suit Ching', 'Sun Chen', 'Sun Sun', 'Swee Gek', 'Swee Lan', 'Swee Leng',
        'Swee Leong', 'Swee Lian', 'Swee Liang', 'Swee Ling', 'Sze Nga', 'Sze Sze', 'Sze Yeo', 'Talpo', 'Teck Cheng',
        'Teck Geok', 'Tee Hooi', 'Teeo Huang', 'Ting Ting', 'Tung Mui', 'Voon Kuen', 'Voon Noh', 'Vun Ping', 'Wai Han',
        'Wai Ling', 'Wai Yen', 'Wan Ling', 'Wan Xin', 'Wan Yee', 'Wan Ying', 'Wee Choo', 'Wei Li', 'Wei-li',
        'Wen Cheng',
        'Wen Li', 'Wen Yi', 'Whui Whui', 'Wimin', 'Wui Hien', 'Xin Ci', 'Xin Yi', 'Xin Yi', 'Xin Yuan', 'Xin Yue',
        'Xing Rong', 'Xiu Sui', 'Xiu Ting', 'Xiu Zhen', 'Xue Ying', 'Ya Li', 'Yan Lih', 'Yan Pei', 'Yanling',
        'Yaw Fung',
        'Ye Ching', 'Yee Li', 'Yen Ling', 'Yen Nee', 'Yen Yee', 'Yi Ling', 'Yi-Ling', 'Yin Chin', 'Yin Ing', 'Yin Yin',
        'Ying Wen', 'Ying Zhen', 'Yock Mun', 'Yoke Kiew', 'Yoke Ping', 'Yoke Sim', 'Yoke Wei', 'Yook Thye', 'Yoon Choo',
        'Yu Chun', 'Yu Hua', 'Yu Lin', 'Yu Lin', 'Yu Shan', 'Yu Shan', 'Yueh Siew', 'Yuen Kay', 'Yuen Yee', 'Yuh Ling',
        'Yurong', 'Zhiqiang', 'Zihui', 'Zu Ying')

    def chinese_name_female(self):
        return self.random_element(self.chinese_names_female)

    chinese_names_male = (
        'Jia Shuo', 'Cheng Sean', 'Chier Wei', 'Hua Yi', 'Eng Siang', 'Hong Kiat', 'Jian Song', 'Jie Hao', 'Jinrong',
        'Kai Wen', 'Ming', 'Ming Gui', 'Rong', 'Ta-Wei', 'Teng Kiat', 'Wei', 'Wei Jie', 'Wei Quan', 'Wei Shaun',
        'Weiliang ', 'Wei-Lun', 'Wen Loong', 'Wen Loong', 'Xianyi', 'Xin Jaime', 'Xue Qian', 'Yi Qiang', 'Yiew Hsien',
        'Yip Hang', 'Yuan', 'Yuanruo', 'Yueh', 'Yung Shen', 'Zhe Yuan', 'Zheng Yang', 'Zhi Jie', 'Zonghan', 'Chee Seng',
        'Cheng Yu', 'Ngiap Heng', 'Tee Seng', 'Boon Hui', 'JK', 'Teck Heng', 'Koon Tan', 'Kiong Tan', 'Hong Boon',
        'Kok Hwee', 'Kok Wah', 'Kok Wee', 'Kok Sing', 'Kah How', 'Kah Hwee', 'Chee Keong', 'Chee How', 'Wee Leong',
        'Wee Meng', 'Wee Kiat', 'Wee Teck', 'Wee Tat', 'Wee Keong', 'Boon Kiat', 'Boon How', 'Boon Keong', 'Boon Tat',
        'Guohui', 'Guohua', 'Guowei', 'Guoxing', 'Jiahao', 'Jiahui', 'Ziqiang', 'Zihao', 'Weiliang', 'Weiming',
        'Weijie',
        'Weide', 'Weida', 'Weiqiang', 'Wenjie', 'Wenhao', 'Wenqiang')

    def chinese_name_male(self):
        return self.random_element(self.chinese_names_male)

    english_names_male = (
        'Aaron', 'Adam', 'Adrian', 'Aidan', 'Aiden', 'Alan', 'Albert', 'Alec', 'Alex', 'Alfred', 'Andrew', 'Andy',
        'Angus',
        'Anthony', 'Arnold', 'Ayden', 'Ben', 'Benjamin', 'Benton', 'Bernard', 'Bernie', 'Bo', 'Boris', 'Bradley',
        'Brandon',
        'Brendon', 'Brian', 'Caleb', 'Carson', 'Carter', 'Cary', 'Casey', 'Cedrick', 'Charles', 'Chris', 'Christian',
        'Clay', 'Clifford', 'Colby', 'Colin', 'Cyril', 'Damian', 'Dan', 'Darian', 'Darrell', 'Darren', 'Dave', 'David',
        'Davin', 'Dean', 'Demond', 'Dennis', 'Derek', 'Dexter', 'Donald', 'Douglas', 'Dylan', 'Ed', 'Edison', 'Edward',
        'Elliot', 'Elwin', 'Eric', 'Ernest', 'Ethan', 'Felix', 'Frank', 'Fred', 'Frederic', 'Gabe', 'Gabriel', 'Garett',
        'Garry', 'Garth', 'Gavin', 'Gene', 'Geoffrey', 'George', 'Gerald', 'Gerard', 'Gilbert', 'Godfrey', 'Gordon',
        'Graham', 'Grant', 'Grayson', 'Greg', 'Hans', 'Harmon', 'Harold', 'Harrison', 'Harry', 'Hayden', 'Henry',
        'Herman',
        'Holden', 'Howard', 'Hudson', 'Hugh', 'Hunter', 'Ian', 'Irving', 'Irwin', 'Ivan', 'Luke', 'Jackson', 'Jake',
        'Jameson', 'Jamie', 'Jarred', 'Jarvis', 'Jasper', 'Jeff', 'Jefferey', 'Jerald', 'Jerome', 'Jeromy', 'Jimmy',
        'Joe',
        'Joel', 'Joesph', 'Joey', 'John', 'Johnathan', 'Johnathon', 'Jonas', 'Jonathan', 'Jonathon', 'Jordon', 'Joseph',
        'Josh', 'Joshua', 'Joshuah', 'Josiah', 'Jovan', 'Julian', 'Justen', 'Kaden', 'Keaton', 'Keith', 'Kelvin', 'Ken',
        'Kevin', 'Kenneth', 'Kenny', 'Kurt', 'Kurtis', 'Kyle', 'Lance', 'Lawrence', 'Lawson', 'Lenny', 'Leonard',
        'Lewis',
        'Lionel', 'Louis', 'Lucas', 'Lucian', 'Leon', 'Mackenzie', 'Malcolm', 'Marc', 'Mark', 'Markus', 'Marshall',
        'Martin', 'Marvin', 'Mathew', 'Mathias', 'Matt', 'Melvin', 'Mervin', 'Micheal', 'Michel', 'Mike', 'Morgan',
        'Moses',
        'Nathan', 'Nathaniel', 'Neal', 'Ned', 'Neil', 'Nelson', 'Nicholas', 'Nick', 'Nigel', 'Oswald', 'Oswaldo',
        'Otto',
        'Otis', 'Owen', 'Patrick', 'Paul', 'Pete', 'Philip', 'Preston', 'Randal', 'Randy', 'Ray', 'Raymond', 'Reuben',
        'Richard', 'Richmond', 'Rick', 'Riley', 'Robb', 'Robert', 'Robin', 'Rocky', 'Roderick', 'Rodger', 'Roger',
        'Roland',
        'Roman', 'Ron', 'Rowan', 'Rowland', 'Roy', 'Rudy', 'Rupert', 'Russ', 'Russel', 'Russell', 'Rusty', 'Ryan',
        'Ryley',
        'Sam', 'Sammy', 'Samson', 'Scott', 'Sean', 'Seth', 'Shawn', 'Sheldon', 'Sonny', 'Spencer', 'Stan', 'Stanley',
        'Stanton', 'Stefan', 'Stephan', 'Stephen', 'Sterling', 'Steve', 'Stewart', 'Stuart', 'Sylvester', 'Taylor',
        'Ted',
        'Terrence', 'Terry', 'Theo', 'Thomas', 'Timmothy', 'Timothy', 'Tom', 'Tony', 'Travis', 'Trevor', 'Turner',
        'Tyler',
        'Vernon', 'Vicente', 'Victor', 'Vince', 'Vincent', 'Wallace', 'Walter', 'Warren', 'Will', 'Willard', 'William',
        'Wilmer', 'Wilson', 'Wilton', 'Winston', 'Wyatt', 'Xavier', 'Xander', 'Zachary', 'Zack',)

    def english_name_male(self):
        return self.random_element(self.english_names_male)

    english_names_female = (
        'Abigail', 'Adelia', 'Adlina', 'Alexis', 'Alicia', 'Alvira', 'Amanda', 'Angeline', 'Ashley', 'Ava', 'Azusa',
        'Beth',
        'Cathy', 'Charmaine', 'Cherilyn', 'Cheryl', 'Chloe', 'Chloe', 'Christina', 'Claire', 'Claudia', 'Dorothy',
        'Dolores', 'Elaine', 'Emma', 'Emma', 'Estelle', 'Esther', 'Eunice', 'Faith', 'Fatin', 'Felicia', 'Feuer',
        'Fiona',
        'Gemmie', 'Gina', 'Grace', 'Hafizah', 'Isabella', 'Jamie', 'Jane', 'Jasmine', 'Jeannie', 'Joey', 'Jolene',
        'Judy',
        'Julia', 'Kimberly', 'Kristen', 'Leah', 'Lee', 'Lily', 'Lena', 'Ling', 'Luna', 'Lynn', 'Ma', 'Madison',
        'Marion',
        'Michelle', 'Min', 'Mindy', 'Mitchie', 'Nasuha', 'Natalie', 'Nicole', 'Olivia', 'Preeti', 'Rachel', 'Rebecca',
        'Regina', 'Rena', 'Renie', 'Sarah', 'Shasha', 'Sherilyn', 'Sheryl', 'Sophia', 'Valerie', 'Vanessa', 'Vicky',
        'Yvonne', 'Abigail', 'Adeline', 'Adrienne', 'Aisha', 'Alana', 'Alexandra', 'Alice', 'Althea', 'Alysha',
        'Amanda',
        'Amy', 'Anabelle', 'Angelina', 'Anna', 'Anne', 'April', 'Ashley', 'Beatrice', 'Bernice', 'Bernadette', 'Betty',
        'Camille', 'Candice', 'Carole', 'Caroline', 'Cassandra', 'Catherine', 'Cathy', 'Cecilia', 'Celine', 'Charlotte',
        'Chloe', 'Christine', 'Claire', 'Connie', 'Constance', 'Cora', 'Corinne', 'Cynthia', 'Dahlia', 'Dakota', 'Dana',
        'Daniella', 'Daphne', 'Darlene', 'Desiree', 'Diana', 'Dora', 'Dorothy', 'Doris', 'Edwina', 'Eileen', 'Elaina',
        'Eleanore', 'Elisa', 'Elizabeth', 'Elmira', 'Emily', 'Emma', 'Erica', 'Esther', 'Eugenia', 'Eunice', 'Felicia',
        'Frederique', 'Devi', 'Dora', 'Gabriella', 'Georgina', 'Gladys', 'Glenda', 'Grace', 'Hanna', 'Hannah',
        'Heather',
        'Helen', 'Hillary', 'Imelda', 'Isabell', 'Jacky', 'Jaclyn', 'Jacyntha', 'Janice', 'Jessica', 'Judy', 'Julia',
        'Kate', 'Kathleen', 'Kayla', 'Kelly', 'Kimberly', 'Kim', 'Kirsten', 'Larissa', 'Laura', 'Lauren', 'Lelia',
        'Lina',
        'Linda', 'Lindsey', 'Lisa', 'Lynn', 'Megan', 'Mandy', 'Marcia', 'Margaret', 'Margie', 'Maria', 'Maureen',
        'Melissa',
        'Michelle', 'Natalie', 'Natasha', 'Nayeli', 'Nedra', 'Nadia', 'Nelda', 'Nella', 'Nelle', 'Nellie', 'Neoma',
        'Nettie', 'Neva', 'Nia', 'Nichole', 'Nicole', 'Phoebe', 'Phyllis', 'Rachel', 'Rebecca', 'Roslyn', 'Ruth',
        'Sandy',
        'Sarah', 'Selena', 'Selina', 'Serena', 'Susan', 'Susie', 'Suzanne', 'Sydnie', 'Sylvia', 'Tiffany', 'Vernie',
        'Vivienne', 'Wendy', 'Zoe')

    def english_name_female(self):
        return self.random_element(self.english_names_female)

    chinese_family_names = (
        'Seetoh', 'Ang', 'Au', 'Aw', ' Boo', 'Chai', 'Chan', 'Chang', 'Chee', 'Chen', ' Cheng', 'Chew', 'Chia', 'Chin',
        'Choi', 'Choo', 'Choy', 'Chua', 'Chye', 'Ee', 'Eng', 'Fang', 'Fong', 'Foo', 'Fu', 'Gan', 'Goh', 'Guo', 'Han',
        'Ho',
        'Hong', 'Hoon', 'Kang', 'Kee', 'Khim', 'Khoo', 'Koh', 'Kok', 'Khor', 'Kwok', 'Lai', 'Lam', 'Lau', 'Lee', 'Leng',
        'Leong', 'Leow', 'Li', 'Lieu', 'Liew', 'Lim', 'Lin', 'Ling', 'Loh', 'Lok', 'Low', 'Loy', 'Lum', 'Lye', 'Mok',
        'Neo',
        ' Ng', 'Ngiam', 'Oh', 'Lim', 'Ong', ' Ooi', 'Pang', 'Peck', 'Peh', 'Pei', 'Phua', 'Poh', 'Poon', 'Quek', 'Seow',
        'Sim', 'Sng', ' Soh', 'Sun', 'Tan', 'Tan', 'Tan', 'Tan', 'Tan', 'Shum', 'Yip', 'Si', 'Yu', 'To', 'Tay', 'Teh',
        'Teo', 'Teoh', 'Thia', 'Toh', 'Tong', 'Toy', 'Wee', ' Wong', 'Woo', 'Cheah', 'Yang', 'Yao', 'Yap', ' Yeo',
        'Yeoh',
        'Yong', 'Zhang', 'Zhen', ' Zhou')

    def chinese_family_name(self):
        return self.random_element(self.chinese_family_names)

    mixed_family_names = (
        'Barker', 'Blake', 'Charteris', 'Cordeiro', 'Critchley', 'Danker', 'de Souza', 'De Witt', 'Desker', 'Keller',
        'Klass', 'Kraal', 'Lazaroo', 'Lopez', 'Miller', 'Monteiro', 'Palmer', 'Schirmer', 'Scully', 'Sheares',
        'Shelley',
        'Smith', 'Tessensohn', 'Thompson', 'Oliveiro', 'Abisheganaden', 'Ahmad', 'Avadai', 'Balakrishnan', 'Banerjee',
        'Baratham', 'Benjamin', 'Bhaskar', 'Chandra', 'Desai', 'Dhanabalan', 'Gafoor', 'General', 'George', 'Gomez',
        'Gore',
        'Govindasamy', 'Gupta', 'Iswaran', 'Jasudasen', 'Jeyaretnam', 'Kannabiran', 'Kaur', 'Kausikan', 'Kesavapany',
        'Kewalram', 'Khiatani', 'Kishnani', 'Krishnan', 'Kumar', 'Kumar', 'Kumar', 'Mahbubani', 'Menon', 'Menon',
        'Mohan',
        'Mohan', 'Nithiah', 'Palanivelu', 'Patel', 'Pillai', 'Pillay', 'Puniamoorthy', 'Rai', 'Rajagobal', 'Rajah',
        'Rajah',
        'Rajiv', 'Rajoo', 'Ramanathan', 'Ramaswamy', 'Sadasivan', 'Saram', 'Sathyalingam', 'Selvadurai', 'Selverajah',
        'Sethuraj,', 'Shanmugam', 'Sharil', 'Sharma', 'Singh', 'Singh', 'Soin', 'Thomas', 'Thumboo', 'Varathan',
        'Vasoo',
        'Vijiaratnam', 'Wijeysingha')

    def mixed_family_name(self):
        return self.random_element(self.mixed_family_names)

    malay_family_names = (
        'Bakar', 'Firdaus', 'Hasan', 'Hazirah', 'Ibrahim', 'Ishak', 'Ismail', 'Kadir', 'Mahmood', 'Mohamad', 'Mohamad',
        'Mohamed', 'Nasar', 'Nasir', 'Nasser', 'Nordin', 'Othman', 'Rahmat', 'Rashid', 'Riduan', 'Saat', 'Salim',
        'Salleh',
        'Subhash', 'Wahid', 'Yacob', 'Yusoff')

    def malay_family_name(self):
        return self.random_element(self.malay_family_names)

    malay_names_male = (
        'Adam', 'Adi', 'Ahmad', 'Aidan', 'Amar', 'Aqil', 'Aryan', 'Ashraff', 'Daniel', 'Danish', 'Effendy', 'Farish',
        'Haziq', 'Imran', 'Irfan', 'Ishak', 'Khalish', 'Mikhail', 'Mohamed', 'Nafiz', 'Rai', 'Rayyan', 'Ridwan',
        'Sabtu',
        'Sam', 'Taufik', 'Thaqif', 'Umar', 'Yusuf', 'Zikri', 'Samir', 'Rashad', 'Abdul', 'Ahmad', 'Ahmed', 'Akeem',
        'Ali',
        'Amir', 'Ari', 'Hassan', 'Hiram', 'Ibrahim', 'Khalil', 'Mohamed', 'Mohammad', 'Mohammed', 'Muhammad', 'Nasir',
        'Raheem', 'Rahul',)

    def malay_name_male(self):
        return self.random_element(self.malay_names_male)

    malay_name_female_set = (
        'Abidah', 'Adilah', 'Aisha', 'Aisyah', 'Azizah ', 'Afiqah', 'Badriah', 'Bahirah', 'Burairah', 'Diana', 'Farah',
        'Farihah', 'Fatimah', 'Farida', 'Hafsah', 'Hajar', 'Hasna', 'Halima', 'Laila', 'Latifah', 'Nabila', 'Nabilah',
        'Mariah', 'Mariam', 'Masyitah', 'Muslimah', 'Nabila', 'Nadya', 'Naimah', 'Najah', 'Nazihah', 'Noor', 'Rahimah',
        'Rahmah', 'Salma', 'Samihah', 'Sasha', 'Nurul', 'Siti', 'Siti', 'Siti', 'Siti', 'Taibah', 'Tamimah', 'Yasmin',
        'Yumna', 'Zahrah', 'Zaidah ', 'Zainab', 'Zubaidah')

    def malay_name_female(self):
        return self.random_element(self.malay_name_female_set)

    suffixes = ('Jr.', 'Sr.', 'I', 'II', 'III', 'IV', 'V', 'MD', 'DDS', 'PhD', 'DVM')

    country_of_origins = (
    'China', 'India', 'China', 'India', 'China', 'India', 'China', 'India', 'China', 'India', 'China', 'India', 'China',
    'China', 'China', 'India', 'China', 'India', 'China', 'India', 'China', 'India', 'China', 'India', 'China', 'India',
    'China', 'China', 'China', 'India', 'China', 'India', 'China', 'India', 'China', 'India', 'China', 'India', 'China',
    'India', 'China', 'China', 'Indonesia', 'Japan', 'South Korea', 'Pakistan', 'Bangladesh', 'Malaysia', 'Philippines',
    'Sri Lanka', 'Taiwan', 'Thailand', 'Timor-Leste', 'Vietnam', 'Indonesia', 'Japan', 'South Korea', 'Pakistan',
    'Bangladesh', 'Malaysia', 'Philippines', 'Sri Lanka', 'Taiwan', 'Thailand', 'Vietnam', 'Australia', 'Denmark',
    'Finland', 'France', 'Germany', 'Norway', 'Canada', 'Austria', 'Belgium', 'New Zealand', 'South Africa', 'Spain',
    'United Kingdom', 'United States of America', 'Bahrain', 'Laos', 'Mauritius', 'Myanmar', 'Nepal', 'Hong Kong',
    'Bhutan', 'Papua New Guinea', 'Brunei', 'Cambodia', 'Tajikistan', 'Turkey', 'Yemen',)

    def country_of_origin(self):
        """
        :example 'China'
        """
        return self.random_element(self.country_of_origins)

    citizenships = (
        'Singaporean', 'Singaporean', 'Singaporean', 'Singaporean', 'Singaporean', 'Singaporean', 'PR', 'PR',
        'Expatriat',)

    def citizenship(self):
        """
        :example 'Singaporean'
        """
        return self.random_element(self.citizenships)

    nric_prefix_formats = (
        'S#######', 'S#######', 'S#######', 'S#######', 'S#######',
        'S#######', 'S#######', 'S#######', 'S#######', 'S#######',
        'S#######', 'S#######', 'S#######', 'S#######', 'S#######',
        'S#######', 'S#######', 'T#######', 'F#######', 'G#######',
    )

    nric_suffixs = (
        'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A',
        'X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K',
    )

    def nric_prefix(self):
        return self.numerify(self.random_element(self.nric_prefix_formats))

    def nric_suffix(self):
        return self.random_element(self.nric_suffixs)

    def nric(self):
        return self.nric_prefix() + self.nric_suffix()
