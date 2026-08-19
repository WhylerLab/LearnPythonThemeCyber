# dock_tools.py

# OBEJCTIVE siehe main.py


def kg_to_tons(kg):
    tons = round(kg / 1000,2)
    return tons



def format_manifest(item, qty):
    return f'{item.upper()} x{qty}'