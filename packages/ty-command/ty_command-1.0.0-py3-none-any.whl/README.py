from sys import path

path.insert(0, "./src/ty")

import ty

with open("README.md", "w") as f:
    f.write(ty.__doc__)
