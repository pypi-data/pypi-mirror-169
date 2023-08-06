"""Word2Number Library that supports indian currency standards
"""
decimal_words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


indian_number_system = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "lac": 100000,
    "lakh": 100000,
    "crore": 10000000,
    "point": ".",
}


def number_formation(number_words):
    """
    function to form numeric multipliers for million, billion, thousand etc.

    input: list of strings
    return value: integer
    """

    numbers = []
    for number_word in number_words:
        numbers.append(indian_number_system[number_word])
    if len(numbers) == 4:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 3:
        return numbers[0] * numbers[1] + numbers[2]
    elif len(numbers) == 2:
        if 100 in numbers:
            return numbers[0] * numbers[1]
        else:
            return numbers[0] + numbers[1]
    else:
        return numbers[0]


def get_decimal_sum(decimal_digit_words):
    """function to convert post decimal digit words to numerial digits

    Args:
        decimal_digit_words (list(str)): list of strings of words

    Returns:
        float: numeric value of decimals
    """
    decimal_number_str = []
    for dec_word in decimal_digit_words:
        if dec_word not in decimal_words:
            return 0
        else:
            decimal_number_str.append(indian_number_system[dec_word])
    final_decimal_string = "0." + "".join(map(str, decimal_number_str))
    return float(final_decimal_string)


def word_to_num(number_sentence):
    """function to return integer for an input `number_sentence` string

    Args:
        number_sentence (str): words to be converted
    Returns:
        int: numeric value of input words
    """
    if not isinstance(number_sentence, str):
        raise ValueError(
            "Type of input is not string! Please enter a valid number word (eg. 'two crore twenty three thousand and forty nine')"
        )

    number_sentence = number_sentence.replace("-", " ").strip()
    number_sentence = number_sentence.lower()  # converting input to lowercase
    number_sentence = number_sentence.replace("lac", "lakh")

    if number_sentence.isdigit():  # return the number if user enters a number string
        return int(number_sentence)

    split_words = (
        number_sentence.strip().split()
    )  # strip extra spaces and split sentence into words

    clean_numbers = []
    clean_decimal_numbers = []

    # removing and, & etc.
    for word in split_words:
        if word in indian_number_system:
            clean_numbers.append(word)

    # Error message if the user enters invalid input!
    if len(clean_numbers) == 0:
        raise ValueError(
            "No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)"
        )

    # Error if user enters million,billion, thousand or decimal point twice
    if (
        clean_numbers.count("thousand") > 1
        or clean_numbers.count("lakh") > 1
        or clean_numbers.count("crore") > 1
        or clean_numbers.count("point") > 1
    ):
        raise ValueError(
            "Redundant number word! Please enter a valid number word (eg. two lakh twenty three thousand and forty nine)"
        )

    # separate decimal part of number (if exists)
    if clean_numbers.count("point") == 1:
        clean_decimal_numbers = clean_numbers[clean_numbers.index("point") + 1 :]
        clean_numbers = clean_numbers[: clean_numbers.index("point")]

    crore_index = clean_numbers.index("crore") if "crore" in clean_numbers else -1
    lakh_index = clean_numbers.index("lakh") if "lakh" in clean_numbers else -1
    thousand_index = (
        clean_numbers.index("thousand") if "thousand" in clean_numbers else -1
    )

    if (
        thousand_index > -1
        and (thousand_index < lakh_index or thousand_index < crore_index)
    ) or (lakh_index > -1 and lakh_index < crore_index):
        raise ValueError(
            "Malformed number! Please enter a valid number word (eg. two lakh twenty three thousand and forty nine)"
        )

    total_sum = 0  # storing the number to be returned

    if len(clean_numbers) > 0:
        # hack for now, better way TODO
        if len(clean_numbers) == 1:
            total_sum += indian_number_system[clean_numbers[0]]

        else:
            if crore_index > -1:
                crore_multiplier = number_formation(clean_numbers[0:crore_index])
                total_sum += crore_multiplier * 10000000

            if lakh_index > -1:
                if crore_index > -1:
                    lakh_multiplier = number_formation(
                        clean_numbers[crore_index + 1 : lakh_index]
                    )
                else:
                    lakh_multiplier = number_formation(clean_numbers[0:lakh_index])
                total_sum += lakh_multiplier * 100000

            if thousand_index > -1:
                if lakh_index > -1:
                    thousand_multiplier = number_formation(
                        clean_numbers[lakh_index + 1 : thousand_index]
                    )
                elif crore_index > -1 and lakh_index == -1:
                    thousand_multiplier = number_formation(
                        clean_numbers[crore_index + 1 : thousand_index]
                    )
                else:
                    thousand_multiplier = number_formation(
                        clean_numbers[0:thousand_index]
                    )
                total_sum += thousand_multiplier * 1000

            if thousand_index > -1 and thousand_index != len(clean_numbers) - 1:
                hundreds = number_formation(clean_numbers[thousand_index + 1 :])
            elif lakh_index > -1 and lakh_index != len(clean_numbers) - 1:
                hundreds = number_formation(clean_numbers[lakh_index + 1 :])
            elif crore_index > -1 and crore_index != len(clean_numbers) - 1:
                hundreds = number_formation(clean_numbers[crore_index + 1 :])
            elif thousand_index == -1 and lakh_index == -1 and crore_index == -1:
                hundreds = number_formation(clean_numbers)
            else:
                hundreds = 0
            total_sum += hundreds

    # adding decimal part to total_sum (if exists)
    if len(clean_decimal_numbers) > 0:
        decimal_sum = get_decimal_sum(clean_decimal_numbers)
        total_sum += decimal_sum

    return total_sum
