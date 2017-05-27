from PIL import Image

class MaskedImage:
    def __init__(self):
      self.mask = [[[]]]
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

    def initSimilarity2(self):
        i, length = 0, 0


    def initMaskedImage(self, mask):

        MaskedImage mIm = MasekdImage()

        mIm.mask = mask
        mIm.image = image

        initSimilarity()
        mIm.similarity = G_globalSimilarity

        mIm.isNew = 0

        return mIm

    def isMasked(self, x, y):
        if mIm == None or mIm.mask == None:
            return 0
        return mim.mask[x][y]

    def setMask(self, x, y, value):
        if mIm == None or mIm.mask == None:
            return
## what does it mean?
##        mIm.mask[x][y]=0 < value

    def distance(self, xs, ys, target, xt, yt, S):
        distance = 0
        wsum = 0
        ssdmax  =9*255*255
        dy, dx, band = 0, 0, 0
        xks, yks = 0, 0
        xkt, ykt = 0, 0
        ssd = 0.0
        res = 0.0
        s_value, t_value, s_gx, t_gx, s_gy, t_gy = 0, 0, 0, 0, 0, 0

        for dy in range(-S, S):
            for dx in range(-S, S):
                xks = xs+dx
    			yks = ys+dy
    			xkt=xt+dx
    			ykt=yt+dy
    			wsum += 1

    			if ( xks<1 || xks>=source.image.height-1 ):
                    distance += 1
                    continue
    			if ( yks<1 || yks>=source.image.width-1 ):
                    distance += 1
                    continue

                if isMasked(xks, yks):
                    distance += 1
                    continue

    			if (xkt<1 or xkt>=target.image.height-1):
                    distance++
                    continue
    			if (ykt<1 or ykt>=target.image.width-1):
                    distance++
                    continue

			    if target.isMasked(xkt, ykt):
                    distance++
                    continue


    			ssd=0
                for (band=0 band<3 ++band):

    				s_value = getSampleMaskedImage(source, xks, yks, band)
    				t_value = getSampleMaskedImage(source, xkt, ykt, band)

    				s_gx = 128+(getSampleMaskedImage(source, xks+1, yks, band) - getSampleMaskedImage(source, xks-1, yks, band))/2
    				t_gx = 128+(getSampleMaskedImage(target, xkt+1, ykt, band) - getSampleMaskedImage(target, xkt-1, ykt, band))/2

    				s_gy = 128+(getSampleMaskedImage(source, xks, yks+1, band) - getSampleMaskedImage(source, xks, yks-1, band))/2
    				t_gy = 128+(getSampleMaskedImage(target, xkt, ykt+1, band) - getSampleMaskedImage(target, xkt, ykt-1, band))/2

    				ssd = ssd + pow(float(s_value-t_value) , 2) // distance between values in [0,255^2]
    				ssd = ssd + pow(float(s_gx-t_gx) , 2) // distance between Gx in [0,255^2]
    				ssd = ssd + pow(float(s_gy-t_gy) , 2) // distance between Gy in [0,255^2]

                distance += ssd/ssdmax

    	res = int(DSCALE*distance/wsum)
    	if (res < 0 or res > DSCALE) return DSCALE
    	return res


    def getSampleMaskedImage(self, x, y, band):
        return data[x][y]

    def upscale(self, newW, nweH):
        x, y = 0, 0
        xs, ys = 0, 0
        H, W = 0, 0
        H= sdop
