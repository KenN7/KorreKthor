import Pi_funct as fun
from time import sleep


def pdf_ok(): #goes left
    print("PDF_ok")
    fun.bCenter()
    fun.aDown()
    fun.valveON()
    fun.aUp()
    fun.bLeft()
    fun.aDown()
    fun.valveOFF()
    fun.aUp()

def pdf_nok(): #goes right
    print("PDF_nok")
    fun.bCenter()
    fun.aDown()
    fun.valveON()
    fun.aUp()
    fun.bRight()
    fun.aDown()
    fun.valveOFF()
    fun.aUp()


sleep(3)
fun.takePic()
sleep(1)
print("Photo")
goodPage = fun.isGoodPage("/home/pi/Desktop/img/image.PNG")
print("hi")
if goodPage :
    print("PDF okay")
    pdf_ok() #Goes LEFT
    print("Am I left ?")
    fun.uploadPic()
    
else:
    print("Is not our pdf file")
    pdf_nok() #Goes RIGHT