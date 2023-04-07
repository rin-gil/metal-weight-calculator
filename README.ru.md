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
    <a href="https://github.com/rin-gil/MetalWeightCalculator/blob/master/README.ua.md">
        <img src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/icons/flags/ukraine_24x24.png" alt="Ua">
    </a>
</p>

## Калькулятор веса металла

Приложение выполняет расчет теоретического веса металлопроката, по данным введенным пользователем. Доступен выбор различных видов металлопроката, металлов и металлических сплавов.
Опробовать приложение в работе можно на сайте [https://metal-calc.my.to](https://metal-calc.my.to)

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
* Приложение доступно в браузере по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Скриншоты

<p align="center">
    <img src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/projects/MetalWeightCalculator/screenshot_ru.png" alt="Главный экран MetalWeightCalculator">
</p>

### Разработчики

* [Ringil](https://github.com/rin-gil)

### Лицензия

Проект Калькулятор веса металла распространяется по лицензии [MIT](https://github.com/rin-gil/MetalWeightCalculator/blob/master/LICENCE)
