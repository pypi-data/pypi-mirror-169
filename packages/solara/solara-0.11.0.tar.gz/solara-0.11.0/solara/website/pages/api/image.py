"""
# Image

```python
@reacton.component
def Image(image: Union[str, Path, "np.ndarray"]):
    ...
```

Displays an image from a URL, Path or numpy data.
"""

from pathlib import Path

import numpy as np
import PIL.Image

from solara.alias import reacton, sol


@reacton.component
def Page():

    image_path = Path(sol.__file__).parent.resolve() / "server/static/sun64.png"
    image_url = "/static/sun64.png"
    image_ndarray = np.asarray(PIL.Image.open(image_path))

    with sol.VBox() as main:
        with sol.Card(title="As a path"):
            sol.Image(image_path)

        with sol.Card(title="As a URL"):
            sol.Image(image_url)

        with sol.Card(title="As NumPy array"):
            sol.Image(image_ndarray)

    return main
