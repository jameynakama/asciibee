import argparse

from asciibee import constants, convert

parser = argparse.ArgumentParser(
    prog="asciibee",
    description="""Convert an image to ASCII art

    Scaling is done by reducing the image by a factor of 2 until it fits in the
    terminal window or the width and height are both below the max dimension you
    specify.""",
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument("image_path", help="Path to the image to convert")
parser.add_argument(
    "-s",
    "--shader",
    help=f"The shader to use (they increase in complexity)",
    type=int,
    choices=range(1, len(constants.SHADERS) + 1),
    default=len(constants.SHADERS),
    required=False,
)
parser.add_argument(
    "-w",
    "--max-width",
    help="The maximum allowable output width (number of columns)",
    type=int,
    required=False,
)
parser.add_argument(
    "-O",
    "--original-size",
    help="Output the original size of the image (will override max-dimension)",
    action="store_true",
)

args = parser.parse_args()

ascii_image = convert.AsciiImage(
    args.image_path,
    shader=constants.SHADERS[args.shader - 1],
    max_allowable_width=args.max_width,
)
ascii_image.convert(args.original_size)
ascii_image.show()
