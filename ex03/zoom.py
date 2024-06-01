from load_image import ft_load
import matplotlib.pyplot as plt

def ft_zoom(path: str, crop: dict) -> None:
    try:
        assert isinstance(crop, dict), "assertion error: crop should be a dictionary"
        assert all(key in crop for key in ['top', 'bottom', 'left', 'right']), "assertion error: crop should have the keys 'top', 'bottom', 'left', 'right'"

        img = ft_load(path)
        assert img is not None, "assertion error: image should not be None"

        crop_img = img[crop['top']:crop['bottom'], crop['left']:crop['right']]
        plt.imshow(crop_img)
        # plt.show()
        plt.savefig("crop.jpeg")

        print(f"New size in pixel of the image: x:{crop['right'] - crop['left']} y:{crop['bottom'] - crop['top']}")
        print(f"New shape after slicing: {crop_img.shape}")
        height, width, _ = crop_img.shape
        for y in range(height):
            for x in range(width):
                r, g, b = img[y, x]
                print(f"[{r}, {g}, {b}]")
    
    except AssertionError as e:
        print(e)

def main() -> None:
    crop = {
        'top': 100,
        'bottom': 500,
        'left': 400,
        'right': 900
    }
    ft_zoom("../animal.jpeg", crop)

if __name__ == "__main__":
    main()