def assign_variant(surname):
    seed = sum(ord(c) for c in surname.lower())

    datasets = {
        "students": [
            {"name": "Anna", "age": 19, "score": 85},
            {"name": "Petr", "age": 17, "score": 60},
            {"name": "Eva", "age": 21, "score": 92},
            {"name": "Jan", "age": 18, "score": 70},
            {"name": "Lucie", "age": 20, "score": 88},
        ],
        "products": [
            {"name": "Notebook", "price": 15000, "rating": 4.5},
            {"name": "Mouse", "price": 500, "rating": 4.0},
            {"name": "Keyboard", "price": 1200, "rating": 4.2},
            {"name": "Monitor", "price": 8000, "rating": 4.3},
            {"name": "Printer", "price": 3000, "rating": 3.8},
        ],
        "cars": [
            {"model": "Skoda", "speed": 180, "year": 2018},
            {"model": "BMW", "speed": 240, "year": 2020},
            {"model": "Audi", "speed": 220, "year": 2019},
            {"model": "Mercedes", "speed": 250, "year": 2021},
            {"model": "Volkswagen", "speed": 200, "year": 2017},
        ]
    }

    dataset_keys = list(datasets.keys())
    dataset = dataset_keys[seed % 3]

    operators = [["<", ">", "="], [">=", "<=", "!="]]
    ops = operators[seed % 2]

    extras = ["Query(data).distinct(\"age\") - Vrátí pouze záznamy, které mají unikátní hodnotu daného pole.",
              "Query(data).sort_by(\"age\").count() - Vrátí počet záznamů v v aktuálním výsledku.",
              "Query(data).sort_by(\"age\").first() - Vrátí první záznam z aktuálního výsledku."]
    extra = extras[seed % 3]

    return {
        "dataset_name": dataset,
        "data": datasets[dataset],
        "operators": ops,
        "extra_method": extra
    }


if __name__ == "__main__":
    surname = input("Zadej prijmeni (bez diakritiky): ")
    result = assign_variant(surname)

    print("\n--- TVOJE ZADANI ---")
    print("Dataset:", result["dataset_name"])
    print("Povolene operatory:", result["operators"])
    print("Rozsireni:", result["extra_method"])
    print("Data:")
    for row in result["data"]:
        print(row)
