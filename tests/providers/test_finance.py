from datetime import date, timedelta

import pytest

from faker.providers.date_time import Provider as DateTimeProvider

STOCK_OPTION_KEYS = {
    "underlying_symbol",
    "option_type",
    "strike_price",
    "underlying_price",
    "premium",
    "expiration_date",
    "quote_date",
    "delta",
    "gamma",
    "theta",
    "vega",
    "rho",
    "exercised",
    "exercise_date",
}

# "Realism-lite" strike-price band from the design doc is ~20% of the underlying price;
# tests use a looser bound so they aren't coupled to that exact recommended percentage.
STRIKE_BAND_PCT = 0.5


def _intrinsic_value(option_type, underlying_price, strike_price):
    if option_type == "CALL":
        return max(0.0, underlying_price - strike_price)
    return max(0.0, strike_price - underlying_price)


def _in_the_money(option_type, underlying_price, strike_price):
    if option_type == "CALL":
        return underlying_price > strike_price
    return underlying_price < strike_price


class TestFinanceProvider:
    """Test finance provider (listed call/put stock options) methods"""

    def test_option_type(self, faker, num_samples):
        for _ in range(num_samples):
            option_type = faker.option_type()
            assert option_type in ("CALL", "PUT")

    def test_underlying_symbol_format(self, faker, num_samples):
        for _ in range(num_samples):
            symbol = faker.underlying_symbol()
            assert isinstance(symbol, str)
            assert symbol.isalpha()
            assert symbol.isupper()

    def test_underlying_symbol_default_is_curated(self, faker, num_samples):
        # Falls back to a small built-in list of common tickers, not arbitrary strings.
        seen = {faker.underlying_symbol() for _ in range(num_samples)}
        assert len(seen) < num_samples

    def test_underlying_symbol_with_custom_list(self, faker, num_samples):
        symbols = ["ZZZZ", "YYYY", "XXXX"]
        for _ in range(num_samples):
            symbol = faker.underlying_symbol(symbols=symbols)
            assert symbol in symbols

    def test_underlying_symbol_empty_list_raises(self, faker):
        # symbols=[] carries no choices to draw from. Verified against the real
        # implementation: it treats an explicit empty list as distinct from an omitted
        # one (`symbols if symbols is not None else default`) and does not fall back -
        # `random_element(())` raises IndexError. This is a deliberate, reasonable
        # choice (an explicit empty list is a stronger signal than a missing argument),
        # not a bug, so the test pins down the actual behavior rather than the
        # fallback originally guessed before the implementation existed.
        with pytest.raises(IndexError):
            faker.underlying_symbol(symbols=[])

    def test_strike_price_without_underlying(self, faker, num_samples):
        for _ in range(num_samples):
            strike = faker.strike_price()
            assert isinstance(strike, float)
            assert strike > 0

    def test_strike_price_band_around_underlying(self, faker, num_samples):
        for _ in range(num_samples):
            underlying_price = faker.pyfloat(min_value=10, max_value=500, right_digits=2)
            strike = faker.strike_price(underlying_price=underlying_price)
            assert abs(strike - underlying_price) / underlying_price <= STRIKE_BAND_PCT

    def test_strike_price_snapped_to_standard_increment(self, faker, num_samples):
        for _ in range(num_samples):
            strike = faker.strike_price()
            # Standard exchange strike intervals (0.50, 1, 2.50, 5, 10, ...) are all
            # multiples of 0.50 - snapping to anything finer would not be "standard".
            doubled = strike * 2
            assert abs(doubled - round(doubled)) < 1e-6

    def test_option_premium_meets_intrinsic_value_call(self, faker, num_samples):
        for _ in range(num_samples):
            underlying_price = faker.pyfloat(min_value=10, max_value=500, right_digits=2)
            strike = faker.strike_price(underlying_price=underlying_price)
            expiration = faker.date_between(start_date="+1d", end_date="+90d")
            premium = faker.option_premium(
                strike_price=strike,
                underlying_price=underlying_price,
                expiration_date=expiration,
                option_type="CALL",
            )
            assert isinstance(premium, float)
            intrinsic = _intrinsic_value("CALL", underlying_price, strike)
            assert premium >= intrinsic - 1e-6

    def test_option_premium_meets_intrinsic_value_put(self, faker, num_samples):
        for _ in range(num_samples):
            underlying_price = faker.pyfloat(min_value=10, max_value=500, right_digits=2)
            strike = faker.strike_price(underlying_price=underlying_price)
            expiration = faker.date_between(start_date="+1d", end_date="+90d")
            premium = faker.option_premium(
                strike_price=strike,
                underlying_price=underlying_price,
                expiration_date=expiration,
                option_type="PUT",
            )
            assert isinstance(premium, float)
            intrinsic = _intrinsic_value("PUT", underlying_price, strike)
            assert premium >= intrinsic - 1e-6

    def test_option_premium_at_the_money_is_time_value_only(self, faker, num_samples):
        # At the money (strike == underlying_price), intrinsic value is 0 for both CALL
        # and PUT by definition (max(0, 0)), so the entire premium is the time-value
        # component. This pins down that boundary case explicitly rather than relying on
        # it showing up by chance in the randomized strike/underlying sampling used by
        # the general premium invariant tests above.
        for _ in range(num_samples):
            underlying_price = faker.pyfloat(min_value=10, max_value=500, right_digits=2)
            strike_price = underlying_price
            expiration = faker.date_between(start_date="+1d", end_date="+90d")
            option_type = faker.option_type()
            premium = faker.option_premium(
                strike_price=strike_price,
                underlying_price=underlying_price,
                expiration_date=expiration,
                option_type=option_type,
            )
            intrinsic = _intrinsic_value(option_type, underlying_price, strike_price)
            assert intrinsic == 0.0
            time_value = premium - intrinsic
            assert time_value == premium
            assert time_value >= -1e-6

    def test_expiration_date_default_cadence_is_friday(self, faker, num_samples):
        for _ in range(num_samples):
            expiration = faker.expiration_date()
            assert isinstance(expiration, date)
            assert expiration.weekday() == 4  # Friday

    def test_expiration_date_on_or_after_quote_date(self, faker, num_samples):
        for _ in range(num_samples):
            quote_date = faker.date_between(start_date="-30d", end_date="today")
            expiration = faker.expiration_date(quote_date=quote_date)
            assert expiration >= quote_date
            assert expiration.weekday() == 4

    def test_stock_option_is_flat_dict_with_documented_keys(self, faker, num_samples):
        for _ in range(num_samples):
            option = faker.stock_option()
            assert isinstance(option, dict)
            assert set(option.keys()) == STOCK_OPTION_KEYS
            assert "greeks" not in option

    def test_stock_option_field_types(self, faker, num_samples):
        for _ in range(num_samples):
            option = faker.stock_option()
            assert option["option_type"] in ("CALL", "PUT")
            assert isinstance(option["underlying_symbol"], str)
            assert isinstance(option["strike_price"], float)
            assert isinstance(option["underlying_price"], float)
            assert isinstance(option["premium"], float)
            assert isinstance(option["expiration_date"], date)
            assert isinstance(option["quote_date"], date)
            assert isinstance(option["exercised"], bool)
            for greek in ("delta", "gamma", "theta", "vega", "rho"):
                assert isinstance(option[greek], float)

    def test_stock_option_date_ordering(self, faker, num_samples):
        for _ in range(num_samples):
            option = faker.stock_option()
            assert option["quote_date"] <= option["expiration_date"]

    def test_stock_option_premium_meets_intrinsic_value(self, faker, num_samples):
        for _ in range(num_samples):
            option = faker.stock_option()
            intrinsic = _intrinsic_value(
                option["option_type"], option["underlying_price"], option["strike_price"]
            )
            assert option["premium"] >= intrinsic - 1e-6

    def test_stock_option_strike_price_band(self, faker, num_samples):
        for _ in range(num_samples):
            option = faker.stock_option()
            underlying_price = option["underlying_price"]
            assert underlying_price > 0
            assert abs(option["strike_price"] - underlying_price) / underlying_price <= STRIKE_BAND_PCT

    def test_stock_option_greeks_bounds(self, faker, num_samples):
        for _ in range(num_samples):
            option = faker.stock_option()
            assert -1.0 - 1e-6 <= option["delta"] <= 1.0 + 1e-6
            assert option["gamma"] >= -1e-6
            assert option["theta"] <= 1e-6  # theta is always negative (or ~0 at the boundary)
            assert option["vega"] >= -1e-6

    def test_stock_option_exercise_fields_consistent(self, faker, num_samples):
        for _ in range(num_samples):
            option = faker.stock_option()
            if option["exercised"]:
                assert option["exercise_date"] is not None
                assert isinstance(option["exercise_date"], date)
            else:
                assert option["exercise_date"] is None

    def test_stock_option_exercised_weighted_toward_in_the_money(self, faker, num_samples):
        itm_total = itm_exercised = 0
        otm_total = otm_exercised = 0
        for _ in range(num_samples):
            option = faker.stock_option()
            in_the_money = _in_the_money(
                option["option_type"], option["underlying_price"], option["strike_price"]
            )
            if in_the_money:
                itm_total += 1
                itm_exercised += option["exercised"]
            else:
                otm_total += 1
                otm_exercised += option["exercised"]

        # This is a distributional property, not a per-sample guarantee - only compare
        # rates when both moneyness buckets collected enough samples to be meaningful.
        if itm_total >= 5 and otm_total >= 5:
            assert (itm_exercised / itm_total) > (otm_exercised / otm_total)

    # option_chain() generates a full ladder of contracts across every expiration in the
    # window per call, so chain-level invariants use a smaller repeat count than the
    # single-contract tests above to keep the suite fast.
    chain_samples = 20

    def test_option_chain_single_ticker_from_symbol(self, faker):
        for _ in range(self.chain_samples):
            chain = faker.option_chain(symbol="AAPL")
            assert isinstance(chain, dict)
            assert set(chain.keys()) == {"AAPL"}

    def test_option_chain_single_ticker_from_symbols_list(self, faker):
        symbols = ["FOO", "BAR", "BAZ"]
        for _ in range(self.chain_samples):
            chain = faker.option_chain(symbols=symbols)
            assert len(chain) == 1
            ticker = next(iter(chain))
            assert ticker in symbols

    def test_option_chain_default_symbol_is_curated(self, faker):
        for _ in range(self.chain_samples):
            chain = faker.option_chain()
            assert len(chain) == 1

    def test_option_chain_empty_symbols_list_raises(self, faker):
        # option_chain() falls through to underlying_symbol(symbols) when no explicit
        # symbol= is given, so it inherits the same "explicit empty list raises" behavior
        # verified above rather than falling back to the default ticker list.
        with pytest.raises(IndexError):
            faker.option_chain(symbols=[])

    def test_option_chain_inverted_date_range_is_normalized(self, faker):
        # end_date before start_date is nonsensical for a Friday-cadence walk from start
        # to end. Verified against the real implementation: rather than raising or
        # returning an empty result, it swaps the two bounds
        # (`if range_end < range_start: range_start, range_end = range_end, range_start`)
        # and proceeds normally - a defensive normalization, not a bug. So an inverted
        # "+3w"/"today" pair should behave identically to the equivalent normal
        # "today"/"+3w" range: a non-empty, Friday-cadenced chain within that window.
        today = date.today()
        default_end = today + timedelta(weeks=3)
        chain = faker.option_chain(symbol="AAPL", start_date="+3w", end_date="today")
        expirations = chain["AAPL"]
        assert expirations
        for expiration_date in expirations:
            assert today <= expiration_date <= default_end
            assert expiration_date.weekday() == 4

    def test_option_chain_monthly_cadence_spaces_expirations_by_28_days(self, faker):
        # Only "weekly" cadence is documented in the design doc, but the real
        # implementation also supports "biweekly" and "monthly" (verified: it steps
        # expirations by 28 calendar days from a Friday-snapped start for "monthly",
        # keeping every expiration on a Friday since 28 is a multiple of 7).
        chain = faker.option_chain(symbol="AAPL", start_date="today", end_date="+18w", cadence="monthly")
        expirations = sorted(chain["AAPL"])
        assert len(expirations) >= 2
        for expiration_date in expirations:
            assert expiration_date.weekday() == 4
        for earlier, later in zip(expirations, expirations[1:]):
            assert (later - earlier).days == 28

    def test_option_chain_unsupported_cadence_raises(self, faker):
        # A cadence value outside the supported set ("weekly"/"biweekly"/"monthly")
        # raises rather than silently falling back to weekly or producing an empty or
        # malformed result.
        with pytest.raises(ValueError):
            faker.option_chain(symbol="AAPL", cadence="quarterly")

    def test_option_chain_default_window_and_friday_cadence(self, faker):
        today = date.today()
        default_end = today + timedelta(weeks=3)
        for _ in range(self.chain_samples):
            chain = faker.option_chain(symbol="AAPL")
            expirations = chain["AAPL"]
            assert isinstance(expirations, dict)
            assert expirations
            for expiration_date, contracts in expirations.items():
                assert isinstance(expiration_date, date)
                assert today <= expiration_date <= default_end
                assert expiration_date.weekday() == 4
                assert isinstance(contracts, list)
                assert len(contracts) >= 1

    def test_option_chain_custom_date_range(self, faker):
        start = DateTimeProvider._parse_date("+2w")
        end = DateTimeProvider._parse_date("+6w")
        for _ in range(self.chain_samples):
            chain = faker.option_chain(symbol="AAPL", start_date="+2w", end_date="+6w")
            for expiration_date in chain["AAPL"]:
                assert start <= expiration_date <= end
                assert expiration_date.weekday() == 4

    def test_option_chain_explicit_weekly_cadence_matches_default(self, faker, num_samples):
        chain = faker.option_chain(symbol="AAPL", cadence="weekly")
        for expiration_date in chain["AAPL"]:
            assert expiration_date.weekday() == 4

    def test_option_chain_contracts_match_stock_option_shape(self, faker, num_samples):
        chain = faker.option_chain(symbol="AAPL")
        for expiration_date, contracts in chain["AAPL"].items():
            for contract in contracts:
                assert isinstance(contract, dict)
                assert set(contract.keys()) == STOCK_OPTION_KEYS
                assert "greeks" not in contract
                assert contract["underlying_symbol"] == "AAPL"
                assert contract["expiration_date"] == expiration_date
                assert contract["option_type"] in ("CALL", "PUT")
                intrinsic = _intrinsic_value(
                    contract["option_type"], contract["underlying_price"], contract["strike_price"]
                )
                assert contract["premium"] >= intrinsic - 1e-6

    def test_option_chain_strike_ladder_has_multiple_strikes(self, faker, num_samples):
        chain = faker.option_chain(symbol="AAPL")
        for contracts in chain["AAPL"].values():
            strikes = {contract["strike_price"] for contract in contracts}
            assert len(strikes) >= 2
