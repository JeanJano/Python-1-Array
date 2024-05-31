from ctypes import Array
import imageio.v2 as imageio


def ft_load(path: str) -> Array:
    try:
        img = imageio.imread(path)
        print(f"The shape of the image is: {img.shape}")

        height, width, _ = img.shape
        for y in range(height):
            for x in range(width):
                if ((y <= 1 and x <= 1) or (y >= height - 1 and x >= width - 1)):
                    r, g, b = img[y, x]
                    print(f"[{r}, {g}, {b}]")

        return img

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
