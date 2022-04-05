import random
import math

# DO NOT CHANGE THE FOLLOWING LINE
def lloyds(data, k, columns, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    # This function has to return a list of k cluster centers (lists of floats of the same length as columns)
    def dist(center, instance, columns):
        distance = 0
        index = 0
        for column in columns:
            distance += (instance[column] - center[index])**2
            index += 1
        return math.sqrt(distance)

    def mean(cluster, columns):
        average = []
        index = 0
        for column in columns:
            average.append(0)
            for instance in cluster:
                average[index] += instance[column]
            average[index] /= len(cluster)
            index += 1
        return average

    clusters = []
    for i in range(k):
        clusters.append([])

    if centers is None:
        centers = []
        random.seed()
        for i in range(k):
            random_instance = random.choice(data)
            center = []
            for column in columns:
                center.append(random_instance[column])
            
            centers.append(center)

    if n is None:
        n = 10

    for iteration in range(n):
        for instance in data:
            smaller_index = 0
            smaller_distance = dist(centers[smaller_index], instance, columns)

            for current_index in range(1, len(centers)):
                current_distance = dist(centers[current_index], instance, columns)

                if current_distance < smaller_distance:
                    smaller_distance = current_distance
                    smaller_index = current_index
            
            clusters[smaller_index].append(instance)

        for i in range(k):
            centers[i] = mean(clusters[i], columns)
            clusters[i].clear()

    return centers
    
# DO NOT CHANGE THE FOLLOWING LINE
def kmedoids(data, k, distance, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    # This function has to return a list of k cluster centroids (data instances!)
    pass

