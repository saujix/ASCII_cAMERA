import cv2
import time
import os
import os
import platform
import shutil


oS = platform.system()

# must provide camera permission to terminal

# uhmm ackchually we need to chek the osh, yeshh
if oS == "Darwin":
    com = 'clear'
elif oS == "Windows":  
    com= 'cls'
else:
    com = 'clear'

# uhmm ackchually we need to chek the terminal size, yeshh
columns, rows = shutil.get_terminal_size()


asciiChar = "  .`',:;   " # darker -> lighter

cam = cv2.VideoCapture(0)


# the magik
def conversion():

    frame = cam.read()[1]

    grayFrame = cv2.flip(cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY),1)
        
    resultAscii = ""

    columns, rows = shutil.get_terminal_size()

    rows = int(columns * (0.27))
    grayFrame = cv2.resize(grayFrame , (columns, rows))

    # iterating through all the pixels, converting them into the ascii character based on their brightness, merging into a line -
    # - adding that line to the next line of the resultAscii variable -
    # - this makes 1 frame , doing it infinite number of times till the user press ctrl + c to break the loop
    
    for row in grayFrame:

        lineChar = ""
        medianBrightness = []

        for pixelValue in row:
            
            # break the 255 into the len of the asciilength
            blockLen = 255/len(asciiChar)

            #looking in which range it lies
            range = int(pixelValue/blockLen)

            # putting the character in place of the pixel num
            char = asciiChar[int(range) - 1]
            
            # making an array for all the pixel (for median brightness)
            medianBrightness.append(pixelValue)
            
            lineChar += char

        resultAscii +=  lineChar + "\n"
    
    middlePoint = len(medianBrightness) // 2
    os.system(com)
    
    # sorting (for median)
    medianBrightness.sort()
    
    print(resultAscii)
    
    print(f"""
        Columns: {columns}, Rows: {rows}
        More colums, better picture quality
        Median Brightness : {int((medianBrightness[middlePoint]/255)*100)}%
        """)
    

if __name__ == "__main__":
    Status = True
    while Status:
        conversion()
        print("     Press Ctrl + C to exit")
