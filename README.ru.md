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
    <a href="https://github.com/rin-gil/MetalWeightCalculator/blob/master/README.md">Read English</a>
</p>

## Калькулятор веса металла

Приложение выполняет расчет теоретического веса металлопроката, по данным, которые ввел пользователь.
Доступен выбор различных видов металлопроката, металлов и металлических сплавов.
Опробовать приложение в работе можно на сайте [metal-calc.mooo.com](https://metal-calc.mooo.com)

### Установка

```
git clone https://github.com/rin-gil/MetalWeightCalculator.git
cd MetalWeightCalculator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mv .env.dist .env
```

### Настройка и запуск

* Запустите приложение командой `python3 manage.py runserver`
* Теперь приложение доступно в браузере по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Скриншоты

<p align="center">
    <img src="https://raw.githubusercontent.com/rin-gil/MetalWeightCalculator/master/metalCalc/static/img/home_page.png" alt="Главный экран приложения">
</p>

### Разработчики

* [Ringil](https://github.com/rin-gil)

### License

Проект Калькулятор веса металла распространяется по лицензии [MIT](https://github.com/rin-gil/MetalWeightCalculator/blob/master/LICENCE)
