# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ['{{last_name}}{{first_name}}']
    first_names = [
        'An', 'An', 'Au',
        'Bach', 'Banh', 'Bao', 'Bien', 'Bien', 
        'Cam', 'Canh', 'Canh', 'Cao', 'Cat', 'Chan', 'Chau', 'Chiem', 'Chu', 'Chung', 'Chu', 'Co', 'Cu', 'Cung', 
        'Cung', 'Cung', 'Cuu', 
        'Dịch', 'Diep', 'Dinh', 'Doan', 'Du', 'Dung', 'Du', 'Duu', 'Dai', 'Dam', 'Dao', 'Dau', 'Diền', 'Dinh', 'Doan', 
        'Do', 'Dong', 'Dong', 'Duong', 
        'Gia', 'Giai', 'Gian', 'Giang', 'Giap', 
        'Ha', 'Ha', 'Ha', 'Hac', 'Han', 'Hau', 'Hình', 'Hoa', 'Hoac', 'Hoan', 'Hong', 'Hua', 'Huong', 'Hy', 
        'Kha', 'Khau', 'Khuat', 'Kieu', 'Kim', 'Ky', 'Ky', 
        'La', 'Lac', 'Lai', 'Lam', 'Lang', 'Lanh', 'LAm', 'Lan', 'Le', 'Lien', 'Lieu', 'Lieu', 'Long', 'Loi', 'Lục', 
        'Lu', 'Luong', 'Luu', 
        'Ma', 'Mac', 'Mach', 'Mai', 'Manh', 'Mao', 'Man', 'Mieu', 'Mong', 
        'NgAn', 'Nghe', 'Nghiem', 'Ngu', 'Nguu', 'Nhac', 'Nhan', 'Nham', 'Nhiep', 'Nhieu', 'Nhung', 'Ninh', 'Nong', 
        'o', 'on', 'ong', 
        'Phi', 'Pho', 'Phong', 'Phong', 'Phu', 'Phung', 'Phuong', 
        'Quach', 'Quan', 'Quan', 'Quang', 'Quang', 'Que', 'Quyen', 
        'Sai', 'Sam', 'Su', 
        'Ta', 'Tao', 'Tang', 'TAn', 'Tan', 'Tat', 'Te', 
        'Thach', 'Thai', 'Thai', 'Thang', 'Thanh', 'Thao', 'ThAn', 'Thi', 'Thich', 'Thien', 'Thieu', 'Thoi', 'Thuy', 
        'Thu', 'Thuong', 'Tien', 'Tiet', 'Tieu', 'Tieu', 'To', 'Ton', 'Tong', 'Tong', 'Trac', 'Trach', 'Trai', 'Trang', 
        'Tram', 'TrAu', 'Trì', 'Trieu', 'Trịnh', 'Truong', 'Tu', 'Tuởng', 'Uc', 'ung', 
        'Van', 'Van', 'VAn', 'Vi', 'Vinh', 'Vu', 'Vuong', 'Vuu', 
        'Xa', 'Xam', 'Xe', 
        'Yen'
    ]

    last_names = [
        'Nguyen', 'Tran', 'Le', 'Pham', 'Huynh', 'Hoang', 'Phan', 
        'Vu', 'Vo', 'Đang', 'Bui', 'Đo', 'Ho', 'Ngo', 'Duong', 'Ly'
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

    def first_mid_name(self):
        '''
        @example 'Tien'
        '''
        return self.random_element(self.first_names)

    def last_mid_name(self):
        '''
        @example 'Nguyen'
        '''
        return self.random_element(self.last_names)
