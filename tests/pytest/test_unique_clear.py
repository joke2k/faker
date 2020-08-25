def test_unique_clears(testdir):
    """Successive uses of the `faker` pytest fixture have the
    generated unique values cleared between functions."""

    testdir.makepyfile(
        """
        def test_generate_two_unique_booleans(faker):
            faker.unique.boolean()
            faker.unique.boolean()

        def test_another_boolean(faker):
            faker.unique.boolean()
        """,
    )

    result = testdir.runpytest()

    result.assert_outcomes(passed=2)
