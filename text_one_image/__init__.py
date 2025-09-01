from .core import TextOnImage

_default = TextOnImage()

def add_text(image_path, output_path, text, **kwargs):

    return _default.add_text(image_path, output_path, text, **kwargs)

__all__ = ["TextOnImage", "add_text"]
