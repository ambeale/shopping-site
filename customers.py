"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {}, {}, {}>".format(self.first_name, self.last_name, self.email)

def read_customer_file(filename):
    """Read in txt file of customer info"""

    customers = {}

    with open(filename) as file:
        for line in file:
            (first_name, 
             last_name, 
             email, 
             password) = line.strip().split("|")
            
            customers[email] = Customer(first_name, 
                                        last_name, 
                                        email, 
                                        password)

    return customers

def get_by_email(email):
    """Search customers by email."""

    return customers.get(email)


customers = read_customer_file("customers.txt")