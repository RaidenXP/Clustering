import random
import math

# DO NOT CHANGE THE FOLLOWING LINE
def lloyds(data, k, columns, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    # This function has to return a list of k cluster centers (lists of floats of the same length as columns)
    def dist(center, instance, columns):
        
        return math.sqrt((point[x] - center[0])**2 + (point[y] - center[1])**2)

    iterations = 0

    if centers is None:
        centers = []
        for i in range(k):
            random.seed()
            random_instance = random.choice(data)
            center = []
            for column in columns:
                center.append(random_instance[column])
            
            centers.append(center)
    
    cluster_list = []

    if n is None:
        iterations = 10
    else:
        iterations = n

    
    
# DO NOT CHANGE THE FOLLOWING LINE
def kmedoids(data, k, distance, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    # This function has to return a list of k cluster centroids (data instances!)
    pass

