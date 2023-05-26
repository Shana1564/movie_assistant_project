import pickle
file = open("my_dict.pk1", "rb")
unpickled_dict = pickle.load(file)
print(unpickled_dict)