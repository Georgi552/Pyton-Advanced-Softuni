def age_assignment(*args, **kwargs):
    result = {}
    for x in args:

        result[x] = kwargs[x[0]]
    return result


print(age_assignment("Peter", "George", G=26, P=19))