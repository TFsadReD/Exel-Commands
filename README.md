<div align="center">
<h1>Exel Commands<br>🔢 Утилиты для работы с коллекциями</h1>

![Python](https://img.shields.io/badge/Python-3.13+-blue)
</div>

> *To read in English, scroll down*

Этот репозиторий содержит набор полезных функций для работы с коллекциями чисел и смешанных данных в Python.
Функции помогают преобразовывать данные, суммировать, усреднять и фильтровать их по заданным условиям.
Идея для этого проекта была взята из `Exel` и команд существующих там

---

## 📂 Содержание

- Возможности
- Установка
- Использование
  - type_query
  - to_number
  - flatten
  - summ_coll
  - average_coll
  - count_if
  - summ_if
  - average_if
  - if_error
- Примеры
- Лицензия

---

## ✨ Возможности

- 🔍 Определение типа переменной
- 🔄 Преобразование строк, чисел и булевых значений в числа.
- 📚 *«Выпрямление»* вложенных коллекций (`list`, `tuple`, `set`)
- ➕ Суммирование элементов с обработкой разных типов
- ⚖️ Вычисление среднего значения коллекций
- ✅ Подсчёт и суммирование элементов по условиям (`str`, `lambda`, `bool`)
- 🎯 Гибкое округление результата
- 🧱 И многое другое

---

## ⚙️ Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/TFsadReD/Exel-Commands.git
```

---

## 🛠 Использование

### `type_query(variable)`

Возвращает строку с типом переменной:

```python
type_query(10)        # 'int'
type_query("hello")   # 'str'
```

---

### `to_number(variable)`

Преобразует переменную к числу *(если возможно)*:

```python
to_number("42")     # 42
to_number("3.14")   # 3.14
to_number(True)     # 1
to_number("false")  # 0
```

---

### `flatten(variable)`

Разворачивает вложенные коллекции в одномерный список:

```python
flatten([1, [2, 3], (4, {5, 6})])
# [1, 2, 3, 4, 5, 6]
```

---

### `summ_coll(*args)`

Суммирует все элементы коллекций:

```python
summ_coll([1, 2], (3, 4))
# 10
```

---

### `average_coll(*args, around=None)`

Вычисляет среднее значение элементов:

```python
average_coll([1, 2, 3, 4])            # 2.5
average_coll([1, 2, 3, 4], around=2)  # 2.50
```

---

### `count_if(*args, condition=">0")`

Считает количество элементов, удовлетворяющих условию:

```python
count_if([-2, -1, 0, 1, 2], condition=">0")
# 2

count_if([1, 2, 3], condition=lambda x: x % 2 == 1)
# 2
```

---

### `summ_if(*args, condition=">0")`

Суммирует элементы по условию:

```python
summ_if([-2, -1, 0, 1, 2], condition=">0")
# 3
```

---

### `average_if(*args, condition=">0", around=None)`

Среднее значение элементов по условию:

```python
average_if([-2, -1, 0, 1, 2], condition=">0")
# 1.5
```

---

### `if_error(condition, error=None, returning=None)`

Проверяет выражение на выполнимость, при ошибке выдавая значение, указанное вами:

```python
a = "10"
b = "1f"
с = if_error(f"int({a})", "No")
print(c)
# 10
print(if_error(f"int({b})", b))
# 1f
```

---

## 📊 Примеры

```python
data = [1, "2", [3, "true", "false"], (4, 5.5)]

print(summ_coll(data))                                # 16.5
print(average_coll(data, around=1))                   # 3.3
print(count_if(data, condition=">=2"))                # 4
print(summ_if(data, condition=lambda x: x % 2 == 1))  # 9
print(average_if(data, condition=True))               # 2.75
```

---

## ⚖ Лицензия

Этот проект распространяется под лицензией **[Apache-2.0 license](https://github.com/TFsadReD/Exel-Commands#Apache-2.0-1-ov-file)**

---

## 🏆 Автор:

- **TFsadReD**

<br><br>

<br><br>

<div align="center">
<h1>Exel Commands<br>🔢 Utilities for Working with Collections</h1>

![Python](https://img.shields.io/badge/Python-3.13+-blue)

</div>

This repository contains a set of useful functions for working with collections of numbers and mixed data in Python.
The functions help transform data, sum, average, and filter them based on given conditions.
The idea for this project was inspired by `Excel` and its built-in commands.

---

## 📂 Contents

- Features
- Installation
- Usage
  - type_query
  - to_number
  - flatten
  - summ_coll
  - average_coll
  - count_if
  - summ_if
  - average_if
  - if_error
- Examples
- License

---

## ✨ Features

* 🔍 Detect the type of a variable
* 🔄 Convert strings, numbers, and booleans into numbers
* 📚 *Flatten* nested collections (`list`, `tuple`, `set`)
* ➕ Sum elements while handling different types
* ⚖️ Calculate averages of collections
* ✅ Count and sum elements by condition (`str`, `lambda`, `bool`)
* 🎯 Flexible rounding of results
* 🧱 And much more

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/TFsadReD/Exel-Commands.git
```

---

## 🛠 Usage

### `type_query(variable)`

Returns a string with the type of a variable:

```python
type_query(10)        # 'int'
type_query("hello")   # 'str'
```

---

### `to_number(variable)`

Converts a variable to a number *(if possible)*:

```python
to_number("42")     # 42
to_number("3.14")   # 3.14
to_number(True)     # 1
to_number("false")  # 0
```

---

### `flatten(variable)`

Flattens nested collections into a one-dimensional list:

```python
flatten([1, [2, 3], (4, {5, 6})])
# [1, 2, 3, 4, 5, 6]
```

---

### `summ_coll(*args)`

Sums all elements in collections:

```python
summ_coll([1, 2], (3, 4))
# 10
```

---

### `average_coll(*args, around=None)`

Calculates the average value of elements:

```python
average_coll([1, 2, 3, 4])            # 2.5
average_coll([1, 2, 3, 4], around=2)  # 2.50
```

---

### `count_if(*args, condition=">0")`

Counts the number of elements satisfying a condition:

```python
count_if([-2, -1, 0, 1, 2], condition=">0")
# 2

count_if([1, 2, 3], condition=lambda x: x % 2 == 1)
# 2
```

---

### `summ_if(*args, condition=">0")`

Sums elements by condition:

```python
summ_if([-2, -1, 0, 1, 2], condition=">0")
# 3
```

---

### `average_if(*args, condition=">0", around=None)`

Calculates the average value of elements by condition:

```python
average_if([-2, -1, 0, 1, 2], condition=">0")
# 1.5
```

---

### `if_error(condition, error=None, returning=None)`

Checks the expression for feasibility, returning the value you specified in case of an error:

```python
a = "10"
b = "1f"
с = if_error(f"int({a})", "No")
print(c)
# 10
print(if_error(f"int({b})", b))
# 1f
```

---

## 📊 Examples

```python
data = [1, "2", [3, "true", "false"], (4, 5.5)]

print(summ_coll(data))                                # 16.5
print(average_coll(data, around=1))                   # 3.3
print(count_if(data, condition=">=2"))                # 4
print(summ_if(data, condition=lambda x: x % 2 == 1))  # 9
print(average_if(data, condition=True))               # 2.75
```

---

## ⚖ License

This project is distributed under the **[Apache-2.0 license](https://github.com/TFsadReD/Exel-Commands#Apache-2.0-1-ov-file)**

---

## 🏆 Author

* **TFsadReD**
