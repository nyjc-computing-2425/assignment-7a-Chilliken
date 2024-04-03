# Write a function to convert numbers to text numerals


def text_numeral(num):
    """
    Changes number to text based on range of numbers

    Parameters
    ----------
    num: int
        number to change to text

    Returns
    -------
    str
    text of number provided as parameter
    
    """
    
    num = str(num)

    num_dict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    text = ""
    if len(num) == 2 and num[0] != '0':
        tens = int(num[0]) * 10
        if tens >= 20:
            text += num_dict[tens]
            text += " "
            if num[1] in '123456789':
                ones = int(num[1])
                text += num_dict[ones] 
    
        elif tens < 20:
    
            num = int(num)
            text += num_dict[num]
    elif len(num) == 1:

        if num[0] in '123456789':
            ones = int(num[0])
            text += num_dict[ones]
    return text

