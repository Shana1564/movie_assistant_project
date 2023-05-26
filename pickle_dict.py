import pickle
my_dict = {"a": 1, "b": 2, "c": 3}

file = open("my_dict.pk1", "wb")
pickle.dump(my_dict, file)
file.close()
