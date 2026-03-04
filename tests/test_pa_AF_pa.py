from faker import Faker

fake = Faker("pa_AF_pa")

def test_pa_AF_pa_person():
    assert fake.name()
    assert fake.first_name()
    assert fake.first_name_female()
    assert fake.last_name()
    assert fake.date_of_birth()

def test_pa_AF_pa_contact():
    assert fake.email()
    assert fake.phone_number()
    assert fake.random_int(10, 100)

def test_pa_AF_pa_address():
    assert fake.province()
    assert fake.city()
    assert fake.district()
    assert fake.street()
    assert fake.postalcode()

def test_pa_AF_pa_automotive():
    assert fake.license_plate()

def test_pa_AF_pa_bank():
    assert fake.bank()
    assert fake.bank_name()
    assert fake.account_number()
    assert fake.swift()
    assert fake.bank_country()

def test_pa_AF_pa_codes():
    assert fake.ean13()
    assert fake.upc_a()

def test_pa_AF_pa_colors_company():
    assert fake.color()
    assert fake.color_name()
    assert fake.company()
    assert fake.pricetag()

def test_pa_AF_pa_datetime():
    assert fake.date_time()
    assert fake.day_of_week()
    assert fake.day_of_month()
    assert fake.month_name()
    assert fake.year()
    assert fake.month()

def test_pa_AF_pa_geo():
    latlng = fake.local_latlng()
    assert isinstance(latlng, (list, tuple))
    assert len(latlng) == 3
    assert fake.local_longitude()
    assert fake.local_latitude()

def test_pa_AF_pa_internet_books():
    assert fake.domain_name()
    assert fake.isbn13()
    assert fake.isbn10(separator="/")

def test_pa_AF_pa_jobs_text():
    assert fake.job()
    assert fake.job_male()
    assert fake.job_female()
    assert isinstance(fake.get_words_list(), list)
    assert fake.words()
    assert fake.sentence()
    assert fake.sentences(nb=2)
    assert fake.paragraph()
    assert fake.paragraphs(nb=6)

def test_pa_AF_pa_afghan_id():
    afid = fake.afghan_id(separator="-")
    assert "-" in afid
    assert len(afid.replace("-", "")) == 13
