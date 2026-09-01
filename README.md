# My First Autotests

Учебный проект по автоматизации тестирования на Python + pytest.

## Установка

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать виртуальное окружение:

```bash
.venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Запустить тесты:

```bash
pytest
```

## First test

The project contains a simple pytest test:

```python
def test_addition():
    assert 2 + 2 == 4
```