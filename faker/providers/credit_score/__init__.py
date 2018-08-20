# coding=utf-8
from __future__ import unicode_literals
from collections import OrderedDict

from .. import BaseProvider


class CreditScore(object):
    def __init__(self, name, provider, score_range):
        self.name = name
        self.provider = provider
        self.score_range = score_range


class Provider(BaseProvider):
    """ Provider for Credit Score. """

    # FICO 8 Score is the most widely-used non-industry specific credit score model,
    # followed by 5, 2, and 4 as per https://www.myfico.com/credit-education/credit-scores/fico-score-versions
    #
    # Ranges obtained here and validated elsewhere:
    #
    # * https://blog.myfico.com/whats-a-good-credit-score-range/
    # * https://www.wrightrealtors.com/home/credit-score.htm

    fico8_range = [300, 850]
    fico5_range = [334, 818]
    fico2_range = [320, 844]
    fico4_range = [309, 839]

    credit_score_types = OrderedDict(
        (
            ("fico8", CreditScore("FICO Score 8", "FICO", fico8_range)),
            ("fico5", CreditScore("Equifax Beacon 5.0", "Equifax", fico5_range)),
            ("fico2", CreditScore("Experian/Fair Isaac Risk Model V2SM", "Experian", fico2_range)),
            ("fico4", CreditScore("TransUnion FICO Risk Score, Classic 04", "TransUnion", fico4_range)),
        )
    )
    credit_score_types["fico"] = credit_score_types["fico8"]

    def credit_score_name(self, score_type=None):
        """ Returns the name of the credit score. """
        if score_type is None:
            score_type = self.random_element(self.credit_score_types.keys())
        return self._credit_score_type(score_type).name

    def credit_score_provider(self, score_type=None):
        """ Returns the name of the credit score provider. """
        if score_type is None:
            score_type = self.random_element(self.credit_score_types.keys())
        return self._credit_score_type(score_type).provider

    def credit_score(self, score_type=None):
        """ Returns a valid credit score. """
        credit_score_summary = self._credit_score_type(score_type)
        score = self._generate_credit_score(credit_score_summary.score_range)
        return score

    def credit_score_full(self, score_type=None):
        credit_score_summary = self._credit_score_type(score_type)

        tpl = "{name}\n" "{provider}\n" "{credit_score}\n"

        tpl = tpl.format(
            name=self.credit_score_name(credit_score_summary),
            provider=self.credit_score_provider(credit_score_summary),
            credit_score=self.credit_score(credit_score_summary),
        )
        return self.generator.parse(tpl)

    def _credit_score_type(self, score_type=None):
        """ Returns a credit score type instance of the specified type (random if none provided). """
        if score_type is None:
            score_type = self.random_element(self.credit_score_types.keys())
        elif isinstance(score_type, CreditScore):
            return score_type
        return self.credit_score_types[score_type]

    def _generate_credit_score(self, credit_score_range):
        """ Returns an integer within the range specified by credit_score_range. """
        return self.generator.random_int(*credit_score_range)
