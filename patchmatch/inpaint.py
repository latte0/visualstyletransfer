from PIL import Image

class Inpaint:
    def __init__(self):
        self.initial = MaskedImage()

        nnf_src2dest = NNF()
        nnf_dest2src = NNF()

        radius = 0

        pyramid = MaskedImage()

        nbEltPyramid = 0
        nbEltMaxPyramid = 0

#    def initNNF(MaskedImage input, MaskedImage output, int patchsize):

# elt type maskedimage
    def addEltInpaintingPyramid(self, elt):
        inc = INCREASE_PYRAMID_SIZE_RATE

        if inc < 2:
            inc = 2

        if (self.pyramid == None || self.nbEltMaxPyramid == 0 ):
            self.nbEltMaxPyramid = inc
            self.pyramid = []
        else if (self.nbEltPyramid == self.nbEltMaxPyramid):
            self.nbEltMaxPyramid = self.nbEltMaxPyramid*inc

        self.pyramid[self.nbEltPyramid] = elt
        self.nbEltPyramid += 1

    def ExpectationMaximization(self, int level):
        emloop, x, y, H, W, i, j = 0, 0, 0, 0, 0, 0, 0

        vote = [[[]]]

        iterEM = 1+2*level
        iterNNF = int(min(7, 1 + level))

        upscaled = 0

        newsource = MaskedImage()
        source = self.nnf_src2dest.input
        target = self.nnf_dest2src.output
        newtarget = None

        Size size

        print("em loop " + iterEM + " " + iterNNF)

        for emloop in (1,iterEM):
            print(1 + iterEM-emloop)

            if newtarget is not None:
                self.nnf_src2dest.output = newtarget
                self.nnf_dest2src.input = newtarget

                target = newtarget
                newtarget = None:

            H = source.image.height
            W = source.image.width

            for x in range(H):
                for y in range(W):
                    if !


    def ExpectationStep(self, src2dest, vote, source, upscale):
        int y, x, H, W, Ho, Wo, xp, yp, dp, dy, dx
        int xs,ys,xt,yt
        int*** field = self.field
        int R = self.S # int R = self.PatchSize
        double w

        H = self.input.image.height
        W = self.input.image.width
        Ho = self.output.image.height
        Wo = self.output.image.width
        for y in ra:
            for ( y=0  y<W ++y):

                xp=field[x][y][0]
                yp=field[x][y][1]
                dp=field[x][y][2]

                w = G_globalSimilarity[dp]

                for dy in range(-R,R):
                    for dx in range(-R, R):

                        if (sourceToTarget):
                            xs=x+dx
                            ys=y+dy
                            xt=xp+dx
                            yt=yp+dy
                        else:
                            xs=xp+dx
                            ys=yp+dy
                            xt=x+dx
                            yt=y+dy

                        if (xs<0 or xs>=H): continue
                        if (ys<0 or ys>=W): continue
                        if (xt<0 or xt>=Ho): continue
                        if (yt<0 or yt>=Wo): continue

                        if (upscale):
                            weightedCopy(source, 2*xs,   2*ys,   vote, 2*xt,   2*yt,   w)
                            weightedCopy(source, 2*xs+1, 2*ys,   vote, 2*xt+1, 2*yt,   w)
                            weightedCopy(source, 2*xs,   2*ys+1, vote, 2*xt,   2*yt+1, w)
                            weightedCopy(source, 2*xs+1, 2*ys+1, vote, 2*xt+1, 2*yt+1, w)
                        else:
                            weightedCopy(source, xs, ys, vote, xt, yt, w)


    def weightedCopy(src, xs, ys, vote, xd, yd, w):
        if src.isMasked(xs,ys):
            return

        vote[xd][yd][0] += w*src.getSampleMaskedImage(xs, ys, 0)
        vote[xd][yd][1] += w*src.getSampleMaskedImage(xs, ys, 1)
        vote[xd][yd][2] += w*src.getSampleMaskedImage(xs, ys, 2)
        vote[xd][yd][3] += w

    def MaximizationStep(target, vote):

        x, y, H, W, r, g, b = 0, 0, 0, 0, 0, 0, 0

        H = target.image.height
        W = target.image.width

        for y in range(H):
            for x in range(W):

                if(vote[y][x][3] > 0):
                    r = int(vote[x][y][0]/vote[x][y][3])
                    g = int(vote[x][y][1]/vote[x][y][3]);
                    b = int(vote[x][y][2]/vote[x][y][3]);

                    target.setSampleMaskedImage(x, y, 0, r );
                    target.setSampleMaskedImage(x, y, 1, g );
                    target.setSampleMaskedImage(x, y, 2, b );
                    target.setMask(x, y, 0);

    def inpaint(self, input, mask, radius):
        level, x, y = 0, 0, 0
        new_nnf = NNF()
        new_nnf_rev = NNF()

        self.initial = input.initMaskedImage(mask)

        tmp = Image.load()

        source = sef.initial
        target = MaskedImage()

        addEltInpaintingPyramid(source)

        while source.image.width.radius and source.image.height.radius:
            source = downsample(source)
            addEltInpaintingPyramid(source)

        maxlevel = imp.nbEltPyramid

        for level in range(maxlevel-1, 0, -1):

            source = self.pyramid[level]

            if (level == maxlevel-1):
                target = source.copy()

                for y in range (target.image.height):
                    for x in range(target.image.width):
                        setMask(target, x, y 0)
