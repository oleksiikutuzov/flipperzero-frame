from PIL import Image
import sys

# Open screen background
img1 = Image.open(r"images/background.png")

# Open screen frame
img2 = Image.open(r"images/frame.png")

# Open screenshot itself
img3 = Image.open(sys.argv[1])

# Paste frame over screen background
img1.paste(img2, (0, 0), mask=img2)

# Resize the screenshot
img3 = img3.resize((784, 416), Image.Resampling.LANCZOS)

# Paste the screenshot over the frame with screen background
img1.paste(img3, (683, 294))

img1.save('framed_' + sys.argv[1])
