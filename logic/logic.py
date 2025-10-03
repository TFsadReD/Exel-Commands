def type_query(variable):
    format_variable = type(variable).__name__
    return format_variable


def to_number(variable):
    match type_query(variable):
        case "int" | "float":
            return variable
        case "str":
            if variable.isdigit():
                return int(variable)
            try:
                return float(variable)
            except:
                if variable.lower() == "true":
                    return 1
                elif variable.lower() == "false":
                    return 0
        case "bool":
            return int(variable)
        case _:
            return None


def flatten(variable):
    result = []
    for char in variable:
        if isinstance(char, (list, tuple, set)):
            result.extend(flatten(char))
        else:
            result.append(char)
    return result


def summ_coll(*args):
    summ = 0
    variable = flatten(args)

    for char in variable:
        num_char = to_number(char)
        if num_char is None:
            return "SyntaxError"
        summ += num_char
    return summ


def average_coll(*args, around=None):
    variable = flatten(args)

    num_variable = summ_coll(*variable)
    if num_variable is None:
        return "SyntaxError"

    average_variable = num_variable / len(variable)
    if around is None:
        return average_variable
    else:
        return f"{average_variable:.{around}f}"


def count_if(*args, condition=">0"):
    variable = flatten(args)
    k = 0

    if isinstance(condition, str):
        for char in variable:
            num = to_number(char)
            if num is None:
                continue
            if eval(f"{num}{condition}"):
                k += 1

    elif callable(condition):
        for char in variable:
            if condition(char):
                k += 1

    elif condition is True:
        k = sum(1 for char in variable if char)

    return k


def summ_if(*args, condition=">0"):
    variable = flatten(args)
    summ = 0

    if isinstance(condition, str):
        for char in variable:
            num = to_number(char)
            if num is None:
                continue
            if eval(f"{num}{condition}"):
                summ += num

    elif callable(condition):
        for char in variable:
            num = to_number(char)
            if num is not None and condition(num):
                summ += num

    elif condition is True:
        summ = summ_coll(*args)
    return summ


def average_if(*args, condition=">0", around=None):
    variable = flatten(args)
    summ = 0
    count = 0

    if isinstance(condition, str):
        for char in variable:
            num = to_number(char)
            if num is None:
                continue
            if eval(f"{num}{condition}"):
                summ += num
                count += 1

    elif callable(condition):
        for char in variable:
            num = to_number(char)
            if num is not None and condition(num):
                summ += num
                count += 1

    elif condition is True:
        summ = summ_coll(*args)
        count = len(flatten(variable))


    average_variable = summ / count
    if around is None:
        return average_variable
    else:
        return f"{average_variable:.{around}f}"


def if_error(condition, error=None, returning=None):
    try:
        if returning is None:
            result = eval(f"{condition}")
            return result
        elif returning == True:
            eval(f"{condition}")
        else:
            print("Error, use True or None")
    except:
        return error