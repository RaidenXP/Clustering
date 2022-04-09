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

    def calc_threshold(previous_centers, current_centers, columns):
        threshold = 0
        for i in range(len(previous_centers)):
            distance = 0
            for j in range(len(columns)):
                distance += (current_centers[i][j] - previous_centers[i][j])**2
            threshold += distance

        return threshold

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

    check = True
    iteration = 0

    while(iteration < n and check):
        for instance in data:
            smaller_index = 0
            smaller_distance = dist(centers[smaller_index], instance, columns)

            for current_index in range(1, len(centers)):
                current_distance = dist(centers[current_index], instance, columns)

                if current_distance < smaller_distance:
                    smaller_distance = current_distance
                    smaller_index = current_index
            
            clusters[smaller_index].append(instance)

        previous_centers = centers.copy()
        
        for i in range(k):
            if(len(clusters[i])):
                centers[i] = mean(clusters[i], columns)
                clusters[i].clear()

        if eps is not None:
            threshold = calc_threshold(previous_centers, centers, columns)
            #print(threshold)
            if threshold < eps:
                #print("exited through eps")
                check = False
        
        iteration += 1

    return centers
    
# DO NOT CHANGE THE FOLLOWING LINE
def kmedoids(data, k, distance, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    # This function has to return a list of k cluster centroids (data instances!)
    def new_center(cluster, distance):
        distance_sums = []
        for instance in cluster:
            summed = 0
            for other_instance in cluster:
                if instance.equals(other_instance):
                    continue
                else:
                    summed += distance(instance, other_instance)
            distance_sums.append(summed)
        
        next_center = distance_sums.index(min(distance_sums))

        return cluster[next_center]
        
    def calc_threshold(previous_centers, current_centers, distance):
        threshold = 0
        index = 0
        for instance in previous_centers:
            threshold += distance(instance, current_centers[index])
            index += 1

        return threshold

    clusters = []
    for i in range(k):
        clusters.append([])

    if centers is None:
        centers = []
        random.seed()
        for i in range(k):
            random_instance = random.choice(data)
            centers.append(random_instance)

    if n is None:
        n = 10

    check = True
    iteration = 0

    while(iteration < n and check):
        for instance in data:
            smaller_index = 0
            smaller_distance = distance(centers[smaller_index], instance)

            for current_index in range(1, len(centers)):
                current_distance = distance(centers[current_index], instance)

                if current_distance < smaller_distance:
                    smaller_distance = current_distance
                    smaller_index = current_index
            
            clusters[smaller_index].append(instance)

        previous_centers = centers.copy()
        
        for i in range(k):
            if(len(clusters[i])):
                centers[i] = new_center(clusters[i], distance)
                clusters[i].clear()

        if eps is not None:
            threshold = calc_threshold(previous_centers, centers, distance)
            #print(threshold)
            if threshold < eps:
                check = False
        
        iteration += 1

    return centers