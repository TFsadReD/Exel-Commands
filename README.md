# 🔢 Utils for Working with Collections in Python

Этот репозиторий содержит набор полезных функций для работы с коллекциями чисел и смешанных данных в Python.
Функции помогают преобразовывать данные, суммировать, усреднять и фильтровать их по заданным условиям.
Идея для этого проекта была взята из `Exel` и команд существующих там

---

## 📂 Содержание

- [Возможности](#возможности)
- [Установка](#установка)
- [Использование](#использование)
  - [type_query](#type_query(variable))
  - [to_number](#to_number(variable))
  - [flatten](#flatten(variable))
  - [summ_coll](#summ_coll(*args))
  - [average_coll](#average_coll(*args,around=None))
  - [count_if](#count_if(*args,condition=">0"))
  - [summ_if](#summ_if(*args,condition=">0"))
  - [average_if](#average_if(*args,condition=">0",around=None))
- [Примеры](#Примеры)
- [Лицензия](#лицензия)

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
average_coll([1, 2, 3, 4], around=2)  # '2.50'
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

## 📊 Примеры

```python
data = [1, "2", [3, "true", "false"], (4, 5.5)]

print(summ_coll(data))                                # 16.5
print(average_coll(data, around=1))                   # '3.3'
print(count_if(data, condition=">=2"))                # 4
print(summ_if(data, condition=lambda x: x % 2 == 1))  # 9
print(average_if(data, condition=True))               # '2.75'
```

---

## ⚖ Лицензия

Этот проект распространяется под лицензией **[Apache-2.0 license](https://github.com/TFsadReD/Exel-Commands#Apache-2.0-1-ov-file)**

---

## 🏆 Автор:

- **TFsadReD**