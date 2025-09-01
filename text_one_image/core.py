from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import os


class TextOnImage:
    def __init__(self, font_dir=None):
        """
        :param font_dir: مسیر فونت‌ها (اگر None باشه از فونت‌های پیش‌فرض استفاده می‌کنه)
        """
        self.font_dir = font_dir or os.path.join(os.path.dirname(__file__), "fonts")
        self.default_fonts = {
            "fa": os.path.join(self.font_dir, "Vazir-Regular.ttf"),
            "en": os.path.join(self.font_dir, "Roboto-Regular.ttf"),
        }

    def _prepare_text(self, text: str, lang: str):
        """
        آماده‌سازی متن برای زبان فارسی (reshaping + bidi)
        """
        if lang == "fa":
            reshaped = arabic_reshaper.reshape(text)
            return get_display(reshaped)
        return text

    def add_text(
        self,
        image_path: str,
        output_path: str,
        text: str,
        lang: str = "en",
        position: tuple = ("center", "bottom"),
        font_size: int = 40,
        color: str = "white",
        stroke_width: int = 2,
        stroke_fill: str = "black",
    ):
        """
        متن را روی عکس اضافه می‌کند و ذخیره می‌کند.
        """
        image = Image.open(image_path).convert("RGBA")
        draw = ImageDraw.Draw(image)

        text = self._prepare_text(text, lang)
        font_path = self.default_fonts.get(lang, self.default_fonts["en"])
        font = ImageFont.truetype(font_path, font_size)

        # اندازه متن
        text_bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
        text_w, text_h = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # موقعیت
        if position[0] == "center":
            x = (image.width - text_w) // 2
        elif position[0] == "right":
            x = image.width - text_w - 20
        else:  # left
            x = 20

        if position[1] == "bottom":
            y = image.height - text_h - 20
        elif position[1] == "center":
            y = (image.height - text_h) // 2
        else:  # top
            y = 20

        # درج متن با استروک
        draw.text(
            (x, y),
            text,
            font=font,
            fill=color,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )

        # ذخیره
        image.save(output_path, format="PNG")
        return output_path
