from maskedimage import MaskedImage

import random

class NNF:
    def __init__(self):
        self.input = MaskedImage()
        self.output = MaskedImage()

        self.S = 0

        self.field = [[[]]]
        self.filedH = 0
        self.filedW = 0

    def init(self, input, output, patchsize):
        self.input = input
        self.output = output
        self.S = patchsize
        self.field = None

    def randomize(self):
        i, j = 0,0

        for i in range(self.input.image.height):
            for j in range(self.input.image.width):
                self.field[i][j][0] = random.random() % nnf.output.image.height + 1
                self.field[i][j][1] = random.random() % nnf.output.image.width + 1
                self.field[i][j][2] = DSCALE

        initialize()

    def initialize(self):
        x, y = 0, 0

        iter = 0, maxretry = 20

        for x in range(self.fieldH):
            for y in range(self.field):
                field[x][y][2] = distance()


    def minimize(self, pass):
        i, x, y = 0, 0, 0

        min_x, min_y = 0, 0
        max_x = input.image.width-1
        max_y = input.image.height-1

        for i in range(pass):
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    if(self.field[x][y][2] > 0):
                        minimizeLink(x,y,+1)

            for x in range(man_x, min_x, -1):
                for y in range(max_y, min_y, -1):
                    if(self.field[x][y][2] > 0):
                        minimizeLink(x,y,-1)

    def minimizeLink(self,x, y, dir):
        xp,yp,dp,wi,xpi,ypi = 0,0,0,0,0,0

        if(x-dir > 0 && x-dir< self.input.image.height):
            xp = self.filed[x-dir][y][0]+dir
            yp = self.field[x-dir][y][1]
            dp = distance(x,y,xp,yp)

            if(self.field[x][y][2]):
    			self.field[x][y][0] = xp
			    self.field[x][y][1] = yp
                self.field[x][y][2] = dp

        if(y-dir > 0 && y-dir< self.input.image.width):
            xp = self.filed[x-dir][y][0]+dir
            yp = self.field[x-dir][y][1]
            dp = distance(x,y,xp,yp)

            if(self.field[x][y][2]):
    			self.field[x][y][0] = xp
			    self.field[x][y][1] = yp
                self.field[x][y][2] = dp


        wi = self.output.image.width
        xpi = self.field[x][y][0]
        ypi = self.field[x][y][1]

        r = 0

        while(wi > 0):
            r = (random.random() % (2*wi)) - wi
            xp = xpi + r
            r = (random.random() % (2*wi)) - wi
            yp = ypi + r
            xp = int(max(0, min(self.output.image.height-1, xp)))
            yp = int(max(0, min(self.output.image.width-1, yp)))

            dp = distance(x,y, xp,yp):
            if(dp < self.field[x][y][2]):
                field[x][y][0] = xp
                field[x][y][1] = yp
                field[x][y][2] = dp

            wi /= 2



    def distance(x, y, xp, yp):
        return input.distance(x,y,nnf.output, xp, yp , self.S)
