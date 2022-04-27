def sorting_cheeses(** kwargs):
    sorted_cheases = sorted(kwargs.items(), key=lambda x:(-len(x[1]), x[0]))
    result = ''
    for name, quantities in sorted_cheases:
        result += name + '\n'
        sorted_quantities = sorted(quantities, reverse=True)

        result += "\n".join([str(el) for el in sorted_quantities]) + "\n"
    return result

print(
sorting_cheeses(
Parmigiano=[165, 215],
Feta=[150, 515],
Brie=[150, 125]
)
)