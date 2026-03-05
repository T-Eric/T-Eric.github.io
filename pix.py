from PIL import Image

left = Image.open("readme_preview/sourapple.jpg")
right = Image.open("readme_preview/transapple.png")

canvas = Image.new("RGBA", (left.width + right.width, left.height))
canvas.paste(left, (0, 0))
canvas.paste(right, (left.width, 0))

canvas.save("readme_preview/concat.png")
