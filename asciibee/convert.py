import os

from PIL import Image

from asciibee import constants


class AsciiImage:
    ascii_matrix: list = []

    def __init__(
        self,
        image_path: str,
        shader: list,
        max_allowable_width: int = None,
    ) -> None:
        self.image_path = image_path
        self.shader = shader
        self.max_allowable_width = max_allowable_width

    def _reduce(self, image: Image) -> Image:
        if not self.max_allowable_width:
            terminal_size = os.get_terminal_size()
            while image.size[0] > terminal_size[0] or image.size[1] > terminal_size[1]:
                image = image.reduce(2)
        else:
            while image.size[0] > self.max_allowable_width:
                image = image.reduce(2)
        return image

    def convert(self, original_size: bool = False) -> None:
        with Image.open(self.image_path).convert("L") as image:
            if not original_size:
                image = self._reduce(image)

            for y in range(image.size[0]):
                self.ascii_matrix.append([])
                for x in range(image.size[1]):
                    pixel = image.getpixel((x, y))
                    value = (pixel * (len(self.shader) - 1)) / 255
                    self.ascii_matrix[y].append(self.shader[int(value)])

    def show(self) -> None:
        for row in self.ascii_matrix:
            for char in row:
                print(char, end="")
            print()
