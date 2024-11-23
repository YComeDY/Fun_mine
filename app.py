from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # Новый маршрут для корневого URL
def home():
    return render_template('index.html')  # Главная страница

@app.route('/game')  # Новый маршрут для игры
def game():
    return render_template('game.html')

@app.route('/characters')  # Новый маршрут для персонажей
def characters():
    return render_template('characters.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
