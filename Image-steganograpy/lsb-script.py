#!/usr/bin/python3
from stegano import lsbset

from stegano.lsbset import generators

flag="The secret is hacktoberfest is awesome!"

lets=lsbset.hide("./image.png",flag,generators.eratosthenes())
#the secret hided steg.png has been created successfully
lets.save("steg.png")



#To Decrypty 

f=open("steg.png","rb")

lsbset.reveal(f,generators.eratosthenes())

'The secret is hacktoberfest is awesome!'
