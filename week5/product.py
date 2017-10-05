class Products(object):

    def __init__(self, price, item_name, weight, brand, status='for sale'):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.status=status

    def sell(self):
        self.status='sold'
        return self

    def add_tax(self, tax):
        self.price*=tax
        return self

    def return_item(self, reason):
        if reason=='defective':
            self.status='defective'
            self.price=0
        elif reason=='unopened':
            self.status='for sale'
        elif reason=='opened box':
            self.status='used'
            self.price*=.8
        else:
            self.status='we arnt accepting returns'
        return self

    def display_info(self):
        print ' Price: ${} \n Item name: {} \n Weight: {} \n Brand: {} \n Price: {} \n Status: {} \n'.format(self.price, self.item_name, self.weight, self.brand, self.price, self.status)



cup=Products(2, 'red solo cup', .1, 'Dixie')
cup.return_item('opened box').display_info()

cat=Products(10, 'cat', .1, 'Meow Factory')
cat.display_info()

# Nice job!!!
# -Dev
