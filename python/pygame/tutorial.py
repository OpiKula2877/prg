import tkinter as tk
from tkinter import ttk
import random

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Investigační systém")
        self.root.geometry("900x650")

        # === DATA: MAIly (globální seznam pro záložku Maily) ===
        self.mails = []

        # === DATA: TOtožnosti (10 osob s maily) ===
        self.persons = [
            {"jmeno": "Adam", "prijmeni": "Černý", "vek": 28, "vyska": 180, "vaha": 78, "pohlavi": "Muž", "vlasy": "Černé", "oci": "Hnědá", "mails": []},
            {"jmeno": "Barbora", "prijmeni": "Dvořáková", "vek": 34, "vyska": 168, "vaha": 62, "pohlavi": "Žena", "vlasy": "Hnědé", "oci": "Zelená", "mails": []},
            {"jmeno": "David", "prijmeni": "Horák", "vek": 45, "vyska": 175, "vaha": 90, "pohlavi": "Muž", "vlasy": "Šedivé", "oci": "Šedivá", "mails": []},
            {"jmeno": "Eva", "prijmeni": "Kovářová", "vek": 22, "vyska": 162, "vaha": 54, "pohlavi": "Žena", "vlasy": "Blond", "oci": "Modrá", "mails": []},
            {"jmeno": "Filip", "prijmeni": "Malý", "vek": 31, "vyska": 172, "vaha": 70, "pohlavi": "Muž", "vlasy": "Hnědé", "oci": "Hnědá", "mails": []},
            {"jmeno": "Gabriela", "prijmeni": "Novotná", "vek": 29, "vyska": 170, "vaha": 60, "pohlavi": "Žena", "vlasy": "Žádné", "oci": "Hnědá", "mails": []},
            {"jmeno": "Jan", "prijmeni": "Svoboda", "vek": 50, "vyska": 178, "vaha": 85, "pohlavi": "Muž", "vlasy": "Šedivé", "oci": "Modrá", "mails": []},
            {"jmeno": "Kateřina", "prijmeni": "Procházková", "vek": 26, "vyska": 165, "vaha": 58, "pohlavi": "Žena", "vlasy": "Červené", "oci": "Zelená", "mails": []},
            {"jmeno": "Lukáš", "prijmeni": "Veselý", "vek": 37, "vyska": 182, "vaha": 88, "pohlavi": "Muž", "vlasy": "Hnědé", "oci": "Hnědá", "mails": []},
            {"jmeno": "Markéta", "prijmeni": "Zemanová", "vek": 41, "vyska": 167, "vaha": 66, "pohlavi": "Žena", "vlasy": "Blond", "oci": "Šedivá", "mails": []},
        ]

        # Notebook (záložky)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)

        # Vytvoření záložek
        self.tab_mails = tk.Frame(self.notebook)
        self.tab_ident = tk.Frame(self.notebook)
        self.tab_sim = tk.Frame(self.notebook)
        self.tab_history = tk.Frame(self.notebook)

        self.notebook.add(self.tab_mails, text="Maily")
        self.notebook.add(self.tab_ident, text="Totožnosti")
        self.notebook.add(self.tab_sim, text="SIM Force")
        self.notebook.add(self.tab_history, text="Historie nákupů")

        # Naplnění záložek
        self.load_mails()
        self.load_ident_tab()
        self.load_sim_tab()
        self.add_placeholder(self.tab_history, "Zde bude historie nákupů.")

    # === MAILY ===
    def load_mails(self):
        for widget in self.tab_mails.winfo_children():
            widget.destroy()

        if not self.mails:
            tk.Label(self.tab_mails, text="Žádné maily").pack(pady=10)
            return

        canvas = tk.Canvas(self.tab_mails)
        scrollbar = ttk.Scrollbar(self.tab_mails, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for i, mail in enumerate(self.mails):
            frame = tk.Frame(scrollable_frame, relief="groove", borderwidth=1)
            frame.pack(fill="x", padx=5, pady=3)
            tk.Label(frame, text=mail["name"], width=20, anchor="w").pack(side="left", padx=5)
            tk.Button(frame, text="otevřít", command=lambda m=mail: self.open_mail(m)).pack(side="left", padx=3)
            tk.Button(frame, text="odstranit", command=lambda idx=i: self.delete_mail(idx)).pack(side="left", padx=3)
            tk.Button(frame, text="zločin", bg="red" if mail["is_suspect"] else "lightgray",
                      command=lambda idx=i: self.toggle_crime(idx)).pack(side="left", padx=3)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def open_mail(self, mail):
        top = tk.Toplevel(self.root)
        top.title(f"Zpráva od: {mail['name']}")
        top.geometry("500x400")
        text_widget = tk.Text(top, wrap="word")
        text_widget.insert("1.0", mail["text"])
        text_widget.config(state="disabled")
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)
        tk.Button(top, text="Zavřít", command=top.destroy).pack(pady=5)

    def delete_mail(self, index):
        del self.mails[index]
        self.load_mails()

    def toggle_crime(self, index):
        self.mails[index]["is_suspect"] = not self.mails[index]["is_suspect"]
        self.load_mails()

    # === TOtožnosti ===
    def load_ident_tab(self):
        search_frame = tk.LabelFrame(self.tab_ident, text="Vyhledávání", padx=10, pady=10)
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame, text="Věk:").grid(row=0, column=0, sticky="w")
        self.age_from = tk.Entry(search_frame, width=5)
        self.age_to = tk.Entry(search_frame, width=5)
        self.age_from.grid(row=0, column=1, padx=2)
        tk.Label(search_frame, text="až").grid(row=0, column=2, padx=2)
        self.age_to.grid(row=0, column=3, padx=2)
        tk.Label(search_frame, text="let").grid(row=0, column=4, padx=5)

        tk.Label(search_frame, text="Výška:").grid(row=1, column=0, sticky="w")
        self.height_from = tk.Entry(search_frame, width=5)
        self.height_to = tk.Entry(search_frame, width=5)
        self.height_from.grid(row=1, column=1, padx=2)
        tk.Label(search_frame, text="až").grid(row=1, column=2, padx=2)
        self.height_to.grid(row=1, column=3, padx=2)
        tk.Label(search_frame, text="cm").grid(row=1, column=4, padx=5)

        tk.Label(search_frame, text="Váha:").grid(row=2, column=0, sticky="w")
        self.weight_from = tk.Entry(search_frame, width=5)
        self.weight_to = tk.Entry(search_frame, width=5)
        self.weight_from.grid(row=2, column=1, padx=2)
        tk.Label(search_frame, text="až").grid(row=2, column=2, padx=2)
        self.weight_to.grid(row=2, column=3, padx=2)
        tk.Label(search_frame, text="kg").grid(row=2, column=4, padx=5)

        tk.Label(search_frame, text="Pohlaví:").grid(row=0, column=5, sticky="w", padx=(30,0))
        self.gender_var = tk.StringVar(value="Libovolné")
        gender_menu = ttk.Combobox(search_frame, textvariable=self.gender_var, state="readonly", width=10,
                                   values=["Libovolné", "Muž", "Žena"])
        gender_menu.grid(row=0, column=6, padx=2)

        tk.Label(search_frame, text="Barva vlasů:").grid(row=1, column=5, sticky="w", padx=(30,0))
        self.hair_var = tk.StringVar(value="Libovolné")
        hair_menu = ttk.Combobox(search_frame, textvariable=self.hair_var, state="readonly", width=12,
                                 values=["Libovolné", "Žádné", "Šedivé", "Hnědé", "Blond", "Červené", "Černé"])
        hair_menu.grid(row=1, column=6, padx=2)

        tk.Label(search_frame, text="Barva očí:").grid(row=2, column=5, sticky="w", padx=(30,0))
        self.eye_var = tk.StringVar(value="Libovolné")
        eye_menu = ttk.Combobox(search_frame, textvariable=self.eye_var, state="readonly", width=12,
                                values=["Libovolné", "Zelená", "Modrá", "Hnědá", "Šedivá"])
        eye_menu.grid(row=2, column=6, padx=2)

        tk.Button(search_frame, text="Hledat", command=self.filter_persons).grid(row=3, column=6, pady=10, sticky="e")

        self.results_frame = tk.Frame(self.tab_ident)
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.display_persons(self.persons)

    def display_persons(self, persons):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if not persons:
            tk.Label(self.results_frame, text="Žádné osoby nesplňují kritéria.", fg="gray").pack()
            return

        headers = ["Jméno a příjmení", "Věk", "Výška (cm)", "Váha (kg)", "Pohlaví", "Vlasy", "Oči"]
        for i, h in enumerate(headers):
            width = 18 if i == 0 else 8
            tk.Label(self.results_frame, text=h, font=("Arial", 10, "bold"), relief="sunken", width=width).grid(row=0, column=i, padx=1, pady=2)

        for r, p in enumerate(persons, start=1):
            tk.Label(self.results_frame, text=f"{p['jmeno']} {p['prijmeni']}", width=18, anchor="w").grid(row=r, column=0, padx=1, pady=1)
            tk.Label(self.results_frame, text=p["vek"], width=8).grid(row=r, column=1, padx=1, pady=1)
            tk.Label(self.results_frame, text=p["vyska"], width=8).grid(row=r, column=2, padx=1, pady=1)
            tk.Label(self.results_frame, text=p["vaha"], width=8).grid(row=r, column=3, padx=1, pady=1)
            tk.Label(self.results_frame, text=p["pohlavi"], width=8).grid(row=r, column=4, padx=1, pady=1)
            tk.Label(self.results_frame, text=p["vlasy"], width=10).grid(row=r, column=5, padx=1, pady=1)
            tk.Label(self.results_frame, text=p["oci"], width=10).grid(row=r, column=6, padx=1, pady=1)

    def filter_persons(self):
        def safe_int(val):
            try:
                return int(val) if val.strip() != "" else None
            except ValueError:
                return None

        age_min = safe_int(self.age_from.get())
        age_max = safe_int(self.age_to.get())
        h_min = safe_int(self.height_from.get())
        h_max = safe_int(self.height_to.get())
        w_min = safe_int(self.weight_from.get())
        w_max = safe_int(self.weight_to.get())

        gender = self.gender_var.get()
        hair = self.hair_var.get()
        eye = self.eye_var.get()

        filtered = []
        for p in self.persons:
            if age_min is not None and p["vek"] < age_min: continue
            if age_max is not None and p["vek"] > age_max: continue
            if h_min is not None and p["vyska"] < h_min: continue
            if h_max is not None and p["vyska"] > h_max: continue
            if w_min is not None and p["vaha"] < w_min: continue
            if w_max is not None and p["vaha"] > w_max: continue
            if gender != "Libovolné" and p["pohlavi"] != gender: continue
            if hair != "Libovolné" and p["vlasy"] != hair: continue
            if eye != "Libovolné" and p["oci"] != eye: continue
            filtered.append(p)

        self.display_persons(filtered)

    # === SIM Force ===
    def load_sim_tab(self):
        for widget in self.tab_sim.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.tab_sim, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Zadej jméno a příjmení osoby:", font=("Arial", 11)).pack(pady=5)
        self.sim_entry = tk.Entry(frame, width=30, font=("Arial", 12))
        self.sim_entry.pack(pady=5)
        tk.Button(frame, text="Spustit SIM Force", command=self.start_sim_force).pack(pady=10)

        self.sim_status = tk.Label(frame, text="", fg="red", font=("Arial", 10))
        self.sim_status.pack()

    def start_sim_force(self):
        name_input = self.sim_entry.get().strip()
        if not name_input:
            self.sim_status.config(text="Zadej jméno a příjmení!", fg="red")
            return

        target_person = None
        for p in self.persons:
            if f"{p['jmeno']} {p['prijmeni']}".lower() == name_input.lower():
                target_person = p
                break

        if not target_person:
            self.sim_status.config(text="Jméno není v seznamu nebo nemá SIM kartu.", fg="red")
            return

        self.sim_status.config(text="")
        self.run_sim_game(target_person)

    def run_sim_game(self, person):
        for widget in self.tab_sim.winfo_children():
            widget.destroy()

        self.sim_game_frame = tk.Frame(self.tab_sim, padx=20, pady=20)
        self.sim_game_frame.pack(fill="both", expand=True)

        tk.Label(self.sim_game_frame, text=f"SIM Force: {person['jmeno']} {person['prijmeni']}", font=("Arial", 14, "bold")).pack(pady=10)

        self.sim_time_left = 15
        self.sim_timer_label = tk.Label(self.sim_game_frame, text=f"Čas: {self.sim_time_left}s", font=("Arial", 12))
        self.sim_timer_label.pack()

        self.sim_target = random.randint(1, 50)

        tk.Label(self.sim_game_frame, text="Nastav frekvenci (1–50):").pack(pady=(10,5))
        self.sim_scale_var = tk.IntVar(value=25)
        self.sim_scale = tk.Scale(self.sim_game_frame, from_=1, to=50, orient="horizontal", variable=self.sim_scale_var, length=400)
        self.sim_scale.pack()

        # Barevná tečka – červená na začátku
        self.sim_indicator_dot = tk.Label(self.sim_game_frame, bg="red", width=4, height=2, relief="flat")
        self.sim_indicator_dot.pack(pady=10)

        self.sim_access_btn = tk.Button(self.sim_game_frame, text="Přístup k mailům", state="disabled",
                                        command=lambda: self.grant_mail_access(person))
        self.sim_access_btn.pack(pady=10)

        self.sim_update_check()
        self.sim_countdown(person)

    def sim_update_check(self):
        current = self.sim_scale_var.get()
        if current == self.sim_target:
            self.sim_indicator_dot.config(bg="green")
            self.sim_access_btn.config(state="normal")
        else:
            self.sim_indicator_dot.config(bg="red")
            self.sim_access_btn.config(state="disabled")
        self.sim_check_job = self.root.after(200, self.sim_update_check)

    def sim_countdown(self, person):
        if self.sim_time_left > 0:
            self.sim_time_left -= 1
            self.sim_timer_label.config(text=f"Čas: {self.sim_time_left}s")
            self.sim_timer_job = self.root.after(1000, lambda: self.sim_countdown(person))
        else:
            self.sim_indicator_dot.config(bg="red")
            self.sim_access_btn.config(state="disabled")
            if hasattr(self, 'sim_check_job'):
                self.root.after_cancel(self.sim_check_job)

    def grant_mail_access(self, person):
        if hasattr(self, 'sim_timer_job'):
            self.root.after_cancel(self.sim_timer_job)
        if hasattr(self, 'sim_check_job'):
            self.root.after_cancel(self.sim_check_job)

        self.notebook.select(self.tab_mails)
        self.mails = person["mails"] if person["mails"] else [
            {"name": f"{person['jmeno']} {person['prijmeni']}", "text": "[Žádné zprávy]", "is_suspect": False}
        ]
        self.load_mails()

    # === Pomocné metody ===
    def add_placeholder(self, parent, text):
        tk.Label(parent, text=text, fg="gray", font=("Arial", 11)).pack(pady=20)


# === SPUŠTĚNÍ ===
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()