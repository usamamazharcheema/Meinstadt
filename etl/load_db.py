import sqlite3
from typing import List

import pysqlite3 as sqlite3

import etl
import sql_queries


def insertion(cursor: sqlite3.Cursor, drinks: List[dict]):
    """
    Insert drinks, ingredients, and drink-ingredients data into the database.

    :param cursor: SQLite cursor
    :param drinks: List of drink dictionaries
    :return: None
    """
    drinks_data = []
    ingredients_data = []
    drink_ingredients_data = []

    for drink in drinks:
        drink_id = int(drink["idDrink"])
        name = drink["strDrink"]
        instructions = drink.get("strInstructions", "")
        instructions_de = drink.get("strInstructionsDE", "")
        alcoholic = int(drink.get("strAlcoholic", "") == "Alcoholic")

        if instructions_de is not None:
            drinks_data.append(
                (drink_id, name, instructions, instructions_de, alcoholic)
            )

            for i in range(1, 16):
                ingredient_index = f"strIngredient{i}"
                measure_index = f"strMeasure{i}"
                if (
                    ingredient_index in drink
                    and measure_index in drink
                    and drink[ingredient_index] is not None
                ):
                    ingredient_name = drink[ingredient_index]
                    measure_name = drink[measure_index]
                    measure_in_grams = (
                        etl.measure_conversion.convert_measure_to_grams(measure_name)
                        if measure_name is not None
                        else measure_name
                    )

                    ingredients_data.append((ingredient_name,))
                    drink_ingredients_data.append(
                        (drink_id, ingredient_name, measure_name, measure_in_grams)
                    )

    cursor.executemany(sql_queries.drinks_insertion, drinks_data)
    cursor.executemany(sql_queries.ingredients_insertion, ingredients_data)

    cursor.execute("SELECT id, name FROM ingredients")
    existing_ingredients = dict(cursor.fetchall())
    existing_ingredients = {v: k for k, v in existing_ingredients.items()}

    drink_ingredients_data = [
        (data[0], existing_ingredients[data[1]], data[2], data[3])
        for data in drink_ingredients_data
    ]

    cursor.executemany(sql_queries.drinks_ingredient_insertion, drink_ingredients_data)
