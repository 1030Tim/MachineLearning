import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
df = pd.read_csv("/Users/juhn/Desktop/stady_file/MachineLearning/test/tests/Salary_Data.csv")
x = df["YearsExperience"]
y = df["Salary"]
#plt.scatter(x,y,edgecolors="black",color = "blue",linewidths=2)
#cost function
def cost_function(y,w,x,b)->int:
    y_pred = w*x+b
    cost = ((y-y_pred)**2).mean()
    return cost
def compute_cost(y,w,x,b)->int:
    w_gradient = (x*(w*x+b - y)).mean()
    b_gradient = (w*x+b -y).mean()
    return w_gradient,b_gradient
def gradient_descent(w_init,b_init,count,learning_rate):
    w = w_init
    b = b_init
    w_hist = [ ]
    b_hist = [ ]
    c_hist = [ ]

    for i in range(count):
        w_gradient,b_gradient = compute_cost(y,w,x,b)
        w = w-w_gradient*learning_rate
        b = b-b_gradient*learning_rate
        cost = cost_function(y,w,x,b)
        
        w_hist.append(w)
        b_hist.append(b)
        c_hist.append(cost)

        if (i%1000 == 0):
            print(f"Interation {i:5} Cost {cost:.2f}")
    return w,b,w_hist,b_hist,c_hist

w_init = 0
b_init = 0
learning_rate = 1.0e-3
count = 20000
w_final,b_final,w_hist,b_hist,c_hist = gradient_descent(w_init,b_init,count,learning_rate)

# 視覺化圖形
def viwe(y,w,x,b,elev,azim):
    ws = np.arange(-100,101)
    bs = np.arange(-100,101)
    costs = np.zeros((201,201))
    i = 0
    for w in ws:
        j = 0
        for b in bs:
            costs[i,j] = cost_function(y,w,x,b)
            j+=1
        i+=1
    
    ax = plt.axes(projection="3d")
    ax.view_init(elev,azim)
    w_grid,b_grid = np.meshgrid(ws,bs)
    ax.plot_surface(w_grid,b_grid,costs,alpha=0.5)
    w_index,b_index = np.where(costs == np.min(costs))
    ax.scatter(ws[w_index],bs[b_index],costs[w_index,b_index],color="red")
    ax.scatter(w_hist[0],b_hist[0],c_hist,color="green")
    ax.set_title("Salary Data")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("cost")
    ax.plot(w_hist,b_hist,c_hist,color="blue")
    plt.show()
    
    
viwe(y,w_final,x,b_final,elev=20,azim = 60)

n = float(input("請輸入要預測幾年"))
y_ans = (f"{w_final*n+b_final:.2f}萬")
print(y_ans)
