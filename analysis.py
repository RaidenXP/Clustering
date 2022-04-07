import clustering
import pandas as pd
import matplotlib.pyplot as plt
import math

def plot(data, centers, x, y, scale=None):
    def dist(point,center):
        return math.sqrt((point[x] - center[0])**2 + (point[y] - center[1])**2)
    xs, ys, colors = [], [], []
    for d in data:
        mind = None 
        cluster = None 
        for i,c in enumerate(centers):
            delta = dist(d, c)
            if mind is None or delta < mind:
                mind = delta
                cluster = i
        xs.append(d[x])
        ys.append(d[y])
        colors.append(cluster)
        
    cxs, cys, ccolors = [], [], []
    for i,c in enumerate(centers):
        cxs.append(c[0])
        cys.append(c[1])
        ccolors.append(i)
    if scale is None:
        fr = min(min(xs), min(ys), min(cxs), min(cys))
        to = max(max(xs), max(ys), max(cys), max(cys))
        range = (to-fr)
        fr -= 0.01*range
        to += 0.01*range
    else:
        fr,to = scale
    plt.scatter(xs, ys, c=colors)
    plt.scatter(cxs, cys, c=ccolors, marker = "+")
    plt.xlim((fr,to))
    plt.ylim((fr,to))
    plt.show()


def analysis():
    df = pd.read_csv("norm_steam_games.csv")
    data = [item for (idx, item) in df.iterrows()]

    print(data[0])

    centers = clustering.lloyds(data, 1, ['norm_positive_rev', 'norm_Concurrent_Users'], n=10)
    plot(data, centers, 'norm_positive_rev', 'norm_Concurrent_Users', scale=(0, 1))

    print(centers)

if __name__ == "__main__":
    analysis()