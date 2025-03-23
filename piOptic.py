import digitalio
import board
import cv2
import numpy as np
from PIL import Image, ImageDraw
from adafruit_rgb_display import ssd1351  # pylint: disable=unused-import

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

disp = ssd1351.SSD1351 (spi, rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

width = disp.width
height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)


# Open video capture
cap = cv2.VideoCapture(0)  # /dev/video0

stop = True
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    height, width = frame.shape[:2]
    frame = frame[:height // 2, :]
	
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (128, 128))
    frame_resized = cv2.flip(frame_resized, 0)
    #frame_resized = cv2.flip(frame_resized, 1)

    # Convert resized frame to PIL Image
    frame_pil = Image.fromarray(frame_resized)
    draw = ImageDraw.Draw(frame_pil)
    width, height = frame_pil.size
    center_x, center_y = width // 2, height // 2
    #draw.line([(center_x, 0), (center_x, height)], fill="red", width=2)
    #draw.line([(0, center_y), (width, center_y)], fill="red", width=2)
    
    radius = 3
    draw.ellipse(
		(center_x - radius, center_y - radius, center_x + radius, center_y + radius),
		fill="red"
		)
	
    # Send frame to OLED
    disp.image(frame_pil)
    stop = input()
    
    if stop == "s": break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)
