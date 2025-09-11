from PIL import Image

def GetPic(Adress,Code):
    image = Image.open(Adress)
    SetCode(image,Code)

def AsciiTable(character):
    return ord(character)

def AsciiTableDecode(character):
    return chr(character)

def Decode(Adress):
    image = Image.open(Adress)
    for i in range(1,image.size[0],10):
        for j in range(1,image.size[1],10):          
            s = image.getpixel((i,j))
def SetCode(image,Code):
    for i in range(1,image.size[0],10):
        for j in range(1,image.size[1],10):
            if i < len(Code):
                image.putpixel((i,j),AsciiTable(Code[i]))
                
            
    image.show()

GetPic("D:\Erfan-Python\Python Erfan\Python 0 to 80\Project 1\MentalHealth1.jpeg","Erfan love you")
Decode("D:\Erfan-Python\Python Erfan\Python 0 to 80\Project 1\MentalHealth1.jpeg")
