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

asciiChar = "  .:-=+*#%@"  # Lighter → Darker
# asciiChar = "@%#*+=-:. "

location = "inputs/skrillex.webp"

pic = cv2.imread(location)

# the magik
def conversion():

    grayFrame = cv2.cvtColor(pic , cv2.COLOR_BGR2GRAY)
        
    resultAscii = ""

    columns, rows = shutil.get_terminal_size()

    rows = int(columns * (0.27))
    grayFrame = cv2.resize(grayFrame , (columns, rows))

    # iterating through all the pixels, converting them into the ascii character based on their brightness, merging into a line -
    # - adding that line to the next line of the resultAscii variable -
    # - this makes 1 frame , doing it infinite number of times till the user press ctrl + c to break the loop
    
    for row in grayFrame:

        lineChar = ""

        for pixelValue in row:
            
            # break the 255 into the len of the asciilength
            blockLen = 255/len(asciiChar)

            #looking in which range it lies
            range = int(pixelValue/blockLen)

            # putting the character in place of the pixel num
            char = asciiChar[int(range) - 1]
            
            
            lineChar += char

        resultAscii +=  lineChar + "\n"
    
    os.system(com)
    
    
    return resultAscii
    
    

if __name__ == "__main__":
    
    text = conversion()
    
    try: # if file already exists, i know some aholes will run it more than once, in that case it wont append, it will erase first and then write
        with open(f'outputs/{location.split("/")[-1].split(".")[0]}.txt','r+') as file:
            file.write("")
            for line in text:
                file.write(line)
    except:
        with open(f'outputs/{location.split("/")[-1].split(".")[0]}.txt','r+') as file:
            for line in text:
                file.write(line)
                
    print(f"Conversion Done! save at outputs/{location.split("/")[-1].split(".")[0]}.txt ")
        