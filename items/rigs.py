from typing import Literal


class Rig:
    def __init__(
            self,
            name: str,
            image_url: str,
            meta: bool,
    ):
        self.name = name
        self.image_url = image_url
        self.meta = meta


rig_list = [

    some_rig := Rig(
        name="",
        image_url="",
        meta=False,
    ),

]
