# DROP TABLES
drinks_table_drop = "DROP TABLE IF EXISTS drinks"
ingredients_table_drop = "DROP TABLE IF EXISTS ingredients"
drink_ingredients_table_drop = "DROP TABLE IF EXISTS drink_ingredients"

drop_table_queries = [
    drinks_table_drop,
    ingredients_table_drop,
    drink_ingredients_table_drop,
]

# CREATE TABLES
drinks_table_create = """
                        CREATE TABLE IF NOT EXISTS drinks (
                            drink_id INTEGER NOT NULL PRIMARY KEY,
                            name TEXT,
                            instructions TEXT,
                            Instructions_de TEXT,
                            Alcoholic INTEGER
                        )
                        """

ingredients_table_create = """
                            CREATE TABLE IF NOT EXISTS ingredients (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL UNIQUE
                            )
                            """
drink_ingredients_table_create = """
                                     CREATE TABLE IF NOT EXISTS drink_ingredients (
                                        drink_id INTEGER,
                                        ingredient_id INTEGER,
                                        measure TEXT,
                                        measure_in_grams INTEGER,
                                        FOREIGN KEY (drink_id) REFERENCES drinks (drink_id),
                                        FOREIGN KEY (ingredient_id) REFERENCES ingredients (id),
                                        PRIMARY KEY (drink_id, ingredient_id)
                                    )
                                    """
create_table_queries = [
    drinks_table_create,
    ingredients_table_create,
    drink_ingredients_table_create,
]

# Insertion Queries
drinks_insertion = """
                        INSERT OR IGNORE INTO drinks (drink_id, name, instructions, Instructions_de, Alcoholic)
                        VALUES (?, ?, ?, ?, ?)
                        ON CONFLICT(drink_id) DO UPDATE SET
                            name=excluded.name,
                            instructions=excluded.instructions,
                            Instructions_de=excluded.Instructions_de,
                            Alcoholic=excluded.Alcoholic
                    """
ingredients_insertion = """
                        INSERT INTO ingredients (name) 
                        VALUES (?)
                        ON CONFLICT(name) DO NOTHING
                        """
drinks_ingredient_insertion = """
                              INSERT INTO drink_ingredients (drink_id, ingredient_id, measure, measure_in_grams)
                              VALUES (?, ?, ?, ?)
                              ON CONFLICT(drink_id, ingredient_id) DO NOTHING
                              """

# Analytical Queries
# Query 1: Which alcoholic drinks can be mixed with lemon and whiskey?
drinks_with_lemon_whiskey = """
                                SELECT DISTINCT d.name
                                    FROM drinks d
                                    INNER JOIN drink_ingredients di ON d.drink_id = di.drink_id
                                    INNER JOIN ingredients i ON di.ingredient_id = i.id
                                    WHERE (i.name LIKE '%lemon%' OR i.name LIKE '%whiskey%') AND (d.Alcoholic = 1)
                            """

# Query 2: Which drink(s) can be mixed with just 15g of Sambuca?
drinks_with_15g_sambucca = """
                                SELECT DISTINCT d.name
                                    FROM drinks d
                                    INNER JOIN drink_ingredients di ON d.drink_id = di.drink_id
                                    INNER JOIN ingredients i ON di.ingredient_id = i.id
                                    WHERE i.name LIKE '%sambuca%' AND di.measure_in_grams = 15                            
                            """

# Query 3: Which drink has the most ingredients?
drinks_with_most_ingredients = """
                                SELECT d.name, COUNT(di.ingredient_id) AS Count_Ingredients
                                    FROM drinks d
                                    INNER JOIN drink_ingredients di ON d.drink_id = di.drink_id
                                    GROUP BY d.drink_id, d.name
                                    ORDER BY COUNT(di.ingredient_id) DESC
                                    LIMIT 1                            
                            """

run_queries_list = [
    drinks_with_lemon_whiskey,
    drinks_with_15g_sambucca,
    drinks_with_most_ingredients,
]
