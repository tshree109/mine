import abc

class ItemElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self):
        pass

class ShoppingCartVisitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit(self, item):
        pass

class Coupon(ItemElement):
    def __init__(self, cost, id):
        self.price = cost
        self.id = id

    def get_price(self):
        return self.price

    def get_id(self):
        return self.id

    def accept(self, visitor):
        return visitor.visit(self)


class Meal(ItemElement):
    def __init__(self, price, wt, nm):
        self.price = price
        self.weight = wt
        self.name = nm

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name

    def accept(self, visitor):
        return visitor.visit(self)

class ShoppingCartVisitorImpl(ShoppingCartVisitor):
    def visit(self, item):
        if isinstance(item, Coupon):
            cost = 0
            #apply 2 euros discount if coupon price is greater than 20
            if item.get_price() > 20:
                cost = item.get_price() - 5
            else:
                cost = item.get_price()
            print("Coupon:: {} cost = {}".format(item.get_id(), cost))
            return cost
        elif isinstance(item, Meal):
            cost = item.get_price() * item.get_weight()
            print("{} cost = {}".format(item.get_name(), cost))
            return cost

def calculate_price(items):
    visitor = ShoppingCartVisitorImpl()
    sum = 0
    for item in items:
        sum = sum + item.accept(visitor)

    return sum

