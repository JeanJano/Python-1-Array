def slice_me(family: list, start: int, end: int) -> list:
    assert isinstance(family, list), "assertion error: family should be a list"
    assert all(isinstance(f, list) for f in family), "assertion error: family should be a list of lists"
    assert len(family) > 0, "assertion error: family should not be empty"
    assert all(len(f) == len(family[0]) for f in family), "assertion error: all lists in family should have the same length"
    assert all(all(isinstance(f, (int, float)) for f in sublist) for sublist in family), "assertion error: all elements in family should be integers or floats"
    
    print("My shape is : (", len(family), ", ", len(family[0]) if family else 0, ")", sep="")
    new_family = family[start:end]
    print("My new shape is : (", len(new_family), ", ", len(new_family[0]) if new_family else 0, ")", sep="")
    return new_family


def main () -> None:
    try :
        family = [
            [1.8, 78.4],
            [2.15, 102.7],
            [2.1, 98.5],
            [1.88, 75.2]
        ]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

        # family = [
        #     [1.8, 78.4],
        #     [2.15, 102.7],
        #     [2.1, 98.5],
        #     [1.88, 75.2]
        # ]
        # family = [[]]
        # family = 1
        # family = [12, 13]
        family = [
            [1.8, 78.4, 5, 3 ,4],
            [2.15, 102.7],
            [2.1, 98.5, 2],
            [1.88, 75.2]
        ]
        
        print(slice_me(family, 0, 2))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()