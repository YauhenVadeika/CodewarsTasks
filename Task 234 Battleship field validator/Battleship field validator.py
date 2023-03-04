# my task solution


def get_size(m, r, c, h, w):
    if c < w and ((r > 0 and m[r - 1][c + 1]) or
                  (r < h and
                   ((m[r + 1][c] and m[r][c + 1]) or m[r + 1][c + 1]))):
        return -1
    if r < h and m[r + 1][c] == 1:
        return 1 + get_size(m, r + 1, c, h, w)
    if c < w and m[r][c + 1] == 1:
        return 1 + get_size(m, r, c + 1, h, w)
    return 1


def validate_battlefield(m):
    s = {i: 0 for i in range(5)}
    h, w = len(m) - 1, len(m[0]) - 1
    for row in range(h + 1):
        for col in range(w + 1):
            if (m[row][col] and not (row > 0 and m[row - 1][col])
                    and not (col > 0 and m[row][col - 1])):
                size = get_size(m, row, col, h, w)
                s[size] = s.get(size, 0) + 1
    return all(s[i] == 5 - i for i in range(1, 5))


print(
    validate_battlefield([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                          [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

# codewars task best solution
from scipy.ndimage.measurements import label, find_objects, np


def validate_battlefield(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos]
                     for pos in find_objects(label(field, np.ones((
                         3, 3)))[0]))) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


# codewars task best solution
def validateBattlefield(field):

    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in field]))

    ships = []

    #this algorithm uses the field 2-dimensional array it self to store infomration about the size of ships found
    for i in range(0, 10):
        for j in range(0, 10):
            #if not at end of any edge in 2d-array, check that sum of two cross diagonal elements is not more than max
            #if it is then two ships are two close
            if j < 9 and i < 9:
                if field[i][j] + field[i + 1][j + 1] > max(
                        field[i][j], field[i + 1][j + 1]):
                    return False
                if field[i + 1][j] + field[i][j + 1] > max(
                        field[i + 1][j], field[i][j + 1]):
                    return False
            #if the element at position (i, j) is occupied then add the current value of position to next
            if j < 9 and field[i][j] > 0 and field[i][j + 1] > 0:
                field[i][j + 1] += field[i][j]
            elif i < 9 and field[i][j] > 0 and field[i + 1][j] > 0:
                field[i + 1][j] += field[i][j]
            elif field[i][j] > 0:
                ships.append(field[i][j])  #since we add numbers

    ships.sort()

    return ships == [
        1, 1, 1, 1, 2, 2, 2, 3, 3, 4
    ]  #if the ships we have found are of correct configuration then it will equal this array


# codewars task best solution
#Battleship Validator:
#  Approach: Use a breadth-first-search algorithm to search out the ships on the gameboard,
#            recording their (x,y) locations as tuples. Ship connections are allowed in all
#            eight directions N, NE, ... W, NW.  Board is then validated for the correct number
#            number of ships, and their sizes (corresponding to number of tuples), and lastly
#            whether the ships are in straight lines.
from copy import deepcopy
import queue


#Small lookup for literal values associated to the game
class BattleShipSymbols():
    IS_SHIP = 1
    IS_WATER = 0

    NUM_BATTLESHIP = 1
    NUM_CRUISER = 2
    NUM_DESTROYER = 3
    NUM_SUBMARINE = 4

    SIZE_BATTLESHIP = 4
    SIZE_CRUISER = 3
    SIZE_DESTROYER = 2
    SIZE_SUBMARINE = 1

    #provides an empty manefest of legal ship sizes
    @staticmethod
    def getEmptyManifest(self):
        return {
            self.SIZE_BATTLESHIP: 0,
            self.SIZE_CRUISER: 0,
            self.SIZE_DESTROYER: 0,
            self.SIZE_SUBMARINE: 0
        }

    #Provides a valid ship manefest (of sizes and number) for
    # comparison (validation) purposes
    @staticmethod
    def getValidManifest(self):
        return {
            self.SIZE_BATTLESHIP: self.NUM_BATTLESHIP,
            self.SIZE_CRUISER: self.NUM_CRUISER,
            self.SIZE_DESTROYER: self.NUM_DESTROYER,
            self.SIZE_SUBMARINE: self.NUM_SUBMARINE
        }


#--end class


class BattleShip(object):

    #Entire code-flow of this class is in the constructor
    def __init__(self, gameBoard):
        self.board = deepcopy(gameBoard)
        self.shipLocations = []

        #Can Update: Gameboard does not need to be square; simply update storeShipPieces
        numRows = len(self.board[:])
        numCols = len(self.board[0][:])

        if numRows != numCols:
            self.passesValidation = False
        else:
            self.boardSize = numRows
            self.__storeShipPieces__()
            self.passesValidation = self.__validateBoard__()

    #---end constructor

    def isValidBoard(self):
        return self.passesValidation

    #---end function

    #Precondition: Ships pieces must be stored
    # WLOG first check whether there are a correct number of ships of the correct size,
    # then check if the ships are all straight lines
    def __validateBoard__(self):
        validBoard = True
        validNumPieces = self.__validateNumberPieces__()

        if validNumPieces:
            validShapeSizes = self.__validateShipShapes__()
            validBoard = (validNumPieces and validShapeSizes)
        else:
            validBoard = False

        return validBoard

    #---end function

    #Precondition: Ships pieces must be stored
    # Checks the number of pieces, and their size
    def __validateNumberPieces__(self):
        passesValidation = True
        shipManifest = BattleShipSymbols.getEmptyManifest(BattleShipSymbols)

        #Build the manefest for the provided game board
        for ship in self.shipLocations:
            sizeShip = len(ship)
            if sizeShip not in shipManifest:
                hasValidNumPieces = False
                break
            shipManifest[sizeShip] += 1

        #Compare the built manefest to the true (and valid) manefest
        hasValidNumPieces = (shipManifest == BattleShipSymbols.
                             getValidManifest(BattleShipSymbols))

        return hasValidNumPieces

    #---end function

    #All ships must be in straight lines, therefore for every tile, x must be constant
    #  or y must be constant
    def __validateShipShapes__(self):

        hasValidShipShapes = True

        for ship in self.shipLocations:
            if len(ship) == 1:
                continue
            if not hasValidShipShapes:
                break

            #Post: Ship is built out of atleast two tiles
            shipXTileFirst = ship[0][0]
            shipYTileFirst = ship[0][1]
            constXTile, constYTile = True, True
            for tile in ship:
                curXTile, curYTile = tile[0], tile[1]
                constXTile &= (shipXTileFirst == curXTile)
                constYTile &= (shipYTileFirst == curYTile)
                hasValidShipShapes = (constXTile or constYTile)
                if not hasValidShipShapes:
                    break

        return hasValidShipShapes

    #---end function

    #Precondition: None (constructor called)
    #Postcondition: Each ship's coordinates have been stored as a list of (x,y) points
    def __storeShipPieces__(self):
        n = self.boardSize
        hasVisited = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if not hasVisited[i][j]:
                    rowSeed = i
                    colSeed = j
                    shipCordinates = self.__getConnectedShape__(
                        self.board, hasVisited, n, n, rowSeed, colSeed)
                    if shipCordinates:
                        self.shipLocations.append(shipCordinates)

    #---end function

    #part of the logic to find all connected shapes
    def __inImage__(self, i, j, nR, nC):
        if 0 <= i and i < nR and 0 <= j and j < nC:
            return True
        else:
            return False

    #-----end function

    #part of the logic to find all connected shapes
    #  A desired cell is one that is a ship symbol and has not been visited yet
    def __isDesiredCell__(self, img, hasVisited, i, j):
        if img[i][j] == BattleShipSymbols.IS_SHIP and not hasVisited[i][j]:
            return True
        else:
            return False

    #---end function

    #part of the logic to find all connected shapes
    def __markCellAsVisited__(self, hasVisited, i, j):
        hasVisited[i][j] = True

    #end function

    #We allow connections to be along diagonals; this way the game will not pass
    # validation if pieces are conneceted diagonally
    def __getConnectedShape__(self, img, hasVisited, nR, nC, iRoot, jRoot):
        #dx and dy specify the directions we are going to search dx=0 dy=1 means
        #search north (one cell above), dx=1 dy=-1 is one to right and one down
        dx = [0, 0, 1, 1, 1, -1, -1, -1]
        dy = [1, -1, 0, 1, -1, 0, 1, -1]
        numSearchDirs = len(dx)

        #x,y are lists that are going to hold the nodes conneced to the provided root (i,j)
        xConnected = []
        yConnected = []
        q = queue.Queue()

        #if provided root is desired, save it
        if self.__isDesiredCell__(img, hasVisited, iRoot, jRoot):
            q.put((iRoot, jRoot))
            self.__markCellAsVisited__(hasVisited, iRoot, jRoot)

        #Now we search for connections allong the allowed (eight) directions
        while q.empty() == False:

            u, v = q.get()
            xConnected.append(u)
            yConnected.append(v)

            # from the original root (i,j) provided by the function call, we are going to search
            # in eight directions (NSEW and NE, NW, SE, SW).
            for s in range(numSearchDirs):
                xNew = u + dx[s]
                yNew = v + dy[s]
                #if we're in the image and found a desired cell, add it to the queue
                if self.__inImage__(xNew, yNew, nR,
                                    nC) and self.__isDesiredCell__(
                                        img, hasVisited, xNew, yNew):
                    self.__markCellAsVisited__(hasVisited, xNew, yNew)
                    q.put((xNew, yNew))

        return list(zip(xConnected, yConnected))

    #---end function


#---end Battleship Class


#Driver to call the battleship class, which performs the validation in the constructor
def validate_battlefield(field):

    b = BattleShip(field)

    return b.isValidBoard()


#--end function

# codewars task best solution
from collections import Counter

MOVES = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
VALID = {4: 1, 3: 2, 2: 3, 1: 4}


def validateBattlefield(field):
    return sum(map(sum, field)) == 20 and Counter(flood(list(map(
        list, field)))) == VALID


def flood(field, x=0, y=0):
    while x < 10 and not field[x][y]:
        x, y = divmod(10 * x + y + 1, 10)
    if x < 10:
        bag, found = {(x, y)}, set()
        while bag:
            found |= bag
            for a, b in bag:
                field[a][b] = 0
            bag = {
                (a + dx, b + dy)
                for a, b in bag for dx, dy in MOVES
                if 0 <= a + dx < 10 and 0 <= b + dy < 10 and field[a + dx][b +
                                                                           dy]
            }
        valid = 1 in {len(set(dim)) for dim in zip(*found)} and len(found)
        yield valid
        if valid: yield from flood(field, x, y)


# codewars task best solution
def validate_battlefield(field):
    for i in range(10):
        for j in range(10):
            if field[i][j]:
                field[i][j] = sum(1 for x in range(max(i - 1, 0),
                                                   min(i + 1, 9) + 1)
                                  for y in range(max(j - 1, 0),
                                                 min(j + 1, 9) + 1)
                                  if field[x][y])
    return sum(sum(row) for row in field) == 40


# codewars task best solution
def create_pattern(ship_size):
    return [[0] * (ship_size + 2), [0] + [1] * ship_size + [0],
            [0] * (ship_size + 2)]


def validateBattlefield(field):
    # quick check: occupied cells == 20?
    if sum(sum(field, [])) != 20:
        return False

    # add border around field
    field = [[0] * 10] + field + [[0] * 10]
    for i, row in enumerate(field):
        field[i] = [0] + row + [0]

    # create a rotated version of the field
    rotated_field = [list(row) for row in zip(*field)]

    ship_counter = {1: 0, 2: 0, 3: 0, 4: 0}

    # look for ships
    for ship_size in range(1, 4 + 1):
        pattern = create_pattern(ship_size)
        width = ship_size + 2

        # pattern recognition
        for row in range(10):
            for col in range(13 - width):
                # look for ship horizontally
                sub_field_horizontal = [
                    field[row + i][col:col + width] for i in range(3)
                ]
                if pattern == sub_field_horizontal:
                    ship_counter[ship_size] += 1

                # look for ship vertically (except submarines)
                sub_field_vertical = [
                    rotated_field[row + i][col:col + width] for i in range(3)
                ]
                if ship_size > 1 and pattern == sub_field_vertical:
                    ship_counter[ship_size] += 1

    return ship_counter == {1: 4, 2: 3, 3: 2, 4: 1}