from ecommerce.customer import contact  # absolute import 
print("Sales initialized.", __name__)
# from ..customer import contact # relative import

contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass


# Executing Modules as Script
if __name__ == "__main__":
    print("Sales started")
    calc_tax()
