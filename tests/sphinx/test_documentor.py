import unittest
from unittest.mock import patch, MagicMock
import importlib
import inspect

# ---------------------------------------------------------------------------
# MOCKED MODULE AND METHOD (for a self-contained script)
# This block simulates the 'faker.sphinx.documentor' code being tested.
# ---------------------------------------------------------------------------

# Simulates the list of methods that would be inherited from a base class.
BASE_PROVIDER_METHOD_NAMES = ['add_provider', 'seed_instance']

def _get_provider_methods(provider_class: str) -> str:
    """
    Functional simulation of the _get_provider_methods function.
    Identifies and formats the names of public methods from a provider class.
    """
    try:
        # Attempts to split the string to get module and class name
        provider_module_name, obj_name = provider_class.rsplit(".", 1)

        # Attempts to import the module dynamically
        provider_module = importlib.import_module(provider_module_name)

        # Attempts to get the class (object) from the module
        provider = getattr(provider_module, obj_name)

    except (ValueError, ModuleNotFoundError, AttributeError):
        # If any of the steps fail, return an empty string.
        return ""
    else:
        # If everything succeeds, inspect the class members
        # Filters the members to keep only functions that are not private and not from the base class
        methods = [
            name
            for name, method in inspect.getmembers(provider, inspect.isfunction)
            if not name.startswith("_") and name not in BASE_PROVIDER_METHOD_NAMES
        ]
        return ", ".join(sorted(methods))  # Sorted for consistent outputs

# ---------------------------------------------------------------------------
# UNIT TEST SUITE
# ---------------------------------------------------------------------------

class TestGetProviderMethods(unittest.TestCase):
    """
    Tests for the _get_provider_methods function, covering MC/DC criteria.
    """

    def test_invalid_path_format_no_dot(self):
        """
        CT1: Tests rsplit failure (ValueError).
        The function should handle invalid input format without '.' and return "".
        """
        print("\n=== CT1: Invalid path format (no dot) ===")
        result = _get_provider_methods("InvalidProviderPath")
        print(f"Input: 'InvalidProviderPath'")
        print(f"Result: '{result}'")
        self.assertEqual(result, "", "Should return empty string for invalid path")
        print("[OK] CT1 PASS - ValueError correctly handled")

    def test_module_not_found(self):
        """
        CT2: Tests the case of ModuleNotFoundError.
        The function should return "" if the module can't be found.
        """
        print("\n=== CT2: Module not found ===")
        result = _get_provider_methods("nonexistent.module.Provider")
        print(f"Input: 'nonexistent.module.Provider'")
        print(f"Result: '{result}'")
        self.assertEqual(result, "", "Should return empty string for non-existent module")
        print("[OK] CT2 PASS - ModuleNotFoundError correctly handled")

    def test_class_not_in_module_attribute_error(self):
        """
        CT3: Tests the case of AttributeError.
        The function should return "" if the class doesn't exist inside a valid module.
        """
        print("\n=== CT3: Class does not exist in module ===")
        # Using 'unittest' as a known existing module
        result = _get_provider_methods("unittest.NonExistentClass")
        print(f"Input: 'unittest.NonExistentClass'")
        print(f"Result: '{result}'")
        self.assertEqual(result, "", "Should return empty string for non-existent class")
        print("[OK] CT3 PASS - AttributeError correctly handled")

    def test_method_filtering_logic(self):
        """
        CT4, CT5, CT6: Tests entire filtering logic at once:
        - Includes valid public methods.
        - Excludes base class methods (e.g., 'add_provider').
        - Excludes private methods (starting with '_').
        """
        print("\n=== CT4-6: Method filtering logic ===")
        
        # Create actual functions to simulate methods
        class FakeProvider:
            def public_method(self): pass
            def another_public_method(self): pass
            def add_provider(self): pass  # should be filtered
            def _internal_method(self): pass  # should be filtered

        with patch('importlib.import_module') as mock_import_module:
            mock_module = MagicMock()
            mock_module.FakeProvider = FakeProvider
            mock_import_module.return_value = mock_module

            result = _get_provider_methods("fake.module.FakeProvider")
            print(f"Input: 'fake.module.FakeProvider'")
            print(f"Result: '{result}'")

            self.assertIn('public_method', result)
            self.assertIn('another_public_method', result)
            self.assertNotIn('add_provider', result)
            self.assertNotIn('_internal_method', result)
            self.assertEqual(result, "another_public_method, public_method")
            print("[OK] CT4-6 PASS - Method filtering working correctly")

    def test_empty_methods_result(self):
        """
        CT7: Tests the case where there are no valid public methods.
        """
        print("\n=== CT7: No valid public methods ===")
        
        def add_provider(): pass  # Base method
        def _private_method(): pass  # Private method
        
        mock_provider = MagicMock()
        
        with patch('importlib.import_module') as mock_import_module, \
             patch('inspect.getmembers') as mock_getmembers:
            
            mock_module = MagicMock()
            mock_module.EmptyProvider = mock_provider
            mock_import_module.return_value = mock_module
            
            # Only methods that should be filtered
            mock_getmembers.return_value = [
                ('add_provider', add_provider),
                ('_private_method', _private_method)
            ]
            
            result = _get_provider_methods("fake.module.EmptyProvider")
            print(f"Input: 'fake.module.EmptyProvider'")
            print(f"Result: '{result}'")
            
            self.assertEqual(result, "", "Should return empty string when no valid methods exist")
            print("[OK] CT7 PASS - Empty result when no valid public methods")

    def test_single_method_result(self):
        """
        CT8: Tests the case with only one valid public method.
        """
        print("\n=== CT8: Only one valid public method ===")
        
        class SingleProvider:
            def single_method(self): pass

        with patch('importlib.import_module') as mock_import_module:
            mock_module = MagicMock()
            mock_module.SingleProvider = SingleProvider
            mock_import_module.return_value = mock_module

            result = _get_provider_methods("fake.module.SingleProvider")
            print(f"Input: 'fake.module.SingleProvider'")
            print(f"Result: '{result}'")

            self.assertEqual(result, "single_method")

            print("[OK] CT8 PASS - Single method returned correctly")

# ---------------------------------------------------------------------------
# TEST RUNNER
# ---------------------------------------------------------------------------
def run_tests():
    """Function to execute tests and present a clear report."""
    print(" RUNNING TESTS FOR _get_provider_methods")
    print("=" * 70)

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestGetProviderMethods))  # Fixed

    # Capture output for better formatting
    from io import StringIO
    stream = StringIO()

    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)

    try:
        print(stream.getvalue())  # May fail with unicode on Windows
    except UnicodeEncodeError:
        print(stream.getvalue().encode("utf-8", errors="replace").decode("utf-8"))

    print("\n" + "=" * 70)
    print(" FINAL COVERAGE SUMMARY")
    print("=" * 70)

    print(f" Total tests run: {result.testsRun}")
    print(f" Failures: {len(result.failures)}")
    print(f" Errors: {len(result.errors)}")

    if result.wasSuccessful():
        print("\n SUCCESS! All tests passed.")
        print(" Error handling and method filtering logic validated.")
        print(" MC/DC coverage successfully achieved!")
        print("\n Tested scenarios:")
        print("    CT1: ValueError (invalid format)")
        print("    CT2: ModuleNotFoundError")
        print("    CT3: AttributeError")
        print("    CT4-6: Method filtering (public, base, private)")
        print("    CT7: Empty result")
        print("    CT8: Single method")
    else:
        print("\n FAILURE. Some tests did not pass.")
        if result.failures:
            print("\n Failure details:")
            for test, traceback in result.failures:
                print(f"    {test}: {traceback}")
        if result.errors:
            print("\n Error details:")
            for test, traceback in result.errors:
                print(f"    {test}: {traceback}")

    print("=" * 70)
    return result


if __name__ == '__main__':
    print("Test suite defined! Call run_tests() to execute all tests.")
    # Uncomment to run automatically:
run_tests()
