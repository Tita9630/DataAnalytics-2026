contact_info = {
    "name": "Luna David",
    "address": "1234 st",
    "city": "Charlseton",
    "state": "SC",
    "zip": "01234"
}

print(f"""
{contact_info["name"]}
{contact_info['address']}
{contact_info['city']}, {contact_info["state"]} {contact_info["zip"]}
""")

del contact_info["name"] # removing name 

full_name = {
    "first name": "Luna",
    "last name": "David"
}
full_name.update({"honorific": "Ms."})
contact_info.update({"full_name": full_name})

print(f"""
{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]} {contact_info["city"]}, {contact_info["state"]} 
{contact_info["zip"]}""")