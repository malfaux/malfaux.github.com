#!/usr/bin/python

import Image, ImageDraw
import aggdraw
from math import sqrt,pow
greypen = aggdraw.Pen("grey",0.5)
whitepen = aggdraw.Pen("white",0.5)
greybrush = aggdraw.Brush("grey")
whitebrush = aggdraw.Brush("white")

#img = Image.new("RGBA",(128,128))
drw = aggdraw.Draw("RGBA",(128,128),"white")
drw.setantialias(True)
#drw.rectangle((0,0,128,128),whitepen,whitebrush)
drw.ellipse((0,0,128,128),greypen,whitebrush)
drw.pieslice((0,0,128,128),180,0,greypen,greybrush)
#drw.pieslice((0,64,128,64),0,180,greypen, greybrush)
drw.ellipse((0,32,64,96),whitepen,whitebrush)
drw.pieslice((0,0,128,128),0,30,greypen,greybrush)
drw.polygon([64,32,64,64,int(sqrt(pow(64,2)-pow(32,2)))+64,32], greypen,greybrush)
drw.rectangle((28,44,36,52),greypen,greybrush)
drw.ellipse((92,44,100,52),whitepen,whitebrush)
Image.fromstring('RGBA',(128,128),drw.tostring()).save('/tmp/bbx.jpg')
#drw.flush().save('/tmp/bbx.jpg');
#with open('/tmp/bbx.jpg','wb') as fh:
#	fh.write(drw.tostring())
#drw.rectangle((64,32,128,64),outline="#000",fill="#000")
#img.save('/tmp/bbx.jpg');
