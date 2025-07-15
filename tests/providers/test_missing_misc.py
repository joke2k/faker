# test_missing_misc.py
import json
import pytest
from unittest.mock import patch
from faker import exceptions, Faker # Importe Faker aqui para usar Faker.seed()

# --- Fixture simplificada ---
@pytest.fixture
def faker():
    return Faker()

# Fixture para misc_provider
@pytest.fixture
def misc_provider():
    from faker.providers.misc import Provider as MiscProvider
    f = Faker()
    # Cria uma instância do MiscProvider e associa ela à instância COMPLETA do Faker
    provider_instance = MiscProvider(f)
    return provider_instance

# --- password() ---
def test_password_only_special_chars(misc_provider):
    pwd = misc_provider.password(special_chars=True, digits=False, upper_case=False, lower_case=False)
    assert all(c in "!@#$%^&*()_+" for c in pwd)

def test_password_only_digits(misc_provider):
    pwd = misc_provider.password(special_chars=False, digits=True, upper_case=False, lower_case=False)
    assert all(c.isdigit() for c in pwd)

def test_password_only_uppercase(misc_provider):
    pwd = misc_provider.password(special_chars=False, digits=False, upper_case=True, lower_case=False)
    assert all(c.isupper() for c in pwd)

# --- binary() ---
def test_binary_size(misc_provider):
    data = misc_provider.binary(length=1024)
    assert len(data) == 1024
    assert isinstance(data, bytes)

def test_binary_seeded(misc_provider):
    # CORREÇÃO: Usar o método de classe Faker.seed()
    Faker.seed(42)
    data1 = misc_provider.binary(length=16)
    Faker.seed(42)
    data2 = misc_provider.binary(length=16)
    assert data1 == data2

# --- boolean() ---
def test_boolean_default(misc_provider):
    results = [misc_provider.boolean() for _ in range(100)]
    assert any(results) and not all(results)

def test_boolean_custom_chance(misc_provider):
    results = [misc_provider.boolean(chance_of_getting_true=25) for _ in range(100)]
    assert sum(results) < 40  # ~25%

# --- null_boolean() ---
def test_null_boolean(misc_provider):
    results = [misc_provider.null_boolean() for _ in range(100)]
    assert None in results
    assert True in results
    assert False in results

# --- dsv() ---
def test_dsv_without_header(misc_provider):
    with patch.object(misc_provider.generator, 'pystr_format', side_effect=["Name1", "Address1"]):
        data_columns = ["{{name}}", "{{address}}"] 
        result = misc_provider.dsv(header=None, data_columns=data_columns, num_rows=1)
        lines = result.strip().splitlines()
        assert len(lines) == 1
        assert lines[0] == '"Name1","Address1"' # CSV com QUOTE_ALL adiciona aspas duplas.


def test_dsv_with_row_ids(misc_provider):
    with patch.object(misc_provider.generator, 'pystr_format', side_effect=["Name1", "Email1", "Name2", "Email2"]):
        data_columns = ["{{name}}", "{{email}}"] # Usar tokens
        result = misc_provider.dsv(header=None, data_columns=data_columns, num_rows=2, include_row_ids=True)
        lines = result.strip().splitlines()
        assert len(lines) == 2
        assert lines[0] == '"1","Name1","Email1"' # Ajustado para esperar aspas no '1'
        assert lines[1] == '"2","Name2","Email2"' # Ajustado para esperar aspas no '2'



# --- json() ---
def test_json_simple_structure(misc_provider):
    # Aqui, "name" e "pyint" são nomes de provedores, então o _value_format_selection
    # vai chamar self.generator.format(provider_name)
    with patch.object(misc_provider.generator, 'format') as mock_format:
        # Configura o side_effect para retornar valores diferentes para 'name' e 'pyint'
        mock_format.side_effect = lambda provider_name, *args, **kwargs: {
            "name": "Test Name",
            "pyint": 30,
        }.get(provider_name)

        data_columns = {"name": "name", "age": "pyint"}  # Nomes diretos de provedores
        result = misc_provider.json(data_columns=data_columns, num_rows=1)
        data = json.loads(result)
        assert data["name"] == "Test Name"
        assert data["age"] == 30
        # Verifica se format foi chamado para 'name' e 'pyint'
        calls = mock_format.call_args_list
        assert any(call.args[0] == "name" for call in calls)
        assert any(call.args[0] == "pyint" for call in calls)

def test_json_complex_structure(misc_provider):
    def format_side_effect(provider, *args, **kwargs):
        if provider == "name":
            return "Complex Name"
        elif provider == "street_address":
            return "123 Main St"
        elif provider == "uuid4":
            return "mock-uuid-4"
        return None

    with patch.object(misc_provider.generator, 'format', side_effect=format_side_effect):
        data_columns = {
            "id": "uuid4",
            "profile": {
                "name": "name",
                "addresses": [
                    {"type": "home", "street": "street_address"},
                    {"type": "work", "street": "street_address"}
                ]
            }
        }
        result = misc_provider.json(data_columns=data_columns, num_rows=1)
        data = json.loads(result)
        assert data["profile"]["name"] == "Complex Name"
        assert data["profile"]["addresses"][0]["street"] == "123 Main St"

# --- fixed_width() ---
def test_fixed_width_basic(misc_provider):
    with patch.object(misc_provider.generator, 'format') as mock_format:
        mock_format.side_effect = lambda provider_name, *args, **kwargs: {
            "name": "TestName",
            "pyint": 50,
        }.get(provider_name)

        data_columns = [(10, "name"), (5, "pyint", {"min_value": 1, "max_value": 100})]
        result = misc_provider.fixed_width(data_columns=data_columns, num_rows=1)
        
        # line = result # Removido o .strip() anteriormente, então 'result' já é a string exata

        # 'TestName' (8 chars) alinhado à esquerda em 10 -> 'TestName  '
        # '50' (2 chars) alinhado à esquerda em 5 -> '50   '
        # A linha esperada é 'TestName  50   ' (sem quebra de linha final para num_rows=1).
        assert result == "TestName  50   " # Ajustado para não esperar '\n'

def test_fixed_width_alignment(misc_provider):
    with patch.object(misc_provider.generator, 'format', return_value="John Doe"):
        data_columns = [(10, "name")]
        result = misc_provider.fixed_width(data_columns=data_columns, num_rows=1)
        
        line = result # Remove .strip()

        # "John Doe" (8 caracteres) em um campo de 10 caracteres, alinhado à esquerda
        # deve resultar em "John Doe  " (8 caracteres + 2 espaços)
        # E como num_rows=1, não haverá '\n' final.
        assert line == "John Doe  " # 10 caracteres com padding, sem '\n' final


# --- _value_format_selection() ---
def test_value_format_selection_token(misc_provider):
    with patch.object(misc_provider.generator, 'format', return_value="Hello John Doe"):
        result = misc_provider._value_format_selection("name")
        assert result == "Hello John Doe"

def test_value_format_selection_fixed(misc_provider):
    result = misc_provider._value_format_selection("@fixed_value")
    assert result == "fixed_value"

def test_value_format_selection_provider(misc_provider):
    with patch.object(misc_provider.generator, 'format', return_value="formatted_data") as mock_format:
        result = misc_provider._value_format_selection("provider_name")
        mock_format.assert_called_with("provider_name")
        assert result == "formatted_data"

# --- Testes de erro ---
def test_dsv_invalid_num_rows(misc_provider):
    with pytest.raises(ValueError):
        misc_provider.dsv(num_rows=0)
    
    with pytest.raises(ValueError):
        misc_provider.dsv(num_rows=-1)

def test_json_invalid_data_columns(misc_provider):
    with pytest.raises(TypeError):
        misc_provider.json(data_columns="invalid_type")

def test_fixed_width_invalid_arguments(misc_provider):
    with pytest.raises(TypeError):
        misc_provider.fixed_width(data_columns=[(10, "name", "invalid_kwargs")])