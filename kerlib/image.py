import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def create_image_with_text(image_path="hello.png", text="test"):
    image_width, image_height = (300, 200)
    with Image.new("RGBA", (image_width, image_height), "yellow") as image:
        image.save(image_path, "PNG")
    add_text_to_image(image_path, text, image_font_size=20, fontColor="red")


def add_text_to_image(image_path, text,
                      new_image_path="newImage.png",
                      image_type="PNG",
                      image_font_size=30,
                      font_color="white"):
    with Image.open(image_path) as image:
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        font = ImageFont.truetype(
            os.environ.get("FONT_PATH", "/Library/Fonts/arial.ttf"),
            image_font_size)

        text_width, text_height = draw.textsize(text, font=font)
        draw.text(((image_width-text_width)/2, (image_height-text_height)/2),
                  text, fill=font_color, font=font)
        image.save(new_image_path, image_type)
