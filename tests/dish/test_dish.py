from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish("Medalhão", 10.0)
    assert dish.name == "Medalhão"
    assert dish.price == 10.0
    assert dish.recipe == {}
    assert repr(dish) == "Dish('Medalhão', R$10.00)"
    assert hash(dish) == hash("Dish('Medalhão', R$10.00)")
    assert dish == Dish("Medalhão", 10.0)
    assert dish != Dish("farinha", 5.0)
    bacon = Ingredient("bacon")
    chicken = Ingredient("frango")
    dish.add_ingredient_dependency(bacon, 1)
    dish.add_ingredient_dependency(chicken, 1)
    assert dish.recipe == {bacon: 1, chicken: 1}
    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
    assert dish.get_ingredients() == {bacon, chicken}
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Lasanha", -30)
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Lasanha", complex(1, 2))
