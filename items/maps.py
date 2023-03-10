from typing import Literal


class Map:
    def __init__(
            self,
            name: str,
            image_url: str,
    ):
        self.name = name
        self.image_url = image_url


Factory = Map(
    name="Factory",
    image_url="",
)
