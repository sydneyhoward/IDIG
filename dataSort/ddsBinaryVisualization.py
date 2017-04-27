
from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.radius=15
    data.margin=20
    data.thisHeight= data.height-data.margin*2
    data.numOfInputs=7
    data.numHiddenNodes=20 
    data.numOfOutputs=1
    getNodes(data)

def getNodes(data):
    data.inputNodes=[]
    data.outputNodes=[]
    data.hiddenNodes=[]
    for i in range(1,data.numOfInputs+1):
        data.inputNodes.append((data.width/4, data.thisHeight*i/data.numOfInputs))
    for k in range(1,data.numOfOutputs+1):
        num=data.numOfOutputs
        if data.numOfOutputs==1:
            num=2
        data.outputNodes.append((data.width*3/4,data.thisHeight*k/num))
    for j in range(1,data.numHiddenNodes+1):
        data.hiddenNodes.append((data.width/2,data.thisHeight*j/data.numHiddenNodes))

def getBounds(data,cx,cy):
    x0= cx-data.radius
    y0= cy-data.radius
    x1= cx+data.radius
    y1= cy+data.radius
    return x0,y0,x1,y1

def drawNodes(canvas,data):
    for node in data.inputNodes:
        x0,y0,x1,y1= getBounds(data,node[0], node[1])
        canvas.create_oval(x0,y0,x1,y1,fill="light slate blue")
        ind= data.inputNodes.index(node)
        canvas.create_text(node[0], node[1],text= ind+1)
        
    for i in data.outputNodes:
        x0,y0,x1,y1= getBounds(data,i[0], i[1])
        canvas.create_oval(x0,y0,x1,y1,fill="midnight blue")
        ind= data.outputNodes.index(i)
        canvas.create_text(i[0], i[1],text= ind+1)
    
    for j in data.hiddenNodes:
        x0,y0,x1,y1= getBounds(data,j[0], j[1])
        canvas.create_oval(x0, y0, x1,y1 , fill="slate blue")
        ind= data.hiddenNodes.index(j)
        canvas.create_text(j[0], j[1],text= ind+1)

def drawLines(canvas,data):
    for i in data.inputNodes:
        x0=i[0]
        y0=i[1]
        for j in data.hiddenNodes:
            x1=j[0]
            y1=j[1]
            canvas.create_line(x0,y0,x1,y1,fill="medium slate blue")
    for k in data.outputNodes:
        x0=k[0]
        y0=k[1]
        for l in data.hiddenNodes:
            x1=l[0]
            y1=l[1]
            canvas.create_line(x0,y0,x1,y1,fill="dark slate blue")
    
    

def redrawAll(canvas, data):
    drawLines(canvas,data)
    drawNodes(canvas,data)
    
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 800)

