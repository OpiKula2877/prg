from pathlib import Path

# 1. Kde je tento skript
SCRIPT_DIR = Path(__file__).parent.resolve()
print("📁 Složka tohoto skriptu:", SCRIPT_DIR)

# 2. Kde hledáš teď (aktuální cwd)
print("⚙️ Aktuální pracovní adresář:", Path.cwd())

# 3. Hledej bubilum.png v okolí
print("\n🔍 Hledám 'bubilum.png' v okolí...")

# Možné lokality:
candidates = [
    SCRIPT_DIR / "bubilum.png",
    SCRIPT_DIR.parent / "bubilum.png",
    SCRIPT_DIR.parent.parent / "bubilum.png",
    Path.cwd() / "bubilum.png",
]

for cand in candidates:
    exists = cand.is_file()
    size = cand.stat().st_size if exists else "—"
    print(f" • {cand} → {'✅' if exists else '❌'} ({size} B)")

# 4. Vypiš VŠECHNY .png soubory v okolí (max 2 úrovně)
print("\n🖼️ Všechny .png soubory v okolí (max 2 úrovně níž):")
for p in SCRIPT_DIR.parent.parent.rglob("*.png"):
    if "venv" not in p.parts and "__pycache__" not in p.parts:
        print(f"   - {p.relative_to(SCRIPT_DIR.parent.parent)} ({p.stat().st_size} B)")