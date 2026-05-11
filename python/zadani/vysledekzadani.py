"""
Dataset: students
Povolene operatory: ['<', '>', '=']
Rozsireni: Query(data).distinct("age") - Vrátí pouze záznamy, které mají unikátní hodnotu daného pole.
Data:
"students": [
    {"name": "Anna", "age": 19, "score": 85},
    {"name": "Petr", "age": 17, "score": 60},
    {"name": "Eva", "age": 21, "score": 92},
    {"name": "Jan", "age": 18, "score": 70},
    {"name": "Lucie", "age": 20, "score": 88},
],
"""

students = [
    {"name": "Anna", "age": 19, "score": 85},
    {"name": "Petr", "age": 17, "score": 60},
    {"name": "Eva", "age": 21, "score": 92},
    {"name": "Jan", "age": 18, "score": 70},
    {"name": "Lucie", "age": 20, "score": 88}
]
class Query:
    def __init__(self, data):
        self.data = list(data)

    def filter(self, field, operator, value):
        if operator == "=":
            self.data = [item for item in self.data if item[field] == value]
        elif operator == ">":
            self.data = [item for item in self.data if item[field] > value]
        elif operator == "<":
            self.data = [item for item in self.data if item[field] < value]
        return self

    def sort_by(self, field, descending=False):
            # Seřadíme data podle klíče (field)
            self.data.sort(key=lambda x: x[field], reverse=descending)
            return self

    def limit(self, count):
        # Ořízneme seznam na požadovaný počet
        self.data = self.data[:count]
        return self

    def distinct(self, field):
        # Logika pro unikátní hodnoty
        unique_data = []
        seen_values = set()
        
        for item in self.data:
            val = item[field]
            if val not in seen_values:
                unique_data.append(item)
                seen_values.add(val)
        
        self.data = unique_data
        return self

    def execute(self):
        # Tady vracíme finální výsledek
        return self.data

print(Query(students).filter("age", ">", 17).distinct("age").sort_by("score", descending=True).limit(3).execute())