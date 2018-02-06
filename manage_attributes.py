import manage_requests
import _environment
import requests
import manage_xml

attributes_to_be_checked = {"Test1":"Test1",
                            "Test2":"Test2",
                            "Test3":"Test3"
                            }

def get_domain_name_of_given_attribute(env, attribute_name):

    request_specification = f"/rest/service/admin/attributes/{attribute_name}"
    request = manage_requests.prepare_get_request(env, request_specification)
    get_response = requests.get(request)

    forms_list_values = manage_xml.extract_xml_elements_by_path(get_response.content, './/attributeInfo//domainName')
    forms_list_text_values = list(map(lambda x: x.text, forms_list_values))
    return forms_list_text_values[0]

def get_incorrect_attribute_domains(env):

    incorrect_attribute_domains = {}

    for attribute in attributes_to_be_checked:
        domain_value = get_domain_name_of_given_attribute(env, attribute)
        if attributes_to_be_checked[attribute] != domain_value:
            incorrect_attribute_domains[attribute] = domain_value

    return incorrect_attribute_domains
