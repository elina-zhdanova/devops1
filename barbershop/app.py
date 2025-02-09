from flask import Flask, render_template

app = Flask(__name__)

# Услуги парикмахерской
services = [
    {
        'name': 'Стрижка',
        'price': 'от 400 до 2000 руб.',
        'images': ['images/haircut.jpg', 'images/haircut_man.jpg'],  # Используем 'images' вместо 'image'
        'description': 'Качественная стрижка любой сложности.'
    },
    {
        'name': 'Бритье',
        'price': '500 руб.',
        'images': ['images/shave.jpg'],  # Сделаем 'images' список
        'description': 'Профессиональное бритье с использованием качественных средств.'
    },
    {
        'name': 'Укладка',
        'price': '1000 руб.',
        'images': ['images/styling.jpg'],  # Сделаем 'images' список
        'description': 'Стильная укладка для любого случая.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
