from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_male = ("{{first_name_male}} {{last_name}}",)
    formats_female = ("{{first_name_female}} {{last_name}}",)
    formats = formats_male + formats_female

    first_names_male = (
        "An", "Binh", "Chinh", "Duc", "Hai", "Hoang", "Khanh", "Lam", "Minh", "Nam",
        "Nhan", "Phat", "Quan", "Son", "Tuan", "Van", "Viet", "Xuan", "Huu", "Trung",
    )

    first_names_female = (
        "Anh", "Bao", "Cam", "Diep", "Hoa", "Lan", "Mai", "Nga", "Phuong", "Quynh",
        "Thu", "Huong", "Linh", "Thao", "Ngoc", "Yen", "Trang", "Kieu", "My", "Hien",
    )

    last_names = (
        "Nguyen", "Tran", "Le", "Pham", "Hoang", "Vu", "Do", "Truong", "Ngoc", "Bui",
        "Dang", "Huynh", "Ngo", "Vo", "Luong", "Duong", "Ly", "Ha", "Nguyen", "Ho",
    )

