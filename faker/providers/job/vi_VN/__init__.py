from .. import Provider as JobProvider


class Provider(JobProvider):
    """Translated from Super class"""

    jobs = (
        # Information technology field
        "Lập trình viên",
        "Kỹ sư phần mềm",
        "Kiến trúc sư phần mềm",
        "Nhà phân tích dữ liệu",
        "Chuyên viên bảo mật",
        "Tester",
        "DevOps Engineer",
        "Project Manager",
        "UX/UI Designer",
        "Digital Marketer",
        "Thực Tập",
        # Finance - banking sector
        "Nhân viên ngân hàng",
        "Chuyên viên tín dụng",
        "Kế toán",
        "Kiểm toán",
        "Nhà tư vấn tài chính",
        "Chuyên viên phân tích thị trường",
        # Business areas
        "Giám đốc kinh doanh",
        "Trưởng phòng kinh doanh",
        "Nhân viên kinh doanh",
        "Marketing Manager",
        "Sales Representative",
        "Chuyên viên bán hàng trực tuyến",
        # Education Department
        "Giáo viên",
        "Giảng viên",
        "Chuyên viên tư vấn tuyển sinh",
        "Thực tập sinh giáo dục",
        # Medical
        "Bác sĩ",
        "Y tá",
        "Dược sĩ",
        "Điều Dưỡng",
        # Building sector
        "Kỹ sư xây dựng",
        "Kiến trúc sư",
        "Thợ xây",
        "Kỹ sư giám sát",
        # Service sector
        "Nhân viên khách sạn",
        "Nhân viên nhà hàng",
        "Tư vấn khách hàng",
        "Nhân viên lễ tân",
        # Manufacturing sector
        "Công nhân sản xuất",
        "Kỹ sư sản xuất",
        "Quản lý sản xuất",
        # Agriculture sector
        "Nông dân",
        "Kỹ sư nông nghiệp",
        # Law field
        "Luật sư",
        "Thư ký pháp lý",
        # Other areas
        "Nhà báo",
        "Biên dịch viên",
        "Nghệ sĩ",
        "Nhà thiết kế đồ họa",
        "Nhân viên hành chính",
        "Chuyên viên nhân sự",
        "Nhân Viên Bán Hàng",
    )

    def job(self) -> str:
        return self.random_element(self.jobs)
