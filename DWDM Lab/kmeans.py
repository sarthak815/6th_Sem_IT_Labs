import csv
ip = []
centroids = []
max_iter = 1
def read_csv(path = 'km.csv'):
    file = open(path, 'r')
    filecsv = csv.reader(file)
    for row in filecsv:  
        ip.append(row)
    print(ip)
    return ip

def compute_distance_point(data,centroid,k):
    op = []
    sum = 0
    for point in data:
        for i,j in zip(point, centroid):
            i = int(i)
            j = int(j)
            sum+=(i-j)**2
        sum = sum**0.5
        op.append(sum)
    return op
def clustering_based_on_distance(c_distances,data,k):
    clusters = [[]for i in range(k)]
    for pointidx,point in enumerate(data):
        distance_from_centroids = [c[pointidx] for c in c_distances]
        clusters[distance_from_centroids.index(min(distance_from_centroids))].append(point)
        #print(clusters)
    return clusters
def average_clusters(clusters):
    centroids = []
    for cluster in clusters:
        centroid = []
        for vec_idx in range(len(cluster[0])):
            vec_wise = []
            for point in cluster:
                vec_wise.append(point[vec_idx])
            centroid.append(sum(vec_wise)/len(vec_wise))
        centroids.append(centroid)

def fit(path, k):
    data = read_csv(path)
    centroids = [data[i] for i in range(k)]
    for i in range(max_iter):
        c_distances = [compute_distance_point(data,centroid,k) for centroid in centroids]
        clusters = clustering_based_on_distance(c_distances,data,k)
        print(centroids)
        prev_centroids = centroids[:]
        average_clusters(clusters)
        if centroids==prev_centroids:
            break
    print("Finished clustering in "+iter+" iterations.")
    for point_idx in range(len(data)):
        
    # labels_ = [[cluster[point_idx] for cluster in c_distances].index(min([cluster[point_idx] for cluster in c_distances])) for point_idx in range(len(data))]
    # print(labels_)

    
fit("km.csv",2)