<p align="center">
    <img src="https://repository-images.githubusercontent.com/558666840/d53084b5-8a5e-4b62-8263-a4b32fde99ff" alt="MetalWeightCalculator" width="640">
</p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3110/">
        <img src="https://img.shields.io/badge/python-v3.11-informational" alt="python version">
    </a>
    <a href="https://pypi.org/project/Django/4.2/">
        <img src="https://img.shields.io/badge/Django-v4.2-informational" alt="Django version">
    </a>
    <a href="https://pypi.org/project/django-modeltranslation/0.18.9/">
        <img src="https://img.shields.io/badge/django_modeltranslation-v0.18.9-informational" alt="gunicorn version">
    </a>
    <a href="https://pypi.org/project/environs/9.5.0/">
        <img src="https://img.shields.io/badge/environs-v9.5.0-informational" alt="environs version">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg">
    </a>
    <a href="https://github.com/rin-gil/MetalWeightCalculator/actions/workflows/tests.yml">
        <img src="https://github.com/rin-gil/MetalWeightCalculator/actions/workflows/tests.yml/badge.svg" alt="Code tests">
    </a>
    <a href="https://github.com/rin-gil/MetalWeightCalculator/actions/workflows/codeql.yml">
        <img src="https://github.com/rin-gil/MetalWeightCalculator/actions/workflows/codeql.yml/badge.svg" alt="Code tests">
    </a>
    <a href="https://github.com/rin-gil/MetalWeightCalculator/blob/master/LICENCE">
        <img src="https://img.shields.io/badge/licence-MIT-success" alt="MIT licence">
    </a>
</p>

<p align="right">
    <a href="https://github.com/rin-gil/MetalWeightCalculator/blob/master/README.md">
        <img src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/icons/flags/united-kingdom_24x24.png" alt="En"></a>
    <a href="https://github.com/rin-gil/MetalWeightCalculator/blob/master/README.ru.md">
        <img src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/icons/flags/russia_24x24.png" alt="Ru">
    </a>
</p>

## Калькулятор ваги металу

Додаток виконує розрахунок теоретичної ваги металопрокату, за даними введеними користувачем. Доступний вибір різних видів металопрокату, металів і металевих сплавів.
Випробувати додаток у роботі можна на сайті [https://metal-calc.my.to](https://metal-calc.my.to)

### Встановлення

```
git clone https://github.com/rin-gil/MetalWeightCalculator.git
cd MetalWeightCalculator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mv .env.dist .env
```

### Налаштування та запуск

* Запустіть додаток командою `python3 manage.py runserver`
* Додаток доступний у браузері за адресою: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Скриншоти

<p align="center">
    <img src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/projects/MetalWeightCalculator/screenshot_ua.png" alt="Головний екран MetalWeightCalculator">
</p>

### Розробники

* [Ringil](https://github.com/rin-gil)

### Ліцензія

Проєкт Калькулятор ваги металу поширюється за ліцензією [MIT](https://github.com/rin-gil/MetalWeightCalculator/blob/master/LICENCE)
