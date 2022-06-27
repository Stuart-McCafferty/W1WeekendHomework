# WRITE YOUR FUNCTIONS HERE
from token import PERCENTEQUAL


def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, new_money):
    cc_pet_shop["admin"]["total_cash"] += new_money

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, sold):
    shop["admin"]["pets_sold"] += sold

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pet_breed  = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pet_breed.append(pet)
    return pet_breed

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet
            

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, remove_cash):
    customer["cash"] = customer["cash"] - remove_cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(shop, pet, customer):
    if customer_can_afford_pet(customer, pet) and (pet != None):
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(shop, pet["price"])
        remove_pet_by_name(shop, pet["name"])
        add_pet_to_customer(customer, pet)
        increase_pets_sold(shop, 1)

    
