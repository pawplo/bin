def q_rgb(im, xx, yy, zz):
    for i in range((int)(im.width/xx)):
        for j in range((int)(im.height/xx)):
            r = 0
            g = 0
            b = 0
#            a = 0
            for ii in range(xx):
                for jj in range(xx):
                    r = r + (im.getpixel((i*xx+ii,j*xx+jj))[0])
                    g = g + (im.getpixel((i*xx+ii,j*xx+jj))[1])
                    b = b + (im.getpixel((i*xx+ii,j*xx+jj))[2])
#                    a = a + (im.getpixel((i*xx+ii,j*xx+jj))[3])
            r = r + zz
            g = g + zz
            b = b + zz
            for ii in range(xx):
                for jj in range(xx):
#                    im.putpixel( (i*xx+ii,j*xx+jj), ((int)(r/(xx*xx)), (int)(b/(xx*xx)), (int)(g/(xx*xx)), (int)(a/(xx*xx))) )
                    im.putpixel( (i*xx+ii,j*xx+jj), ( (int)(r/(xx*xx)) - ((int)(r/(xx*xx)) % yy), (int)(b/(xx*xx)) - ((int)(b/(xx*xx)) % yy), (int)(g/(xx*xx)) - ((int)(g/(xx*xx)) % yy ) ) )
