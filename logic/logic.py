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


def summ_coll(variable):
    summ = 0

    for char in variable:
        num_char = to_number(char)
        if num_char is None:
            return "SyntaxError"
        summ += num_char
    return summ


def average_coll(variable, around=None):
    num_variable = summ_coll(variable)
    if num_variable is None:
        return "SyntaxError"

    average_variable = num_variable / len(variable)
    if around is None:
        return average_variable
    else:
        return f"{average_variable:.{around}f}"


a = (1, "23", 324, "342.0", True, 3.4, False, "True", "False")

print(average_coll(a, 4))