import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    assert len(height) > 0 and len(weight) > 0, "assertion error: height and weight should not be empty"
    assert len(height) == len(weight), "assertion error: height and weight should have the same length"
    assert all(isinstance(h, (int, float)) for h in height), "assertion error: height should be a list of integers or floats"
    assert all(isinstance(h, (int, float)) for h in weight), "assertion error: weight should be a list of integers or floats"
    return [weight[i] / (height[i] ** 2) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    assert len(bmi) > 0, "assertion error: height and weight should not be empty"
    assert all(isinstance(h, (int, float)) for h in bmi), "assertion error: bmi should be a list of integers or floats"
    return [bmi[i] > limit for i in range(len(bmi))]

def main() -> None:
    try:
        height = [1.75, 1.65, 1.80]
        weight = [70, 50, 90]
        bmi = give_bmi(height, weight)
        print(bmi)
        limit = 20
        result = apply_limit(bmi, limit)
        print(result)

        # empty_height = []
        # empty_weight = []
        # bmi = give_bmi(empty_height, empty_weight)

        # height = [1.75, 1.65]
        # weight = [70, 50, 90]
        # bmi = give_bmi(height, weight)

        # height = ["ewded", 1.65, 1.80]
        # weight = [70, 50, 90]
        # bmi = give_bmi(height, weight)

        # bmi = [20, "ewded", 30]
        # result = apply_limit(bmi, limit)

        # bmi = []
        # result = apply_limit(bmi, limit)

        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi)
        limit = 26
        result = apply_limit(bmi, limit)
        print(result)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()