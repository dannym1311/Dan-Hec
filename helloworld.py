#animals = ["dog", "cat", "bird"]
#print(animals[1])


food = {"Beef": 12.99, "cheese": 5.99, "milk": 4.99}
#print(food["milk"])


def meal (items: dict[str, float]):
    for (item, price) in items.items():
        items[item] *= 2
    print(items)

meal(food)
meal({"cat": 25})









