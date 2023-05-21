"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""

# my task solution, my second life
import re


def regular(arr):
    return bool(
        re.match("^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])[a-zA-Z\d]{6,}$", arr))


print(regular('fjd3IR9'))
print(regular('ghdfj32'))
print(regular('123'))
print(regular('abc'))

# codewars task best solution
from re import compile, VERBOSE

regex = compile(
    """
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)

# codewars task best solution
regex = (
    '^'  # start line
    '(?=.*\d)'  # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'  # permitted characters (alphanumeric only)
    '{6,}'  # length at least 6 chars
    '$'  # end line
)
# codewars task best solution
regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"
# codewars task best solution
regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
# codewars task best solution
regex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[^a-zA-Z0-9]).{6,}$"
# codewars task best solution
from re import compile, VERBOSE

regex = compile(
    """
^ # start letter
(?=.*?[a-z]) # have lowercase letter
(?=.*?[A-Z]) # have uppercase letter
(?=.*?[0-9]) # have number
[A-Za-z0-9] # only alphabetical
{6,} # from 6 to .
$ # end the line
""", VERBOSE)
# codewars task best solution
import re

regex = re.compile(
    r"""
    (?=^[a-zA-Z0-9]{6,}$)
    (?=\w*[a-z])
    (?=\w*[A-Z])
    (?=\w*\d)
""", re.X)
# codewars task best solution
# Beast , henrywangx , miccl , J-Featherstone , rismakov , chrisdawgr , balberts , becca21 , lion_dron , TTolubaev (+ 231)
regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$"
# codewars task best solution
# lwalker
regex = '(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])^[^\W_]{6,}$'
# codewars task best solution
# ARMANG
#regex= "(?=.{6,})(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])"
regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$"
# codewars task best solution
# kmactavish, brownmike, ad2Phnx, Hypnotiz, hofaiwong, lusbenjamin, Zack_Zack, LSmith-Zenoscave, josebama, chewiee (+ 72)
regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9]{6,}$"
