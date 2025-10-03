from logic.logic import if_error, average_if, average_coll

a = 10
b = "1f"
c = (1, "23", 324, "342.0", True, 3.4, False, "True", "False")
d = (1, 2, [3, [4, [5]]], "6")
l = [1, "2", 3.5, True, False, "10", [5, "7"]]

print(average_if(l, condition="!= False", around=5))
print(average_coll(l,around=5))
print(if_error(f"int({b})", b))