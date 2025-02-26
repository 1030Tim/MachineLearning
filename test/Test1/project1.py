import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import data save data
url = "/Users/juhn/Desktop/stady_file/MachineLearning/test/Test1/Study_Hourse_and_Scorse.csv"
data = pd.read_csv(url)
x = data["Study_Hours"]
y = data["Scores"]
# cost function
def cost_function(y,w,x,b):
    y_pred = w*x+b
    cost = ((y-y_pred)**2).mean()
    return cost
def compute_gradient(y,w,x,b):
    w_gradient = (x*(w*x+b -y)).mean()
    b_gradient = (w*x+b -y).mean()
    return w_gradient,b_gradient
# gradient_descent
def Gradient_Descent(w_init,b_init,count,learning_rate):
    
    w = w_init
    b = b_init
    w_hist = [ ]
    b_hist = [ ]
    c_hist = [ ]

    for i in range(count):
        w_gradient,b_gradient = compute_gradient(y,w,x,b)
        w = w - w_gradient*learning_rate
        b = b - b_gradient*learning_rate
        cost = cost_function(y,w,x,b)
        w_hist.append(w)
        b_hist.append(b)
        c_hist.append(cost)

        if (i%1000 == 0):
            print(f"Interation {i:4} Cost {cost:.2f}")

    return  w,b,w_hist,b_hist,c_hist
    
w_init = -100
b_init = -100
count = 60000
learning_rate = 1.0e-3
w_final,b_final,w_hist,b_hist,c_hist = Gradient_Descent(w_init,b_init,count,learning_rate)

def vive():
    ws = np.arange(-100,101)
    bs = np.arange(-100,101)
    costs = np.zeros((201,201))
    i = 0
    for w in ws:
        j = 0
        for b in bs:
            cost = cost_function(y,w,x,b)
            costs[i,j] = cost
            j+=1
        i+=1
    w_grid,b_grid = np.meshgrid(ws,bs)
    ax = plt.axes(projection="3d")
    ax.view_init(45, 45)
    ax.plot_surface(w_grid,b_grid,costs,alpha=0.5)
    w_index,b_index = np.where(costs==np.min(costs))
    ax.scatter(ws[w_index],bs[b_index],costs[w_index,b_index],color="red")
    ax.scatter(w_hist[0],b_hist[0],c_hist[0],color="green")
    for i in range(len(w_hist)):
        if(i%10 == 0):
            ax.scatter(w_hist[i], b_hist[i], c_hist[i], color="blue", s=10)
    ax.plot(w_hist, b_hist, c_hist)
    plt.savefig("plot.png", dpi=300)
    plt.show()

def plot_1d(y,x,w_final,b_final):
    plt.scatter(x,y,edgecolors="black",color="blue",linewidths=2,label = "Study_Hours")
    y_pred = w_final*x+b_final
    plt.plot(x,y_pred,color="red",label="Scores")
    plt.xlabel("Study_Hours")
    plt.ylabel("Scores")
    plt.title("Study_Hours VS Scores")
    plt.savefig("plot.png",dpi=300)
    plt.legend()
    plt.show()
plot_1d(y,x,w_final,b_final)