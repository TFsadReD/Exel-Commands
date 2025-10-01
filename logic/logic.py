def type_query(variable):
    format_variable = str(type(variable)).replace("<class '", "").replace("'>", "")
    return format_variable


def check_type(variable):
    for char in variable:
        format_char = type_query(char)
        # print(format_char)
        if format_char in "int, float":
            # print(f"standart: {char}")
            ...
        elif format_char == "str" and char.isdigit():
            # print(f"isdigit: {char}")
            ...
        elif format_char == "str" and "." in char:
            for i in range(len(char)):
                char = char[:-1]
                if char[-1] == ".":
                    break
            ...
        elif format_char == "bool":
            ...
        elif char == "True" or char == "False":
            ...
        else:
            return True


def printer(variable):
    format_variable = type_query(variable)
    for char in variable:
        format_char = type_query(char)
        if format_char in "int, float":
            print(f"standart: {char}")
        elif format_char not in "int, float" and char.isdigit():
            print(f"isdigit: {char}")


def summ_coll(variable):
    check = check_type(variable)
    if check:
        return "SyntaxError"

    summ = 0
    for char in variable:
        format_char = type_query(char)
        if format_char in "int, float":
            summ += char
        elif format_char == "str" and char.isdigit():
            summ += int(char)
        elif format_char == "str" and "." in char:
            summ += float(char)
        elif format_char == "bool":
            if char:
                summ += 1
        elif char == "True":
            summ += 1
    return summ


def average_value(variable, around=None):
    check = check_type(variable)
    if check:
        return "SyntaxError"

    average_variable = summ_coll(variable) / len(variable)
    if around is None:
        return average_variable
    else:
        return f"{average_variable:.{around}f}"


a = (1, "23", 324, "342.0", True, 3.4, False, "True", "False")

print(average_value(a))