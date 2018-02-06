import manage_attributes
import pytest

def compose_error_message(environment):
    error_message = "\nIncorrect attribute domains: " + str(manage_attributes.get_incorrect_attribute_domains(environment))
    return error_message

def test_incorrect_attribute_domains(environment):
    assert len(manage_attributes.get_incorrect_attribute_domains(environment)) == 0, compose_error_message(environment)