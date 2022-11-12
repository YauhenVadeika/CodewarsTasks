# my task solution
def increment_string(strng):
    part = strng.rstrip('0123456789')
    main_part = strng[len(part):]
    if main_part == "":
        return strng + "1"
    return part + str(int(main_part) + 1).zfill(len(main_part))


print(increment_string("fo99obar99"))
print(increment_string("foobar00"))
print(increment_string("foo"))

# codewars task best solution
import re


def increment_string(input):
    match = re.search("(\d*)$", input)
    if match:
        number = match.group(0)
        if number is not "":
            return input[:-len(number)] + str(int(number) + 1).zfill(
                len(number))
    return input + "1"


# codewars task best solution
def increment_string(s):
    if s and s[-1].isdigit():
        num = s[len(s.rstrip("0123456789")):]
        return s[:-len(num)] + str(int(num) + 1).zfill(len(num))

    return s + "1"