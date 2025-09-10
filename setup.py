from setuptools import setup, find_packages

setup(
    name="text-on-image",
    version="0.1.0",
    description="Easily add Persian/English text on images with Pillow.",
    author="Ario",
    author_email="ario.h.abbadi@gmail.com",
    url="https://github.com/diaco-dev/text_on_image",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "text_on_image": ["fonts/vazir/*.ttf", "fonts/roboto/*.ttf"],
    },
    install_requires=[
        "Pillow",
        "arabic-reshaper",
        "python-bidi"
    ],
    python_requires=">=3.7",
)
