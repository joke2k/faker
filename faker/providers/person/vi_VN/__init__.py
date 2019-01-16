# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as PersonProvider

#Some of the firstname was base on this list: https://en.m.wikipedia.org/wiki/Vietnamese_name
#Most of them was from my personal experience.
class Provider(PersonProvider):
    formats = ['{{last_name}}{{first_name}}']
    first_names = [
        'An', 'An', 'Au', 'Anh',
        'Bach', 'Banh', 'Beo', 'Bao', 'Bien', 'Bien', 'Buu',
        'Cam', 'Canh', 'Canh', 'Cao', 'Cat', 'Chan', 'Chau', 'Chiem', 'Chu', 'Chung', 'Chu', 'Co', 'Cu', 'Cung', 
        'Cuong', 'Chuc', 'Chien', 'Chanh', 'Cung', 'Cuu', 'Co',
        'Dịch', 'Diep', 'Dinh', 'Doan', 'Du', 'Dung', 'Du', 'Duu', 'Dai', 'Dam', 'Dao', 'Dau', 'Diền', 'Dinh', 'Doan', 
        'Do', 'Dong', 'Dong', 'Duong', 'Dang', 'Dang', 'Duy', 'Dieu', 'Dan',
        'Gia', 'Giai', 'Gian', 'Giang', 'Giap', 
        'Ha', 'Hac', 'Han', 'Hau', 'Hình', 'Hoa', 'Hoac', 'Hoan', 'Hong', 'Hua', 'Huong', 'Hy', 'Hieu', 'Hien',
        'Kha', 'Khau', 'Khuat', 'Kieu', 'Kim', 'Ky', 'Ky', 'Khanh', 'Khuong', 
        'La', 'Lac', 'Lau', 'Lai', 'Lam', 'Lang', 'Lanh', 'Lan', 'Le', 'Lien', 'Lieu', 'Long', 'Loi', 'Luc', 
        'Lu', 'Luong', 'Luu', 'Loi', 'Liem',
        'Ma', 'Mac', 'Mach', 'Mai', 'Manh', 'Mao', 'Man', 'Mieu', 'Mong', 
        'Ngab', 'Nghe', 'Nghiem', 'Ngu', 'Nguu', 'Nhac', 'Nhan', 'Nham', 'Nhiep', 'Nhieu', 'Nhung', 'Ninh', 'Nong', 
        'o', 'on', 'ong',
        'Phi', 'Pho', 'Phong', 'Phong', 'Phu', 'Phung', 'Phuong', 'Phoi', 'Phat',
        'Quach', 'Quan', 'Quan', 'Quang', 'Quang', 'Que', 'Quyen', 'Quy', 'Quynh', 'Qui',
        'Sai', 'Sam', 'Su', 'Sang',
        'Ta', 'Tao', 'Tang', 'Tan', 'Tat', 'Te', 'Tong', 'Ton',
        'Thach', 'Thai', 'Thang', 'Thanh', 'Thao', 'Than', 'Thi', 'Thich', 'Thien', 'Thieu', 'Thoi', 'Thuy', 
        'Thu', 'Thuong', 'Tien', 'Tiet', 'Tieu', 'Tieu', 'To', 'Ton', 'Tong', 'Tong', 'Trac', 'Trach', 'Trai', 'Trang', 
        'Tram', 'Trau', 'Tri', 'Trieu', 'Trinh', 'Truong', 'Tu', 'Tuong', 
        'Uc', 'Ung', 
        'Van', 'Vi', 'Vinh', 'Vu', 'Vuong', 'Vuu', 'Vy', 'Vien',
        'Xa', 'Xam', 
        'Yen'
    ]

    last_names = [
        'Nguyen', 'Luong', 'Tang', 'Diep', 'Tran', 'Le', 'Pham', 'Huynh', 'Hoang', 'Phan', 
        'Vu', 'Vo', 'Đang', 'Bui', 'Đo', 'Ho', 'Ngo', 'Duong', 'Ly', 'Doan', 'Dinh', 'Duong'
    ]

    mid_formats = (
        '{{first_name}} {{mid_name}} {{last_name}}',
    )

    mid_names = [
        'Thi', 'Hong', 'Đang', 'Huu', 'Le', 'Le', 'Lien', 'Hoang', 'Hien', 'Nghia', 'Van', 'Ly', 'Phuoc', 'Phi', 'Bang', 'Bich', 'Dung'
    ]

    def mid_name(self):
        '''
        @example 'Tien Dung Nguyen
        '''
        pattern = self.random_element(self.mid_formats)
        return self.generator.parse(pattern)

    def first_name(self):
        '''
        @example 'Tien'
        '''
        return self.random_element(self.first_names)

    def last_name(self):
        '''
        @example 'Nguyen'
        '''
        return self.random_element(self.last_names)
