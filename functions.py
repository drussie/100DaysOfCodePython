# functions with outputs
def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"

# format_name("marcOs", "TennisOPEDIA")
formatted_string = format_name("marcOs", "TeNnisOPEDIA")
print(formatted_string)
