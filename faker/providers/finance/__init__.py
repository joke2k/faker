import re

from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple

from ...typing import DateParseType
from .. import BaseProvider


class Provider(BaseProvider):
    """Implement default finance provider for Faker.

    Generates fake listed call/put stock option contracts and option chains for
    fintech application testing. Strike prices, premiums, and Greeks are
    plausibility-shaped heuristics (moneyness- and time-to-expiry-aware), not
    output from a real options-pricing model such as Black-Scholes.
    """

    stock_tickers: Tuple[str, ...] = (
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN",
        "META",
        "TSLA",
        "NVDA",
        "JPM",
        "V",
        "MA",
        "WMT",
        "DIS",
        "NFLX",
        "INTC",
        "AMD",
        "BA",
        "KO",
        "PEP",
        "MCD",
        "NKE",
        "ADBE",
        "CSCO",
        "ORCL",
        "IBM",
        "GE",
        "F",
        "GM",
        "XOM",
        "CVX",
        "PFE",
        "JNJ",
        "UNH",
        "HD",
        "COST",
        "PG",
        "T",
        "VZ",
        "CRM",
        "PYPL",
        "SBUX",
    )

    # Number of calendar days a cadence value advances between expirations.
    # Multiples of 7 so every cadence stays aligned to the same weekday once
    # the first expiration is snapped to a Friday.
    option_chain_cadences: Dict[str, int] = {
        "weekly": 7,
        "biweekly": 14,
        "monthly": 28,
    }

    _relative_date_re = re.compile(r"^([+-]\d+)(d|w|y)$")

    def option_type(self) -> str:
        """Generate a random option type: ``CALL`` or ``PUT``."""
        return self.random_element(("CALL", "PUT"))

    def underlying_symbol(self, symbols: Optional[List[str]] = None) -> str:
        """Generate a ticker symbol for an option's underlying stock.

        If ``symbols`` is given, the ticker is picked from that list. Otherwise
        it falls back to a built-in curated list of common stock tickers.
        """
        return self.random_element(symbols if symbols is not None else self.stock_tickers)

    def strike_price(self, underlying_price: Optional[float] = None) -> float:
        """Generate a strike price relative to an underlying price.

        The strike is generated within roughly +/-20% of ``underlying_price``
        (generated if not supplied) and snapped to standard exchange strike
        increments.
        """
        if underlying_price is None:
            underlying_price = self._generate_underlying_price()
        offset = self.generator.random.uniform(-0.2, 0.2)
        raw_strike = underlying_price * (1 + offset)
        increment = self._strike_increment(underlying_price)
        strike = round(raw_strike / increment) * increment
        return max(increment, round(strike, 2))

    def option_premium(
        self,
        strike_price: Optional[float] = None,
        underlying_price: Optional[float] = None,
        expiration_date: Optional[date] = None,
        option_type: Optional[str] = None,
    ) -> float:
        """Generate an option premium.

        Priced as intrinsic value plus a bounded random time-value component
        that shrinks as ``expiration_date`` approaches today. Not a real
        options-pricing model. Any omitted argument is generated internally,
        so this can be called standalone as ``option_premium()``.
        """
        if underlying_price is None:
            underlying_price = self._generate_underlying_price()
        if strike_price is None:
            strike_price = self.strike_price(underlying_price)
        if expiration_date is None:
            expiration_date = self.expiration_date()
        if option_type is None:
            option_type = self.option_type()

        intrinsic_value = self._intrinsic_value(strike_price, underlying_price, option_type)
        days_to_expiration = max((expiration_date - date.today()).days, 0)
        time_value_cap = max(underlying_price * 0.05 * min(days_to_expiration, 90) / 90, 0.01)
        time_value = self.generator.random.uniform(0, time_value_cap)
        return round(intrinsic_value + time_value, 2)

    def option_greeks(
        self,
        strike_price: Optional[float] = None,
        underlying_price: Optional[float] = None,
        expiration_date: Optional[date] = None,
        option_type: Optional[str] = None,
        quote_date: Optional[date] = None,
    ) -> Dict[str, float]:
        """Generate heuristic option Greeks: delta, gamma, theta, vega, and rho.

        These are moneyness- and time-to-expiry-shaped approximations for
        test-data purposes (delta scaled toward +/-1 deep in-the-money, toward
        0 deep out-of-the-money; theta always negative and larger in magnitude
        near expiration), not the output of a real Black-Scholes or binomial
        pricing model. Any omitted argument is generated internally, so this
        can be called standalone as ``option_greeks()``.
        """
        if quote_date is None:
            quote_date = date.today()
        if underlying_price is None:
            underlying_price = self._generate_underlying_price()
        if strike_price is None:
            strike_price = self.strike_price(underlying_price)
        if expiration_date is None:
            expiration_date = self.expiration_date(quote_date)
        if option_type is None:
            option_type = self.option_type()

        moneyness = (underlying_price - strike_price) / underlying_price
        if option_type == "PUT":
            moneyness = -moneyness
        delta_magnitude = min(max(0.5 + moneyness * 2, 0.02), 0.98)
        delta = delta_magnitude if option_type == "CALL" else -delta_magnitude

        days_to_expiration = max((expiration_date - quote_date).days, 1)
        time_factor = max(1 - min(days_to_expiration, 90) / 90, 0.05)
        proximity_to_strike = max(1 - min(abs(moneyness), 1), 0.05)

        gamma = self.generator.random.uniform(0.01, 0.05) * proximity_to_strike
        theta = -self.generator.random.uniform(0.01, 0.10) * time_factor
        vega = self.generator.random.uniform(0.02, 0.20) * proximity_to_strike
        rho = self.generator.random.uniform(-0.05, 0.05)

        return {
            "delta": round(delta, 2),
            "gamma": round(gamma, 2),
            "theta": round(theta, 2),
            "vega": round(vega, 2),
            "rho": round(rho, 2),
        }

    def expiration_date(self, quote_date: Optional[date] = None) -> date:
        """Generate a future expiration date snapped to the weekly Friday cadence.

        ``quote_date`` is the as-of date the expiration is generated relative
        to (defaults to today). Uses
        :meth:`self.generator.date_between() <faker.providers.date_time.Provider.date_between>`
        under the hood.
        """
        if quote_date is None:
            quote_date = date.today()
        horizon = self.generator.date_between(start_date=quote_date, end_date=quote_date + timedelta(days=180))
        return self._snap_to_friday(horizon)

    def stock_option(self, symbols: Optional[List[str]] = None) -> Dict[str, Any]:
        """Generate a fake listed call/put stock option contract.

        Composes :meth:`underlying_symbol`, :meth:`option_type`,
        :meth:`strike_price`, :meth:`expiration_date`, :meth:`option_premium`,
        and :meth:`option_greeks`. Returns a flat ``dict`` with Greeks as
        top-level keys (not nested under a ``"greeks"`` key).
        """
        quote_date = date.today()
        underlying_symbol = self.underlying_symbol(symbols)
        option_type = self.option_type()
        underlying_price = self._generate_underlying_price()
        strike_price = self.strike_price(underlying_price)
        expiration_date = self.expiration_date(quote_date)

        return self._build_quote(
            underlying_symbol,
            option_type,
            strike_price,
            underlying_price,
            expiration_date,
            quote_date,
        )

    def option_chain(
        self,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        start_date: DateParseType = "today",
        end_date: DateParseType = "+3w",
        cadence: str = "weekly",
    ) -> Dict[str, Dict[date, List[Dict[str, Any]]]]:
        """Generate a fake option chain for a single underlying ticker.

        Returns a nested ``dict``: ticker -> expiration date -> a list of flat
        per-strike quotes (both a call and a put per strike), each quote in
        the same shape as :meth:`stock_option`'s return value. Expirations are
        generated between ``start_date`` and ``end_date`` (defaults to a
        3-week window from today) spaced by ``cadence`` (default ``"weekly"``,
        landing on Fridays; overridable to ``"biweekly"`` or ``"monthly"``).
        Only a single ticker is populated per call.
        """
        ticker = symbol or self.underlying_symbol(symbols)
        quote_date = date.today()
        range_start = self._resolve_date(start_date)
        range_end = self._resolve_date(end_date)
        if range_end < range_start:
            range_start, range_end = range_end, range_start

        underlying_price = self._generate_underlying_price()
        strikes = self._strike_ladder(underlying_price)
        expirations = self._expiration_series(range_start, range_end, cadence)

        by_expiration: Dict[date, List[Dict[str, Any]]] = {}
        for expiration in expirations:
            quotes = []
            for strike in strikes:
                for option_type in ("CALL", "PUT"):
                    quotes.append(
                        self._build_quote(
                            ticker,
                            option_type,
                            strike,
                            underlying_price,
                            expiration,
                            quote_date,
                        )
                    )
            by_expiration[expiration] = quotes

        return {ticker: by_expiration}

    def _build_quote(
        self,
        underlying_symbol: str,
        option_type: str,
        strike_price: float,
        underlying_price: float,
        expiration_date: date,
        quote_date: date,
    ) -> Dict[str, Any]:
        """Build one flat quote dict shared by :meth:`stock_option` and :meth:`option_chain`."""
        premium = self.option_premium(strike_price, underlying_price, expiration_date, option_type)
        greeks = self.option_greeks(strike_price, underlying_price, expiration_date, option_type, quote_date)
        exercised, exercise_date = self._exercise_outcome(strike_price, underlying_price, expiration_date, option_type)

        return {
            "underlying_symbol": underlying_symbol,
            "option_type": option_type,
            "strike_price": strike_price,
            "underlying_price": underlying_price,
            "premium": premium,
            "expiration_date": expiration_date,
            "quote_date": quote_date,
            "delta": greeks["delta"],
            "gamma": greeks["gamma"],
            "theta": greeks["theta"],
            "vega": greeks["vega"],
            "rho": greeks["rho"],
            "exercised": exercised,
            "exercise_date": exercise_date,
        }

    def _exercise_outcome(
        self,
        strike_price: float,
        underlying_price: float,
        expiration_date: date,
        option_type: str,
    ) -> Tuple[bool, Optional[date]]:
        """Derive ``exercised``/``exercise_date`` probabilistically from moneyness at expiration.

        Simulates a plausible underlying price at expiration via a bounded
        random walk from the current underlying price, then weights the
        exercise outcome heavily toward ``True`` when that hypothetical price
        would leave the contract in-the-money, and toward ``False`` otherwise.
        """
        price_at_expiration = underlying_price * self.generator.random.uniform(0.85, 1.15)
        in_the_money = self._intrinsic_value(strike_price, price_at_expiration, option_type) > 0
        exercise_probability = 0.85 if in_the_money else 0.05
        exercised = self.generator.random.random() < exercise_probability
        exercise_date = expiration_date if exercised else None
        return exercised, exercise_date

    def _generate_underlying_price(self) -> float:
        return round(self.generator.random.uniform(5.0, 500.0), 2)

    def _intrinsic_value(self, strike_price: float, underlying_price: float, option_type: str) -> float:
        if option_type == "CALL":
            return max(0.0, underlying_price - strike_price)
        return max(0.0, strike_price - underlying_price)

    def _strike_increment(self, price: float) -> float:
        if price < 25:
            return 0.5
        if price < 200:
            return 1.0
        return 5.0

    def _strike_ladder(self, underlying_price: float, strikes_per_expiration: int = 5) -> List[float]:
        increment = self._strike_increment(underlying_price)
        half = strikes_per_expiration // 2
        return sorted(
            max(increment, round(underlying_price + (offset - half) * increment, 2))
            for offset in range(strikes_per_expiration)
        )

    def _snap_to_friday(self, target_date: date) -> date:
        days_until_friday = (4 - target_date.weekday()) % 7
        return target_date + timedelta(days=days_until_friday)

    def _expiration_series(self, start: date, end: date, cadence: str) -> List[date]:
        if cadence not in self.option_chain_cadences:
            raise ValueError(f"Unsupported cadence {cadence!r}; expected one of {sorted(self.option_chain_cadences)}")
        step = timedelta(days=self.option_chain_cadences[cadence])
        current = self._snap_to_friday(start)
        expirations = []
        while current <= end:
            expirations.append(current)
            current += step
        return expirations

    def _resolve_date(self, value: DateParseType) -> date:
        """Resolve a small subset of |DateParseType| values to a concrete date.

        Supports ``date``/``datetime`` objects, ``timedelta``, an ``int``
        number of days from today, and the relative strings ``"today"``/
        ``"now"`` and ``"[+-]<N><d|w|y>"`` (e.g. ``"+3w"``, ``"-30d"``). This
        is a purposely small subset of the date-string grammar supported by
        :meth:`faker.providers.date_time.Provider.date_between` sufficient for
        :meth:`option_chain`'s ``start_date``/``end_date`` bounds.
        """
        if isinstance(value, datetime):
            return value.date()
        if isinstance(value, date):
            return value
        today = date.today()
        if isinstance(value, timedelta):
            return today + value
        if isinstance(value, int):
            return today + timedelta(days=value)
        if isinstance(value, str):
            if value in ("today", "now"):
                return today
            match = self._relative_date_re.match(value)
            if match:
                amount, unit = match.groups()
                amount = int(amount)
                if unit == "d":
                    return today + timedelta(days=amount)
                if unit == "w":
                    return today + timedelta(weeks=amount)
                return today + timedelta(days=round(amount * 365.24))
        raise ValueError(f"Unsupported date value for option_chain: {value!r}")
