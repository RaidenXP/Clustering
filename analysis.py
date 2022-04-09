import clustering
import pandas as pd
import matplotlib.pyplot as plt
import math
import ast

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

def analysis_lloyds():
    def dist(center, instance, columns):
        distance = 0
        index = 0
        for column in columns:
            distance += (instance[column] - center[index])**2
            index += 1
        return math.sqrt(distance)

    df = pd.read_csv("norm_steam_games.csv")
    data = [item for (idx, item) in df.iterrows()]

    #print(data[0])

    k = 3
    #columns = ['norm_positive_rev', 'norm_Concurrent_Users', 'norm_mean_forever_playtime']
    columns = ['norm_positive_rev', 'norm_negative_rev']

    centers = clustering.lloyds(data, k, columns, n=50)
    plot(data, centers, 'norm_positive_rev', 'norm_negative_rev', scale=(0, 1))
    #print(centers)

    clusters = []
    for i in range(k):
        clusters.append([])

    for instance in data:
            smaller_index = 0
            smaller_distance = dist(centers[smaller_index], instance, columns)

            for current_index in range(1, len(centers)):
                current_distance = dist(centers[current_index], instance, columns)

                if current_distance < smaller_distance:
                    smaller_distance = current_distance
                    smaller_index = current_index
            
            clusters[smaller_index].append(instance)
    
    smallest_cluster = clusters[0]
    min_value = len(clusters[0])
    for i in range(1, len(clusters)):
        if min_value > len(clusters[i]):
            min_value = len(clusters[i])
            smallest_cluster = clusters[i]
    
    for instances in smallest_cluster:
        print(instances['name'])

def analysis_medoids():
    def compare_genre(a,b):
        a_set = set()
        b_set = set()

        if (type(a['genre']) != float):
            temp = a['genre'].split(", ")
            a_set = set(temp)
        
        if (type(b['genre']) != float):
            temp = b['genre'].split(", ")
            b_set = set(temp)

        if len(a_set) != 0 and len(b_set) != 0:
            intersect = abs(len(a_set.intersection(b_set)))
            union = abs(len(a_set.union(b_set)))

            jaccard = intersect/union

            return 1 - jaccard
        else:
            return 1

    def compare_tags(a,b):
        a_set = set(ast.literal_eval(a['tags']))
        b_set = set(ast.literal_eval(b['tags']))

        if len(a_set) != 0 and len(b_set) != 0:
            intersect = abs(len(a_set.intersection(b_set)))
            union = abs(len(a_set.union(b_set)))

            jaccard = intersect/union

            return 1 - jaccard
        else:
            return 1
    
    def compare_tags_genre(a,b):
        return(compare_genre(a,b) + compare_tags(a,b))/2.0

    df = pd.read_csv("norm_steam_games.csv")
    data = [item for (idx, item) in df.iterrows()]

    k = 4

    centers = clustering.kmedoids(data, k, compare_genre, n=3)

    clusters = []
    for i in range(k):
        clusters.append([])

    for instance in data:
        smaller_index = 0
        smaller_distance = compare_genre(centers[smaller_index], instance)

        for current_index in range(1, len(centers)):
            current_distance = compare_genre(centers[current_index], instance)

            if current_distance < smaller_distance:
                smaller_distance = current_distance
                smaller_index = current_index
            
        clusters[smaller_index].append(instance)

    smallest_cluster = clusters[0]
    min_value = len(clusters[0])
    for i in range(1, len(clusters)):
        if min_value > len(clusters[i]):
            min_value = len(clusters[i])
            smallest_cluster = clusters[i]
    
    for instances in smallest_cluster:
        print(instances['name'])
    
    print(len(smallest_cluster))

def main():
    analysis_lloyds()
    #analysis_medoids()

if __name__ == "__main__":
    main()