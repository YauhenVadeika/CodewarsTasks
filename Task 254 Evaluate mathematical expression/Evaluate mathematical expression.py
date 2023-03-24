# my task solution
import operator

OP_DICT = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def tokenize(e):
    tokens = []
    st = []
    op = dict()
    cl = dict()

    i = 0
    while i < len(e):
        if e[i] == ' ':
            i += 1
            continue
        if e[i].isdigit():
            j = i
            while i + 1 < len(e) and (e[i + 1].isdigit() or e[i + 1] == '.'):
                i += 1
            tokens.append(float(e[j:i + 1]))
        else:
            if e[i] == '(':
                st.append(len(tokens))
            if e[i] == ')':
                j = len(tokens)
                op[j] = st.pop()
                cl[op[j]] = j
            tokens.append(e[i])

        i += 1
    return tokens, op, cl


def calc(e):
    tokens, op, cl = tokenize(e)

    def eval_muldiv(tokens):
        v, o = 1, '*'
        for token in tokens:
            if isinstance(token, float):
                v = OP_DICT[o](v, token)
            else:
                o = token
        return v

    def dfs(idx_st, idx_en):
        idx = idx_st
        tokens_no_par = []
        while idx <= idx_en:
            if tokens[idx] == '(':
                v = dfs(idx + 1, cl[idx] - 1)
                tokens_no_par.append(v)
                idx = cl[idx]
            else:
                tokens_no_par.append(tokens[idx])

            idx += 1
        tokens_no_neg = []
        idx = 0
        while idx < len(tokens_no_par):
            if tokens_no_par[idx] != '-':
                tokens_no_neg.append(tokens_no_par[idx])
            else:
                if idx > 0 and isinstance(tokens_no_par[idx - 1], float):
                    tokens_no_neg.append('-')
                else:
                    j = idx
                    while not isinstance(tokens_no_par[idx], float):
                        idx += 1
                    n_neg = idx - j
                    v = tokens_no_par[idx] * ((-1)**(n_neg % 2))
                    tokens_no_neg.append(v)
            idx += 1
        idx_addsub = [-1]
        for idx, token in enumerate(tokens_no_neg):
            if token == '+' or token == '-':
                idx_addsub.append(idx)

        v, o = 0, '+'
        for i in range(1, len(idx_addsub)):
            j, k = idx_addsub[i - 1], idx_addsub[i]
            v1 = eval_muldiv(tokens_no_neg[j + 1:k])
            v = OP_DICT[o](v, v1)
            o = tokens_no_neg[k]

        v = OP_DICT[o](v, eval_muldiv(tokens_no_neg[idx_addsub[-1] + 1:]))
        return v

    return dfs(0, len(tokens) - 1)


print(calc("1 + 1"))
print(calc("8/16"))

# codewars task best solution
import re
from operator import mul, truediv as div, add, sub

OPS = {'*': mul, '/': div, '-': sub, '+': add}


def calc(expression):
    tokens = re.findall(r'[.\d]+|[()+*/-]', expression)
    return parse_AddSub(tokens, 0)[0]


def parse_AddSub(tokens, iTok):

    v, iTok = parse_MulDiv(tokens, iTok)

    while iTok < len(tokens) and tokens[iTok] != ')':
        tok = tokens[iTok]
        if tok in '-+':
            v2, iTok = parse_MulDiv(tokens, iTok + 1)
            v = OPS[tok](v, v2)

    return v, iTok


def parse_MulDiv(tokens, iTok):

    v, iTok = parse_Term(tokens, iTok)

    while iTok < len(tokens) and tokens[iTok] in '*/':
        op = tokens[iTok]
        v2, iTok = parse_Term(tokens, iTok + 1)
        v = OPS[op](v, v2)

    return v, iTok


def parse_Term(tokens, iTok):
    tok = tokens[iTok]

    if tok == '(':
        v, iTok = parse_AddSub(tokens, iTok + 1)
        if iTok < len(tokens) and tokens[iTok] != ')': raise Exception()

    elif tok == '-':
        v, iTok = parse_Term(tokens, iTok + 1)
        v, iTok = -v, iTok - 1

    else:
        v = float(tok)

    return v, iTok + 1


# codewars task best solution
def calc(expression):
    ex = list(expression.replace(' ', ''))

    def peek():
        return ex[0] if ex else ''

    def get():
        return ex.pop(0)

    def number():
        result = get()
        while peek() >= '0' and peek() <= '9' or peek() == '.':
            result += get()
        return float(result)

    def factor():
        if peek() >= '0' and peek() <= '9':
            return number()
        elif peek() == '(':
            get()  # '('
            result = expression()
            get()  # ')'
            return result
        elif peek() == '-':
            get()
            return -factor()
        return 0  # error

    def term():
        result = factor()
        while peek() == '*' or peek() == '/':
            if get() == '*':
                result *= factor()
            else:
                result /= factor()
        return result

    def expression():
        result = term()
        while peek() == '+' or peek() == '-':
            if get() == '+':
                result += term()
            else:
                result -= term()
        return result

    return expression()


# codewars task best solution
def calc(l):
    while ')' in l:
        for i, c in enumerate(l):
            if c == '(': lastopen = i
            if c == ')':
                l = l[:lastopen] + str(calc(l[lastopen + 1:i])) + l[i + 1:]
                break

    stack = []
    for t in tokens(l):
        if stack and (stack[-1] == '*' or stack[-1] == '/'):
            op, a = stack.pop(), stack.pop()
            t = a / t if op == '/' else a * t
        stack.append(t)

    stack = stack[::-1]

    a = 0 if stack[-1] in ['+', '-'] else stack.pop()

    while stack:
        op, t = stack.pop(), stack.pop()
        a = a + t if op == '+' else a - t

    return a


def tokens(s):
    R = [('--', '+'), ('+-', '-'), ('++', '+'), ('-+', '-'), ('*+', '*'),
         ('/+', '/')]

    s = ''.join(s.split())
    while any(f in s for f, _ in R):
        for f, r in R:
            s = s.replace(f, r)

    for t in '*/-+':
        s = s.replace(t, ' ' + t + ' ')
    s = s.replace('  ', ' ').replace('* - ', '* -').replace('/ - ', '/ -')

    return [
        t if t in '*/+-' else float(t) if '.' in t else int(t)
        for t in s.split()
    ]


# codewars task best solution
def parse(expr, i):
    num = ''
    while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
        num += expr[i]
        i += 1
    return float(num), i - 1


def calculate(expr, i):
    res, op, p = [], ['+'], 0
    while i < len(expr) and expr[i] != ')':
        if expr[i] == ' ': pass
        elif not expr[i].isdigit() and expr[i] != '(':
            op.append(expr[i])
        else:
            if expr[i].isdigit(): p, i = parse(expr, i)
            else: p, i = calculate(expr, i + 1)
            for sign in op[1:]:
                if sign == '-': p = -p
            if op[0] == '+': res.append(p)
            elif op[0] == '-': res.append(-p)
            elif op[0] == '*': res[-1] *= p
            else: res[-1] /= p
            op.clear()
        i += 1
    return sum(res), i


def calc(expr):
    res, _ = calculate(expr, 0)
    return res


# codewars task best solution

# Evaluate a mathematical expression with nested parenthesis and uniary operators
# Approach: A Pratt Parser is built that was based on the approach provided in
#           ref [1].  The Pratt Parser generates a parse-tree.  The parse tree
#           is then evaluated to a single number
#
#Refs: [1]:  effbot.org/zone/simple-top-down-parsing.htm
import re  #used for the tokenizer

#General nomenclature regarding a Pratt Parser:
# "binding powers" are precedence levels
# "nud" is 'null denotation'  and "led"  is 'left denotation'.
#   A nud does not care about the tokens to the left.
#   A led does care about tokens to the left
#   A nud method is used by values (such as variables and literals) and by prefix operators.
#   A led method is used by infix operators and suffix operators.
#  A token may have both a nud and a led. e.g.  '-' might be both a prefix operator (negating a value)
#  and an infix operator (typical subtraction), so it would have both nud and led methods.

#
#Approach begins here (note; comments etc are as is but made with best effort)
#

#Global Variables (keeping it simple for learning purposes)
#--curToken: Current token in the stream
#--tokenGenerator: A generator which allows us to get the next token (by calling next)
#--symbolTable: A dictionary, keyed on the id of the token (e.g. '+', '(', etc) whosethat contains
#               value is the class of the token (with it's nud, led methods etc)
curToken = None
tokenGenerator = None
symbolTable = {}


#Base class for all symbols (e.g. +, -, (, **, unary operators, terinary operators)
#Everyone gets an id, value and tree node, everyone gets a nud and led method
class symbolBase(object):

    id = None  #Token Name
    value = None  #Only for literals (e.g. .value is 4.1)
    first = second = third = None  #Nodes; third is not used in the calculator program

    def nud(self):
        raise SyntaxError("Syntax error (%r)." % self.id)

    def led(self, left):
        raise SyntaxError("Unknown operator (%r)." % self.id)

    #Pretty plot: Don't print None
    def __repr__(self):
        if self.id == "(name)" or self.id == "(literal)":
            return "(%s %s)" % (self.id[1:-1], self.value)
        out = [self.id, self.first, self.second, self.third]
        out = map(str, filter(None, out))
        return "(" + " ".join(out) + ")"

    #---end __repr__


#---end class


#Build or update a new symbol (e.g. +, -, *, unary operator,...)
#  If symbol does exist: Updates the binding power of the symbol
#  If the symbol does not exist: Create a symbol class, and store the class data,
#                                and store the new symbol in the symbol table
# The function returns the symbol (class) which allows easy assignment of the led
# and nud functions
def symbol(id, bp=0):
    try:
        s = symbolTable[id]
    except KeyError:  #Scenario: New symbol is being created
        #Make a class for the new symbol
        class s(symbolBase):  #New symbol 's' is of the base class
            pass

        #appropriate data storage
        s.__name__ = "symbol-" + id  #nice for debugging :)
        s.id = id  #Token name e.g. +, **, (,...
        s.lbp = bp  #Default binding power is zero
        symbolTable[id] = s  #store our new symbol in the symbol table
    else:  #Scenario: Symbol has already been defined
        s.lbp = max(bp, s.lbp)  #Update the binding power of the symbol

    return s  #return the symbol class (so we can easily assign led or nud )


#---end function


#Defines a led method for a symbol with a given id; creates symbol class if need be
#  See doc on symbol(...) function  (token class will be created if it does not exist)
def infix(id, bp):

    def led(self, left):
        self.first = left
        self.second = expression(bp)
        return self

    symbol(id, bp).led = led  #Store the led method for this symbol


#---end function


#Sets a nud method for a symbol; creates symbol class if need be
#  See doc on symbol(...) function  (token class will be created if it does not exist)
def prefix(id, bp):

    def nud(self):
        self.first = None
        self.second = expression(bp)
        return self

    symbol(id).nud = nud


#---end function


#Build and set the led for right-associative infix symbols; creates symbol class if need be
#  See doc on symbol(...) function  (token class will be created if it does not exist)
# e.g. infix_r('**',30) will make the exponentiation class with identifier '**' and have
#      a binding power of 30; the led method gets a binding power of 29, garanteeing that
#      the operator will be right-evaluated in the expression() function
def infixRight(id, bp):

    def led(self, left):
        self.first = left
        self.second = expression(bp - 1)  #To garantee right associativity
        return self

    symbol(id, bp).led = led  #symbol(...) creates the token class if need be


#---end function

#----------------------
#Define the symbols operators for the parser and their binding power:
infix("+", 10)  #Addition left associative
prefix("+", 100)  #Unary Operator +
infix("-", 10)  #Subtraction left associative
prefix("-", 100)  #Unary Operator -
infix("*", 20)  #Multiplication left associative
infix("/", 20)  #Division left associative
infixRight("**",
           30)  #Exponentiation, right associative (e.g. 2^3^2 is 2^9 not 8^2)

#literal symbol has binding power of 0; similarly end of file (end) has binding zero
#additionally the parenthesis operators have
symbol("(literal)").nud = lambda self: self
symbol("(end)")
symbol(")")  #---Handeling Parenthesis: Each has binding power of zero


#The left parentheisis must have a special operation: We must tunnle-down to evaluate
#what is inside the expression
def nud(self):
    expr = expression()  #chew through the expression inside the parenthesis
    advance(
        ")"
    )  #once we are through the expression, we must have a ')' and push past it
    return expr


#---end funcion
symbol("(").nud = nud  #store the nud function for the left parenthesis

#----------------------end of defining symbols


#For use, currently, when evaluating parentheis (see nud method for
#  the left parentheisis
#Advance simply checks that the current token matches the id, and loads
# the next token into the currentToken
def advance(id=None):
    global curToken, tokenGenerator

    if id and curToken.id != id:
        raise SyntaxError("Expected %r" % id)
    curToken = next(tokenGenerator)  #get the next token


#---end advance


#Main call to the Pratt Parser;
def parse(program):
    global curToken, tokenGenerator

    tokenGenerator = tokenize(program)  #Build the token generator
    curToken = next(tokenGenerator)  #get the first token in 'program'
    return expression()  #parse the expression


#---end function


#expression parser: The bread and butter of Prat's approach
#   curToken is the current token (generated by the token function)
def expression(rbp=0):
    global curToken, tokenGenerator
    t = curToken
    curToken = next(tokenGenerator)
    left = t.nud()
    while rbp < curToken.lbp:
        t = curToken
        curToken = next(tokenGenerator)
        left = t.led(left)
    return left


#---end function

# \s* zero or more whitespace characters
#We have two groups in our regular expression: Group 1 or group 2
# Group 1: Get any floating point value 0.33, 1.9484, 5.4101
#   [0-9]*  zero or more digits 0 through 9
#   [.]?    zero or one decimal point
#   [0-9]+  one or more digits in the range 0-9   (e.g. '1.' is not legal)
# Group 2: Grab an operator
#   \*\*: The exponential operator '**'
#   or
#   . any single character (tokenizer will error-out on an unknown operator)
regEx = "\s*(?:([0-9]*[.]?[0-9]+)|(\*\*|.))"
tokenPattern = re.compile(regEx)


#itty bitty program to understand the regular expression
def testTokenize(program):
    print(tokenPattern.findall(program))


#---end function


def tokenize(program):
    #number and operator is handled by the tokenizer regular expression; run 'testTokenize'
    for number, operator in tokenPattern.findall(program):
        if number:
            symbol = symbolTable["(literal)"]
            s = symbol()
            s.value = number
            yield s
        else:
            symbol = symbolTable.get(operator)
            if not symbol:
                raise SyntaxError("Unknown operator")
            yield symbol()
    symbol = symbolTable["(end)"]
    yield symbol()


#---end function


#Used when evaluating a parse tree, getLiteral will return a float or an integer
def getLiteral(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            raise ValueError("Uknown Literal Value")


#---end function


#Evaluates a parse tree into a single value: Only works for
def evalParseTree(p):

    if p == None:  #A scenario of a unary operator e.g. -1, -(1+5), +(1-3)
        return 0
    elif p.id == "(literal)":
        return getLiteral(p.value)
    else:
        if p.id == '+':
            return evalParseTree(p.first) + evalParseTree(p.second)
        elif p.id == "-":
            return evalParseTree(p.first) - evalParseTree(p.second)
        elif p.id == "*":
            return evalParseTree(p.first) * evalParseTree(p.second)
        elif p.id == "/":
            return evalParseTree(p.first) / evalParseTree(p.second)
        elif p.id == "**":
            return evalParseTree(p.first)**evalParseTree(p.second)


#--end function
