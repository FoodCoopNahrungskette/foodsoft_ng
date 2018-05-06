# Products and orders

class Supplier:
    """ holds supplier information and catalogs """
    pass

class ProductCatalog:
    """ contains the products of a supplier """
    pass

class Order:
    """ informations about a single order at a supplier """
    pass

class OrderItem:
    """ each product that is orderable in an order """
    pass

class ProductAssignment:
    """ contains information which group gets how many stuff """
    pass

class Product:
    """ holds informations about a product """
    pass


# User and group management

class Group:
    """ each user is assigned a group """
    pass

class User:
    """ holds informations like password etc about a user """
    pass

class Deposit:
    """ deposit information for a group """
    pass

class Duty:
    """ each user is assign a duty """
    pass

class DutySchedule:
    """ who is scheduled for which duty on which date """
    pass

# Misc

class BankAccounts:
    """ stores bank accounts """
    pass
