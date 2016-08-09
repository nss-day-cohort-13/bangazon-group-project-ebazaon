import pickle

def serialize(self, file_name, content):
  with open(file_name, 'wb+') as f:
    pickle.dump(content, f)


def deserialize(self, file_name, content):
  with open(file_name, 'rb+') as f:
    content = pickle.load(f)