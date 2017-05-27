from PIL import Image

class MaskedImage:
    def __init__(self):
      self.mask = [[]]
      self.image = Image.load()
      self.similarity = []
      self.isNew = 0

    def initSimilarity(self):
        i,j,k,lenght = 0,0,0,0
        base = [1.0, 0.99, 0.96, 0.83, 0.38, 0.11, 0.02, 0.005, 0.0006, 0.0001, 0 ]
        t, vj, vk = 0.0, 0.0, 0.0
        length = (DSCALE+1)

        G_globalSimilarity = [0]*length

        if(!G_initSim):
            for i in range(length):
                t = float(i/float(length))
                j = int(100*t)
                k = j+1
                vj, vk = 0, 0
                if j < 11: vj = base[j]
                if k < 11: vk = base[k]
                G_globalSimilarity[i] = vj + (100*t-j)*(vk-vj)

        G_initSim = 1

    def initSimilarity2(self,):
        i, length = 0, 0


    def initMaskedImage(self, mask):

        MaskedImage mIm = MasekdImage()

        mIm.mask = mask
        mIm.image = image

        initSimilarity()
        mIm.similarity = G_globalSimilarity

        mIm.isNew = 0

        return mIm

    def getSampleMaskedImage(x, y, band):
        return data[x*step+y]
