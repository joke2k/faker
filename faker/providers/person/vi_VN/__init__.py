from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        "{{first_name_female}} {{last_name}}",
        "{{first_name_unisex}} {{last_name}}",
        "{{prefix_female}} {{first_name_unisex}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}}",
    )
    formats_male = (
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{middle_name}} {{last_name}}",
        "{{first_name_unisex}} {{middle_name}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
    )
    formats = formats_female + formats_male

    # Name from : https://en.wikipedia.org/wiki/Vietnamese_name
    # and https://vinpearl.com/en/vietnamese-names-top-200-popular-names-for-boys-and-girls

    first_names_female = (
        "Ngọc",
        "Hương",
        "Lan",
        "Mai",
        "Thảo",
        "Linh",
        "Hồng",
        "Chi",
        "Vân",
        "Duyên",
        "Dương",
        "Yến",
        "Vi",
        "Ánh",
        "Xuân",
    )

    first_names_unisex = (
        "An",
        "Hà",
        "Bảo",
        "Lâm",
        "Hạnh",
        "Thành",
        "Kim",
        "Nhật",
        "Phương",
        "Khoa",
        "Hải",
        "Nhật",
    )

    first_names_male = (
        "Nam",
        "Hưng",
        "Vũ",
        "Tú",
        "Hoàng",
        "Phúc",
        "Trung",
        "Quang",
        "Anh",
        "Khoa",
        "Dũng",
        "Quang",
        "Thành",
        "Huy",
        "Bảo",
        "Châu",
        "Minh",
        "Tùng",
        "Nhiên",
        "Trọng",
    )

    middle_names = (
        "Văn",
        "Thị",
        "Quang",
        "Đức",
        "Trí",
        "Xuân",
        "Hoàng",
        "Hải",
        "Đức",
        "Thế",
        "Tấn",
        "Phú",
        "Hữu",
        "Bảo",
        "Mai",
        "Mai Bảo",
    )

    last_names = ("Nguyễn", "Trần", "Lê", "Phạm", "Vũ", "Đặng", "Bùi", "Dương", "Mai", "Hoàng")

    # Typically, Vietnamese will be addressed with their given name and a prefix
    # https://en.wikipedia.org/wiki/Vietnamese_name#Given_name

    prefixes_female = ("Cô", "Chị", "Bà", "Quý cô")

    prefixes_male = ("Ông", "Anh", "Bác", "Quý ông")

    def first_name_unisex(self) -> str:
        return self.random_element(self.first_names_unisex)

    def middle_name(self) -> str:
        return self.random_element(self.middle_names)
