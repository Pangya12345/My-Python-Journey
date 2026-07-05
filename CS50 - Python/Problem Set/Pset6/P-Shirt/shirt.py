import sys
from PIL import Image, ImageOps


try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif sys.argv[2][sys.argv[2].index("."):] != ".jpg" and sys.argv[2][sys.argv[2].index("."):] != ".jpeg" and sys.argv[2][sys.argv[2].index("."):] != ".png":
        sys.exit("Invalid output")

    elif sys.argv[1][sys.argv[1].index("."):] == ".jpg" and sys.argv[2][sys.argv[2].index("."):] == ".png":
        sys.exit("Input and output have different extensions")

    else:
    
        shirt = Image.open("shirt.png")
        
        background = Image.open(sys.argv[1])

        size = shirt.size

        background_resized = ImageOps.fit(background, size)

        background_resized.paste(shirt, (0, 0), shirt) 

        background_resized.save(sys.argv[2])      








except FileNotFoundError:
    sys.exit("Input does note exist")
