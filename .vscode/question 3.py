#shopping cart
items = { "apple" : "$10",
          "banana" : "$20",
          "carrot" : "$30",
          "watch"  : "$300",
          "tissue paper" : "$200",
}
itemss = { "apple" : 10,
          "banana" : 20,
          "carrot" : 30,
          "watch"  : 300,
          "tissue paper" : 200,
}
print(items)
class grocery:
    def __init__(self, item, price):
        self.name = item
        self.price = price
    while True:
        x = input("enter the item you want")
        if x == "quit":
            break
        else:
            for x in items:
                if x == "apple":
                   y1 =  int(input("enter the quantity of the apple"))
                elif x == "banana":
                    y2 = int(input("enter the quantity of the banana"))
                elif x == "carrot":
                    y3 = int(input("enter the quantity of the carrot"))
                elif x == "watch":
                    y4 = int(input("enter the quantity of the watch"))
                elif x == "tissue paper":
                    y5 = int(input("enter the quantity of the tissue paper"))
                else:
                    print("thankyou for shopping")
                    break
    total_price = (int(itemss["apple"])*y1) + (int(itemss["banana"])*y2) + (int(itemss["carrot"])*y3) + (int(itemss["watch"])*y4) + (int(itemss["tissue paper"])*y5)
    print(f"your price is {total_price}")
    print("---------THANKYOU FOR SHOPPING------------")


