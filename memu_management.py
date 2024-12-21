def add_items(items,add_item):
    if add_item not in items:
        items.append(add_item)
    return items

def remove_items(items,remove_item):
    if remove_item in items:
        items.remove(remove_item)
    else:
        print(f"{remove_item} does not exists in menu")
    return items

def check_items(items,check_item):
    return f"{check_item} is available" if check_item in items else f"{check_item} is not available"

items=["Pizza","Burger","Pasta","Salad"]
add_item="Tacos"
remove_item="Salad"
check_item="Pizza"

update_menu=add_items(items,add_item)
update_menu=remove_items(items,remove_item)

check=check_items(items,check_item)

print(f"Updated menu: {update_menu}")
print(f"Availability: {check}")

