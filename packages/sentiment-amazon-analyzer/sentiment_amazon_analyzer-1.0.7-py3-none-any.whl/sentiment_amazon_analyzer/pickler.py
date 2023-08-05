import pickle

class Pickler:
    def __init__(self):
        pass

    def save_pickle(self, data, path):
        file = open(path, 'wb')
        pickle.dump(data, file)
        file.close()

    def load_pickle(self, path):
        file = open(path, 'rb')
        data = pickle.load(file)
        file.close()
        return data