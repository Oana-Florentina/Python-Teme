#4. The build_xml_element function receives the following parameters:
# tag, content, and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ",
# _class =" my-link ", id= " someid ") returns  the string =
# "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
def build_xml_element(tag, content, **attributes):
    # Start building the opening tag
    xml_element = f"<{tag}"

    # Add attributes to the opening tag with spaces and double quotes
    for attr, value in attributes.items():
        xml_element += f' {attr}="{value}"'

    # Close the opening tag
    xml_element += f">{content}</{tag}>"

    return xml_element

# Example usage:
xml = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(xml)
