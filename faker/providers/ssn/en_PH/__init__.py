from ... import BaseProvider


class Provider(BaseProvider):
    """
    Provider for Philippine IDs that are related to social security

    There is no unified social security program in the Philippines. Instead, the Philippines has a messy collection of
    social programs and IDs that, when put together, serves as an analogue of other countries' social security program.
    The government agencies responsible for these programs have relatively poor/outdated information and documentation
    on their respective websites, so the sources section include third party "unofficial" information.

    - Social Security System (SSS) - Social insurance program for workers in private, professional, and informal sectors
    - Government Service Insurance System (GSIS) - Social insurance program for government employees
    - Home Development Mutual Fund (popularly known as Pag-IBIG) - Socialized financial assistance and loaning program
    - Philippine Health Insurance Corporation (PhilHealth) - Social insurance program for health care
    - Unified Multi-Purpose ID (UMID) - Identity card with common reference number (CRN) that serves as a link to
                                        the four previous programs and was planned to supersede the previous IDs, but
                                        its future is now uncertain because of the upcoming national ID system

    Sources:
    - https://www.sss.gov.ph/sss/DownloadContent?fileName=SSSForms_UMID_Application.pdf
    - https://www.gsis.gov.ph/active-members/benefits/ecard-plus/
    - https://www.pagibigfund.gov.ph/DLForms/providentrelated/PFF039_MembersDataForm_V07.pdf
    - https://filipiknow.net/is-umid-and-sss-id-the-same/
    - https://filipiknow.net/philhealth-number/
    - https://en.wikipedia.org/wiki/Unified_Multi-Purpose_ID
    """

    sss_formats = ('##-#######-#',)
    gsis_formats = ('###########',)
    philhealth_formats = ('##-#########-#',)
    pagibig_formats = ('####-####-####',)
    umid_formats = ('####-#######-#',)

    def sss(self):
        return self.numerify(self.random_element(self.sss_formats))

    def gsis(self):
        return self.numerify(self.random_element(self.gsis_formats))

    def pagibig(self):
        return self.numerify(self.random_element(self.pagibig_formats))

    def philhealth(self):
        return self.numerify(self.random_element(self.philhealth_formats))

    def umid(self):
        return self.numerify(self.random_element(self.umid_formats))

    def ssn(self):
        # Use UMID as SSN in the interim till its deprecation
        return self.umid()
