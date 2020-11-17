from faker.providers.job import Provider as JobProvider
from faker.providers.job.de_DE import Provider as DeDeJobProvider
from faker.providers.job.el_GR import Provider as ElGrJobProvider
from faker.providers.job.fr_FR import Provider as FrFrJobProvider
from faker.providers.job.hu_HU import Provider as HuHuJobProvider
from faker.providers.job.hy_AM import Provider as HyAmJobProvider
from faker.providers.job.ja_JP import Provider as JaJpJobProvider
from faker.providers.job.ko_KR import Provider as KoKrJobProvider
from faker.providers.job.pt_BR import Provider as PtBrJobProvider
from faker.providers.job.pt_PT import Provider as PtPtJobProvider
from faker.providers.job.sk_SK import Provider as SkSkJobProvider
from faker.providers.job.th_TH import Provider as ThThJobProvider
from faker.providers.job.tr_TR import Provider as TrTrJobProvider


class TestJobProvider:
    """Test job provider methods"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in JobProvider.jobs


class TestJaJp:
    """Test ja_JP job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in JaJpJobProvider.jobs


class TestKoKr:
    """Test ko_KR job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in KoKrJobProvider.jobs


class TestHuHu:
    """Test hu_HU job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in HuHuJobProvider.jobs


class TestHyAm:
    """Test hy_AM job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in HyAmJobProvider.jobs


class TestDeDe:
    """Test de_DE job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in DeDeJobProvider.jobs


class TestFrFr:
    """Test fr_FR job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in FrFrJobProvider.jobs


class TestElGr:
    """Test el_GR job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in ElGrJobProvider.jobs


class TestPtPt:
    """Test pt_PT job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in PtPtJobProvider.jobs


class TestPtBr:
    """Test pt_BR job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.job() in PtBrJobProvider.jobs


class TestSkSk:
    """Test sk_SK job provider"""

    def test_job(self, faker, num_samples):
        for _ in range(num_samples):
            job = faker.job()
            assert isinstance(job, str)
            assert job in SkSkJobProvider.jobs


class TestThTh:
    """Test th_TH job provider"""

    def test_job(self, faker, num_samples):
        assert faker.job() in ThThJobProvider.jobs


class TestTrTr:
    """Test tr_TR job provider"""

    def test_job(self, faker, num_samples):
        assert faker.job() in TrTrJobProvider.jobs
