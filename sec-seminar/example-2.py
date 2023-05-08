import json


class Foo:
    def __init__(self):
        self.data = "hello"

    def __repr__(self) -> str:
        return f"<Foo {self.data}>"


foo_instance = Foo()

with open("data.json", "w") as f:
    json.dump(foo_instance, f)

with open("data.json", "r") as f:
    x = json.load(f)
    print(x)
