# Import face, eye, mouse, nose to create stick faces
from genOneFace import *
from PIL import Image
from createGaussianNumbers import *
import os


def getNumFaces(num, *pars):
    assert len(pars) == 11
    for i in range(num):
        screen = setEnv()
        oneFace(*pars)
        saveImgAndConvert(i, screen)


def getNumFacesWithVar(num, *pars):
    assert len(pars) == 11
    var = g(num)
    for i in range(num):
        screen = setEnv()
        newpar = list(pars)
        intVar = [j+var[i] for j in newpar[:-2]]
        facer, eyer1, eyer2, eyep1, eyep2, noser, nosep1, nosep2, mouser  = intVar
        bigCol, smallCol = newpar[-2:]
        oneFace(facer, eyer1, eyer2, eyep1, eyep2, noser, nosep1, nosep2, mouser, bigCol, smallCol)
        saveImgAndConvert(i, screen)


if __name__ == "__main__":
    getNumFacesWithVar(10, 64, 8, 4, -25, 32, 8, 0, 0, 12, 'white', 'black')
    #Parameter Notice