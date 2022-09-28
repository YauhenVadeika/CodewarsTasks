# my task solution
dict = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}


def switch_it_up(number):
    return dict[number]


print(switch_it_up(0))


# codewars task best solution
def switch_it_up(n):
    return [
        'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine'
    ][n]


# codewars task best solution
def switch_it_up(number):
    number_converter = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return number_converter[number]


# codewars task best solution
def switch_it_up(number):
    dict = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        0: "Zero"
    }

    return dict.get(number)