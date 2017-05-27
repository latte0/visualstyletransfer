from PIL import Image
from Size import Size

def PSNR(original, distorted):
    sumR,sumG,sumB,sumRGB = 0.0, 0.0, 0.0, 0.0
    psnr = 0.0
    EQM = 0.0

    size = Size(original.size)

    h = size.height;
    w = size.width

#    for i in range(h):
#        for j in range(j):

    sumRGB = sumR + sumG + sumb
    EQM = sumRGB / (3*h*w)
#    psnr = 10.0 * log


    return psnr



def SSIM(original, distorted):
    C1 = 6.00210
    C2 = 108.102210
    SSIM = 0.0
