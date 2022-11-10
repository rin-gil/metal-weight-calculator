<p align="center">
    <img src="https://repository-images.githubusercontent.com/558666840/d53084b5-8a5e-4b62-8263-a4b32fde99ff" alt="Калькулятор веса металла" width="640">
</p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3110/"><img src="https://img.shields.io/badge/python-v3.11-informational" alt="python version"></a>
    <a href="https://pypi.org/project/Django/3.2.15/"><img src="https://img.shields.io/badge/Django-v3.2.15-informational" alt="Django version"></a>
    <a href="https://pypi.org/project/environs/9.5.0/"><img src="https://img.shields.io/badge/environs-v9.5.0-informational" alt="environs version"></a>
    <a href="https://pypi.org/project/gunicorn/20.1.0/"><img src="https://img.shields.io/badge/gunicorn-v20.1.0-informational" alt="gunicorn version"></a>
    <a href="https://github.com/rin-gil/MetalWeightCalculator/blob/master/LICENCE"><img src="https://img.shields.io/badge/licence-MIT-success" alt="MIT licence"></a>
</p>

<p align="right">
    <a href="https://github.com/rin-gil/MetalWeightCalculator/blob/master/README.ru.md">Читать на русском</a>
</p>

## Metal Weight Calculator

The application calculates the theoretical weight of rolled steel, based on the data entered by the user.
A selection of different types of rolled metal products, metals and metal alloys is available.
To try out the application, visit [metal-calc.mooo.com](https://metal-calc.mooo.com)

### Installing

```
git clone https://github.com/rin-gil/MetalWeightCalculator.git
cd MetalWeightCalculator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mv .env.dist .env
```

### Setup and launch

* Run the application with the command `python3 manage.py runserver`
* The application is now available in the browser at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Screenshots

<p align="center">
    <img src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/projects/MetalWeightCalculator/screenshot.png" alt="Главный экран приложения">
</p>

### Developers

* [Ringil](https://github.com/rin-gil)

### License

Metal Weight Calculator is licensed under [MIT](https://github.com/rin-gil/MetalWeightCalculator/blob/master/LICENCE)
