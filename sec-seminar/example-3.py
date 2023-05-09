import pickle


class Foo:
    def __init__(self):
        self.data = "hello"

    def __repr__(self) -> str:
        return f"<Foo {self.data}>"


foo_instance = Foo()

with open("data", "wb") as f:
    pickle.dump(foo_instance, f)

with open("data", "rb") as f:
    x = pickle.load(f)
    print(x)
