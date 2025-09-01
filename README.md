# 🖼️ Text On Image Library

A simple and powerful library for adding Persian and English text to images using Pillow. It offers full support for Persian text (right-to-left, proper character shaping) and provides a user-friendly interface for text customization.

## 📦 Installation

To install the library, use the following command:

```bash
pip install text-on-image
```

## 🚀 Quick Start

You can easily add text to an image using the `add_text` function:

```python
from text_on_image import add_text

# Adding Persian text
add_text("input.png", "output_fa.png", text="تخفیف ویژه ۱۹ هزار تومان", lang="fa")

# Adding English text
add_text("input.png", "output_en.png", text="Special Offer $19", lang="en")
```

## ⚙️ Parameters

| Parameter        | Description                                                            |
|------------------|------------------------------------------------------------------------|
| `image_path`     | Path to the input image file (e.g., `input.png`)                        |
| `output_path`    | Path to the output image file (e.g., `output.png`)                      |
| `text`           | The text to display on the image                                        |
| `lang`           | Language of the text (`fa` for Persian, `en` for English)               |
| `position`       | Text position: combination of `(left|center|right, top|center|bottom)`  |
| `font_size`      | Font size (default: 40)                                                |
| `color`          | Text color (e.g., `"white"`, `"yellow"`)                                |
| `stroke_width`   | Stroke width for better text readability (default: 2)                   |
| `stroke_fill`    | Stroke color (e.g., `"black"`)                                         |

## 📂 Example

```python
from text_on_image import add_text

add_text(
    image_path="input.png",
    output_path="output.png",
    text="Hello World",
    lang="en",
    position=("center", "bottom"),
    font_size=48,
    color="yellow",
    stroke_width=2,
    stroke_fill="black"
)
```

## ✨ Features

- **Full Persian Support**: Right-to-left text and proper character shaping using `arabic_reshaper` and `python-bidi`.
- **Flexible Positioning**: Choose text position in both horizontal (left, center, right) and vertical (top, center, bottom) axes.
- **Dedicated Fonts**: Vazir font for Persian and Roboto for English.
- **Text Stroke**: Enhances text readability on varied image backgrounds.
- **Class-Based Design**: Easily extensible for custom use cases.
- **Easy Installation**: Published on PyPI, installable via `pip`.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.