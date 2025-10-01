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


# flatten()


a = (1, "23", 324, "342.0", True, 3.4, False, "True", "False")

print(summ_coll([1, [2, [3, 4, (1, 2)]]]))
print(summ_coll(1, 2, [3, [4, [5]]], "6"))
print(average_coll([1, [2, [3, 4]]], 5))
