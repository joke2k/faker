import unittest

from faker import Faker


class TestJob(unittest.TestCase):
    """
    Test Job
    """

    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestJaJP(unittest.TestCase):
    """
    Test Job ja_JP
    """

    def setUp(self):
        self.fake = Faker('ja_JP')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestKoKR(unittest.TestCase):
    """
    Test Job ko_KR
    """

    def setUp(self):
        self.fake = Faker('ko_KR')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestHuHU(unittest.TestCase):
    "Tests the job module in the Hungarian locale."

    def setUp(self):
        self.fake = Faker('hu_HU')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestHyAm(unittest.TestCase):
    """ Tests jobs in the hy_AM locale """

    def setUp(self):
        self.fake = Faker('hy_AM')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestDeDe(unittest.TestCase):
    """ Tests jobs in the de_DE locale """

    def setUp(self):
        self.fake = Faker('de_DE')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestFrFr(unittest.TestCase):
    """ Tests jobs in the fr_FR locale """

    def setUp(self):
        self.fake = Faker('fr_FR')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestElGr(unittest.TestCase):
    """ Tests jobs in the el_GR locale """

    def setUp(self):
        self.fake = Faker('el_GR')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestPtPt(unittest.TestCase):
    """ Tests jobs in the pt_PT locale """

    def setUp(self):
        self.fake = Faker('pt_PT')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)


class TestPtBR(unittest.TestCase):
    """ Tests jobs in the pt_BR locale """

    def setUp(self):
        self.fake = Faker('pt_BR')
        Faker.seed(0)

    def test_job(self):
        job = self.fake.job()
        assert isinstance(job, str)
