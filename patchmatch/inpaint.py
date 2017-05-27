from PIL import Image

class inpaint:
    def __init__(self):
        self.initial = MaskedImage()

        nnf_src2dest = NNF()
        nnf_dest2src = NNF()

        radius = 0

        pyramid = MaskedImage()

        nbEltPyramid = 0
        nbEltMaxPyramid = 0

#    def initNNF(MaskedImage input, MaskedImage output, int patchsize):
