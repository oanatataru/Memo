def build_xml_element(tag, content, **attributes):
    xml_str = f"<{tag}"

    for key, value in attributes.items():
        xml_str += f' {key}="{value}"'

    xml_str += f">{content}</{tag}>"
    return xml_str


print(build_xml_element("a", "Hello there", href="http://python.org", class_="my-link", id="someid"))
