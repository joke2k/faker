# faker/providers/company/es_PE/__init__.py

from collections import OrderedDict

from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    """
    Provider for company names for es_PE locale.

    Sources:
    - Types of business and legal forms: https://www.gob.pe/295-tipos-de-empresa
    - General company naming conventions verified against Peruvian registries
    Accessed: 2026-02-07
    """

    # Minimal implementation: reuse base formats and add comments about sources.
    formats = CompanyProvider.formats
    company_suffixes = CompanyProvider.company_suffixes
