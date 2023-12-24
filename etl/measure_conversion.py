import re
from typing import Union

splitter = "splitter"


def convert_measure_to_grams(measure: str) -> Union[float, None]:
    """
    Convert a measure to grams based on a predefined dictionary of conversions.

    :param measure: The input measure to be converted.
    :returns:
     - Union[float, None]: The converted measure in grams or None if no matching conversion is found.
    """
    conversion_dict_to_grams = {
        "ml": 1,
        "oz": 30,
        "tsp": 5,
        "tblsp": 15,
        "tbsp": 15,
        "cup": 237,
        "jigger": 45,
        "pint": 568,
        "fluid oz": 30,
        "pound (lb)": 454,
        "shot": 30,
        "cl": 10,
        "dash": 1,
        "part": 5,
        "snit": 89,
        "split": 177,
    }

    for key, value in conversion_dict_to_grams.items():
        if re.search(key, measure, re.IGNORECASE):
            splitter_str = re.sub(r"[^\d./-]", splitter, measure)
            numeric_list = splitter_str.split(splitter)
            numeric_list = list(filter(None, numeric_list))
            if len(numeric_list) == 1:
                if "-" in numeric_list[0]:
                    numeric_list = numeric_list[0].split("-")
                return eval(numeric_list[0]) * value
            elif len(numeric_list) == 2:
                numeric_1 = (
                    "0"
                    if (numeric_list[0] == "-") or (numeric_list[0].startswith("/"))
                    else numeric_list[0]
                )
                numeric_2 = (
                    "0"
                    if (numeric_list[1] == "-") or (numeric_list[1].startswith("/"))
                    else numeric_list[1]
                )

                return (eval(numeric_1) * value) + (eval(numeric_2) * value)

    return None
