def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    This function calculates the Body Mass Index (BMI) for each
    pair of height and weight.

    Parameters:
    height (list[int | float]): A list of heights in meters.
    weight (list[int | float]): A list of weights in kilograms.

    Returns:
    list[int | float]: A list of BMIs.

    Raises:
    AssertionError: If height and weight lists are empty, not of the
    same length, or not lists of integers or floats.
    """
    assert len(height) > 0 and len(weight) > 0, """assertion error: height and
        weight should not be empty"""
    assert len(height) == len(weight), """assertion error: height and weight
        should have the same length"""
    assert all(isinstance(h, (int, float)) for h in height), """assertion
        error: height should be a list of integers or floats"""
    assert all(isinstance(h, (int, float)) for h in weight), """assertion
        error: weight should be a list of integers or floats"""
    return [weight[i] / (height[i] ** 2) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function applies a limit to a list of BMIs and returns a list of
    booleans indicating if each BMI exceeds the limit.

    Parameters:
    bmi (list[int | float]): A list of BMIs.
    limit (int): The limit to apply.

    Returns:
    list[bool]: A list of booleans indicating if each BMI exceeds the limit.

    Raises:
    AssertionError: If bmi list is empty or not a list of integers or floats.
    """
    assert len(bmi) > 0, """assertion error: height and weight should
        not be empty"""
    assert all(isinstance(h, (int, float)) for h in bmi), """assertion error:
        bmi should be a list of integers or floats"""
    return [bmi[i] > limit for i in range(len(bmi))]


# def main() -> None:
#     try:
#         height = [1.75, 1.65, 1.80]
#         weight = [70, 50, 90]
#         bmi = give_bmi(height, weight)
#         print(bmi)
#         limit = 20
#         result = apply_limit(bmi, limit)
#         print(result)

#         # empty_height = []
#         # empty_weight = []
#         # bmi = give_bmi(empty_height, empty_weight)

#         # height = [1.75, 1.65]
#         # weight = [70, 50, 90]
#         # bmi = give_bmi(height, weight)

#         # height = ["ewded", 1.65, 1.80]
#         # weight = [70, 50, 90]
#         # bmi = give_bmi(height, weight)

#         # bmi = [20, "ewded", 30]
#         # result = apply_limit(bmi, limit)

#         # bmi = []
#         # result = apply_limit(bmi, limit)

#         height = [2.71, 1.15]
#         weight = [165.3, 38.4]
#         bmi = give_bmi(height, weight)
#         print(bmi)
#         limit = 26
#         result = apply_limit(bmi, limit)
#         print(result)

#     except AssertionError as e:
#         print(e)


# if __name__ == "__main__":
#     main()
