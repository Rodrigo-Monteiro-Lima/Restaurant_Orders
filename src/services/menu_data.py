import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        if not source_path:
            raise ValueError("source_path is required")
        self.source_path = source_path
        self.dishes = self.load_menu_data()

    def load_menu_data(self) -> set:
        plates = {}
        with open(self.source_path, "r", encoding="utf-8") as file:
            menu_data = csv.reader(file, delimiter=",", quotechar='"')
            next(menu_data)
            for row in menu_data:
                dish_name = row[0]
                price = float(row[1])
                ingredient = row[2]
                amount = int(row[3])
                if dish_name not in plates:
                    plates[dish_name] = Dish(dish_name, price)
                plates[dish_name].add_ingredient_dependency(
                    Ingredient(ingredient), amount
                )
        return set(plates.values())


if __name__ == "__main__":
    menu = MenuData("data/menu_base_data.csv")
    print(menu.dishes)
