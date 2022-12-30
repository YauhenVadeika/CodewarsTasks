# my task solution
class Ball(object):

    def __init__(self, type="regular"):
        self.ball_type = type


print(Ball().ball_type)
print(Ball("super").ball_type)


# codewars task best solution
class Ball(object):
    # your code goes here
    def __init__(self, balltype=None):
        if balltype == None:
            self.ball_type = "regular"
        else:
            self.ball_type = balltype


# codewars task best solution
class Ball:
    __init__ = lambda _, a=0: setattr(Ball, 'ball_type',
                                      ('regular', 'super')[bool(a)])


# codewars task best solution
class Ball(object):

    def __init__(self, type: str = 'regular'):
        self.ball_type = type

    @property
    def ball_type(self):
        return self._ball_type

    @ball_type.setter
    def ball_type(self, type: str):
        self._ball_type = type