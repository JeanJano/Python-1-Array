from load_image import ft_load

def ft_zoom(path: str) -> None:
    ft_load(path)

def main() -> None:
    ft_zoom("../animal.jpeg")

if __name__ == "__main__":
    main()