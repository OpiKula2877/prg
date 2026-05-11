import pyautogui, time #1319, 418
from PIL import ImageGrab

def get_screen_pixel_color(x, y):
    """
    Get RGB color of a pixel at coordinates (x, y) from screen
    
    Args:
        x: X coordinate
        y: Y coordinate
    
    Returns:
        Tuple of (R, G, B) values
    """
    try:
        screenshot = ImageGrab.grab()
        pixel = screenshot.getpixel((x, y))
        
        # Handle images with alpha channel
        if isinstance(pixel, tuple) and len(pixel) == 4:
            return pixel[:3]
        return pixel
    except IndexError:
        print(f"Souřadnice ({x}, {y}) jsou mimo displej")
        return None


if __name__ == "__main__":
    x = int(input("Zadejte X souřadnici: "))
    y = int(input("Zadejte Y souřadnici: "))
    time.sleep(10)
    color = get_screen_pixel_color(x, y)
    
    if color:
        print(f"Barva na pixelu ({x}, {y}): RGB{color}")
