class Query:
    def __init__(self, data):
        # Vytvoříme si kopii dat, abychom neměnili původní seznam
        self.data = list(data)

    def filter_by(self, field, value):
        # Vyfiltrujeme data pomocí list comprehension
        self.data = [item for item in self.data if item.get(field) == value]
        return self  # Zde je to kouzlo: vracíme objekt samotný

    def sort_by(self, field):
        # Seřadíme data podle zadaného klíče
        self.data.sort(key=lambda q: q.get(field))
        return self  # Opět vracíme self pro další řetězení

    def limit(self, n):
        # Ořízneme seznam na n prvků
        self.data = self.data[:n]
        return self

    def execute(self):
        # Finální metoda, která už nevrací self, ale výsledek
        return self.data

# --- TESTOVÁNÍ ---
data = [
    {"name": "Alice", "age": 20}, {"name": "Bob", "age": 17},
    {"name": "Emily", "age": 18}, {"name": "John", "age": 21},
    {"name": "Jack", "age": 22}, {"name": "Kevin", "age": 18},
    {"name": "Annie", "age": 20}, {"name": "Charlotte", "age": 17},
    {"name": "Wanda", "age": 18}, {"name": "Adam", "age": 16},
    {"name": "Fiona", "age": 17}, {"name": "Charlie", "age": 18}
]

# Použití fluent API
result = (
    Query(data)
    .filter_by("age", 18)
    .sort_by("name")
    .limit(2)
    .execute()
)

print(result)