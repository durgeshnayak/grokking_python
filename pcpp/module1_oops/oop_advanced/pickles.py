import pickle


def pickle_test():
    print("pickle test")


with open("test.pickle", "wb") as f:
    pickle.dump(pickle_test, f)

with open("test.pickle", "rb") as f:
    loaded_test = pickle.load(f)
    print(loaded_test)
    print(type(loaded_test))
    loaded_test()  # This can be called as function definition is available in pickels module.
