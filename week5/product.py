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
            self.status='we arent accepting returns'
        return self
    
    
    def display_info(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.cost
        print self.status
        return self

shoes = Products(2, 'Timbs', .1, 'Timberland')
shoes.return_item('opened box').display_info()

pandashirt = Products(10, 'pandashirt', .1, 'PandaHot')
pandashirt.display_info()
