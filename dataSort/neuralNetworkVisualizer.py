
import csv
from tkinter import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.pipeline import make_pipeline

### Sort Data
def getXList(sequence,n,numOfNums):
    currList= [0]*numOfNums
    nList=[]
    finalList=[]
    indicator=False
    for i in sequence:
        copy=i
        while len(i)>n:
            for j in copy:
                currList[int(j)-1]+=1
                for k in currList:
                    nList.append(k)
                currList= [0]*numOfNums
                if len(nList)==n*numOfNums:
                    finalList.append(nList)
                    copy= copy[1:]
                    break
                if len(copy)<=n+1:
                    indicator=True
            if indicator==True:
                break
            nList=[]
    return finalList
    
    
def getYList(sequence,n,numOfNums):
    yResult=[] 
    for i in sequence:
        yResult= i[n:]
    return yResult


def getFinalXList():
    finalXList=[]    
    for i in range(1, 49):
        a=""
        i=str(i)
        if len(i)== 1:
            a+=str(0) 
        a+=i
        with open('design_data_' + a + '.csv') as csvfile:
            objectSequence= csv.reader(csvfile, delimiter= ',')
            n=3
            numOfNums=7
            xList= getXList(objectSequence,n,numOfNums)
        for j in xList:
            finalXList.append(j)
        xList= []
    return finalXList

def getFinalYList():
    finalYList=[]    
    for i in range(1, 49):
        a=""
        i=str(i)
        if len(i)== 1:
            a+=str(0) 
        a+=i
        with open('design_data_' + a + '.csv') as csvfile:
            objectSequence= csv.reader(csvfile, delimiter= ',')
            n=3
            numOfNums=7
            yList= getYList(objectSequence,n,numOfNums)
        for j in yList:
            finalYList.append(j)
        yList= []
    return finalYList

### Train Neural Network

x,y=[],[]            
x= getFinalXList()
y= getFinalYList()
    
x_train, x_test, y_train, y_test= train_test_split(x,y)

scaler= StandardScaler()
scaler.fit(x_train)
x_train= scaler.transform(x_train)
x_test= scaler.transform(x_test)


mlp=MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
    beta_2=0.999, early_stopping=False, epsilon=1e-08,
    hidden_layer_sizes=(10,2), learning_rate='invscaling',
    learning_rate_init=0.01, max_iter=1000, momentum=0.9,
    nesterovs_momentum=True, power_t=0.5, random_state=1000,
    shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
    verbose=False, warm_start=False)
    
mlp.fit(x_train,y_train)
weights=mlp.coefs_

predictions= mlp.predict(x_test)

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))


##### Draw Module

def init(data):
    data.radius=15
    data.margin=20
    data.thisHeight= data.height-data.margin*2
    data.weights= weights
    data.numOfInputs=len(data.weights[0])
    data.hiddenLayer= mlp.hidden_layer_sizes
    data.numOfOutputs=1
    data.inputX=data.width/4
    data.outputX=data.width*3/4
    data.inOutWidth= data.outputX- data.inputX
    data.lineInfo=[]
    getNodes(data)
    getWeights(data)
    
def getWeights(data):
    for i in data.weights:
        for j in i:
            for k in j:
                if k<0:
                    data.color="blue"
                    data.lineWidth=abs(k)
                    data.lineInfo.append((data.color, data.lineWidth))
                else:
                    data.color="red"
                    data.lineWidth=abs(k)
                    data.lineInfo.append((data.color, data.lineWidth))
    
def getNodes(data):
    data.inputNodes=[]
    data.outputNodes=[]
    data.hiddenNodes=[]
    layerL=[]
    for i in range(1,data.numOfInputs+1):
        data.inputNodes.append((data.inputX, data.thisHeight*i/data.numOfInputs))
        
    for k in range(1,data.numOfOutputs+1):
        num=data.numOfOutputs
        if data.numOfOutputs==1:
            num=2
        data.outputNodes.append((data.outputX,data.thisHeight*k/num))
    
    if isinstance(data.hiddenLayer,int):
        data.hiddenLayer=[data.hiddenLayer]
        
    for j in range(len(data.hiddenLayer)):
        for l in range(1,data.hiddenLayer[j]+1):
            layerL.append((data.inputX+ data.inOutWidth*(j+1)/(len(data.hiddenLayer)+1),data.thisHeight*l/data.hiddenLayer[j])) 
        data.hiddenNodes.append(layerL)
        layerL=[]

def getBounds(data,cx,cy):
    x0= cx-data.radius
    y0= cy-data.radius
    x1= cx+data.radius
    y1= cy+data.radius
    return x0,y0,x1,y1

def drawNodes(canvas,data):
    for node in data.inputNodes:
        x0,y0,x1,y1= getBounds(data,node[0], node[1])
        canvas.create_oval(x0,y0,x1,y1,fill="blue")
        ind= data.inputNodes.index(node)
        canvas.create_text(node[0], node[1],text= ind+1)
        
    for i in data.outputNodes:
        x0,y0,x1,y1= getBounds(data,i[0], i[1])
        canvas.create_oval(x0,y0,x1,y1,fill="red")
        ind= data.outputNodes.index(i)
        canvas.create_text(i[0], i[1],text= ind+1)
    
    for j in data.hiddenNodes:
        for k in j:
            x0,y0,x1,y1= getBounds(data,k[0], k[1])
            canvas.create_oval(x0, y0, x1,y1 , fill="seashell3")
            ind= j.index(k)
            canvas.create_text(k[0], k[1],text= ind+1)

def drawLines(canvas,data):
    for m in data.lineInfo:
        for d in range(data.numOfInputs):
            data.color=m[0]
            data.lineWidth=m[1]
            for i in data.inputNodes:
                x0=i[0]
                y0=i[1]
                for j in data.hiddenNodes[0]:
                    x1=j[0]
                    y1=j[1]
                    print("a",data.color,data.lineWidth)
                    canvas.create_line(x0,y0,x1,y1,fill=data.color,width=data.lineWidth)
                    break
                break
        break
        # for e in range(len(data.hiddenLayer)):
        #     data.color=m[0]
        #     data.lineWidth=m[1]
        #     for c in range(len(data.hiddenNodes)):
        #         for a in data.hiddenNodes[c]:
        #             x0= m[0]
        #             y0=m[1]
        #             if c+1< len(data.hiddenNodes):
        #                 for b in  data.hiddenNodes[c+1]:
        #                     x1=b[0]
        #                     y1=b[1]
        #                     print("b",data.color,data.lineWidth)
        #                     canvas.create_line(x0,y0,x1,y1,fill=data.color,width=data.lineWidth)
        #     break
        # for f in range(data.numOfOutputs):
        #     data.color=m[0]
        #     data.lineWidth=m[1]
        #     for k in data.outputNodes:
        #         x0=k[0]
        #         y0=k[1]
        #         for l in data.hiddenNodes[-1]:
        #             x1=l[0]
        #             y1=l[1]
        #             print("c",data.color,data.lineWidth)
        #             canvas.create_line(x0,y0,x1,y1,fill=data.color,width=data.lineWidth)
    
    

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

def run(width=400, height=400):
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

run(800, 800)




















    