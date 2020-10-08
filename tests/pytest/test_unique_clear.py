def test_unique_clears(testdir):
    """Successive uses of the `faker` pytest fixture have the
    generated unique values cleared between functions."""

    testdir.makepyfile(
        """
        import pytest
        from faker.exceptions import UniquenessException

        NUM_SAMPLES = 100

        def test_fully_exhaust_unique_booleans(faker):
            _dummy = [faker.boolean() for _ in range(NUM_SAMPLES)]

            faker.unique.boolean()
            faker.unique.boolean()
            with pytest.raises(UniquenessException):
                faker.unique.boolean()
            _dummy = [faker.boolean() for _ in range(NUM_SAMPLES)]

        def test_do_not_exhaust_booleans(faker):
            faker.unique.boolean()

        def test_fully_exhaust_unique_booleans_again(faker):
            _dummy = [faker.boolean() for _ in range(NUM_SAMPLES)]

            faker.unique.boolean()
            faker.unique.boolean()
            with pytest.raises(UniquenessException):
                faker.unique.boolean()
            _dummy = [faker.boolean() for _ in range(NUM_SAMPLES)]
        """,
    )

    result = testdir.runpytest()

    result.assert_outcomes(passed=3)
