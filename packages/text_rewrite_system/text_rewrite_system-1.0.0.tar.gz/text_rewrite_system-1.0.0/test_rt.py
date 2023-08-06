import subprocess
import importlib.util
import sys
import pytest

from .text_rewrite_system import convert_file

@pytest.mark.dependency()
def test_convert_file():
    assert convert_file("test/test.pyrt") == "test/test.py"

@pytest.fixture
def import_converted_file():
    file_path = "test/test.py"
    module_name = "test"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module

@pytest.mark.dependency(depends=["test_convert_file"])
def test_simple_conversion(import_converted_file):
    assert import_converted_file.test_function("hello world!") == "olá mundo!"

@pytest.mark.dependency(depends=["test_convert_file"])
def test_conversion_with_callable(import_converted_file):
    assert import_converted_file.test_function("hello Sofia!") == "olá SOFIA!"

@pytest.mark.dependency(depends=["test_convert_file"])
def test_conversion_with_capturing_group(import_converted_file):
    assert import_converted_file.test_function("hello! my name is Sofia!") == "olá! o meu nome é Sofia!"

@pytest.mark.dependency(depends=["test_convert_file"])
def test_conversion_with_conditional_true(import_converted_file):
    assert import_converted_file.test_function("hello! I am Sofia!") == "olá! eu sou a Sofia!"

@pytest.mark.dependency(depends=["test_convert_file"])
def test_conversion_with_conditional_false(import_converted_file):
    assert import_converted_file.test_function("hello! I am José!") == "olá! eu sou José!"



@pytest.mark.dependency(depends=["test_convert_file"])
def test_simple_conversion_smart_case(import_converted_file):
    assert import_converted_file.test_function_smart_case("Hello world!") == "Olá mundo!"

@pytest.mark.dependency(depends=["test_convert_file"])
def test_conversion_with_capturing_group_smart_case(import_converted_file):
    assert import_converted_file.test_function_smart_case("Hello! My name is Sofia!") == "Olá! O meu nome é Sofia!"

@pytest.mark.dependency(depends=["test_convert_file"])
def test_conversion_with_conditional_smart_case(import_converted_file):
    assert import_converted_file.test_function_smart_case("Hello! I am Sofia!") == "Olá! eu sou a Sofia!"
