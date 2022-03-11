def create(string):
    return lambda stra: stra==string

tom=create("pass_for_Tom")
print(tom("pass_for_tom"))