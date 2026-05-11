from flask import Flask, render_template, session # Nezapomeň importovat render_template

app = Flask(__name__)
app.secret_key = 'super_tajny_klic' # Nutné pro ukládání čísla



@app.route('/')
def index():
    if 'pocitadlo' not in session:
        session['pocitadlo'] = 0
    # Tato řádka říká: "Vezmi soubor index.html ze složky templates"
    return render_template('index.html', cislo=session['pocitadlo'])

# CESTA PRO PŘIČÍTÁNÍ
@app.route('/plus_jedna', methods=['POST'])
def plus_jedna():
    session['pocitadlo'] = session.get('pocitadlo', 0) + 1
    return redirect(url_for('index'))

# NOVÁ CESTA PRO RESETOVÁNÍ
@app.route('/reset', methods=['POST'])
def reset():
    session['pocitadlo'] = 0  # Vynulujeme to
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)