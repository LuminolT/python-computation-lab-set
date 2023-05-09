# FoodOrder.py

class Customer:
    def __init__(self) -> None:
        self.name = ''
        self.order = []     

    def placeOrder(self, empolyee, customername):
        self.order = []
        self.name = customername
        self.order.append(empolyee.name)
        while True:
            food = empolyee.takeOrder()
            if not food:
                break
            elif food == 1:
                continue
            else:
                self.order.append(food)
        return self.order
    

class Employee:
    def __init__(self, name, foodlist) -> None:
        self.name = name
        self.menu = foodlist   

    def showMenu(self):
        print(f"{'|'}{'Employee name: ':<20}{self.name:>20}{'|'}")
        print(f"{'|'}{'-'*40}{'|'}")
        print(f"{'|'}{'Number':<10}{'Food':<20}{'price/$':>10}{'|'}")
        print(f"{'|'}{'-'*40}{'|'}")
        for food in self.menu:
            print(f"{'|'}{self.menu.index(food)+1:<10}{food.name:<20}{food.price:>10}{'|'}")

    def takeOrder(self):
        foodnum = input("Please input the food number(0 for exit): ")
        foodnum = int(foodnum)
        if foodnum == 0:
            return 0
        elif foodnum-1 >= len(self.menu):
            print("No this food!")
            return 1
        else:
            return self.menu[foodnum - 1]


class Food:
    def __init__(self, f, p) -> None:
        self.name = f
        self.price = p
    
    def __str__(self) -> str:
        return f"{'|'}{self.name:<20}{self.price:>20}{'|'}"


class Lunch:
    def __init__(self, empolyee, customer) -> None:
        self.empolyee = empolyee
        self.customer = customer
        self.orderForm = []

    def order(self):
        print("Menu of employees as follow: ")
        print('+' + '-'*40 + '+')
        print(f"{'|'}{'Menu'.center(40)}{'|'}")
        print(f"{'|'}{'-'*40}{'|'}")
        for emp in self.empolyee:
            emp.showMenu()
            print('+' + '-'*40 + '+')
        customername = input("Please input your name: ")
        while True:
            empnum = input("Please input the empolyee number(0 for exit): ")
            empnum = int(empnum)
            orderform = []
            if empnum == 0:
                break
            elif empnum-1 >= len(self.empolyee):
                print("No this employee!")
                continue
            else:
                orderform = self.customer.placeOrder(self.empolyee[empnum - 1], customername)
                self.orderForm.append(orderform)
        
    def result(self):
        print("Your order form is following: ")
        print('+' + '-'*40 + '+')
        print(f"{'|'}{'Customer name: ':<20}{self.customer.name:>20}{'|'}")
        print(f"{'|'}{'-'*40}{'|'}")
        print(f"{'|'}{'Food':<20}{'price/$':>20}{'|'}")
        print(f"{'|'}{'-'*40}{'|'}")
        sum = 0
        for orderitem in self.orderForm:
            for item in orderitem[1:]:
                print(item)
                sum += item.price
        print(f"{'|'}{'-'*40}{'|'}")
        print(f"{'|'}{'Total':<20}{sum:>20}{'|'}")
        print('+' + '-'*40 + '+')
            

def initial():
    foodlist1 = [Food('pizza', 10), Food('hamburger', 11), Food('chip', 12)]
    foodlist2 = [Food('apple', 10), Food('banana', 11), Food('peach', 12)]
    e1 = Employee('McDonald', foodlist1)
    e2 = Employee('Fruits', foodlist2)
    e = []
    e.append(e1)
    e.append(e2)
    return e
    
def main():
    print("Welcome to Food Order System!")
    emplist = initial()
    c1 = Customer()
    lunch = Lunch(emplist, c1)
    lunch.order()
    lunch.result()


if __name__ == "__main__":
    main()