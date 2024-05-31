import imageio.v2 as imageio
from ctypes import Array


def ft_load(path: str) -> Array:
    try: 
        img = imageio.imread(path)
        print(f"The shape of the image is: {img.shape}")

        height, width, _ = img.shape
        for y in range(height):
            for x in range(width):
                r, g, b = img[y, x]
                print(f"[{r}, {g}, {b}]")

        return img

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)


def main() -> None:
    path = "../landscape.jpg"
    ft_load(path)


if __name__ == "__main__":
    main()
