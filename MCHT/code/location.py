import numpy as np
# ini_point=initial point


def statistics(point_name, point_loc):
    """
    doing statistics on the data of the given point(point_name)
    return n, mean, std
    """
    point_sta = None
    point_name_array = np.unique(point_name)
    for p in point_name_array:
        tmp_loc = point_loc * (point_name==p).reshape((-1,1))
    
        n = np.count_nonzero(tmp_loc, axis=0)
        mean = np.where(n!=0, np.sum(tmp_loc,axis=0)/n, 0)
        tmp = np.where(tmp_loc==0, mean, tmp_loc)
        std = np.where(n!=0, np.sqrt(np.sum((tmp-mean)**2, axis=0))/n, 0)

        if point_sta is None:
            point_sta = np.array([[n, mean, std]])
        
        else:
            point_sta = np.vstack((point_sta, np.array([[n, mean, std]])))
    
    return point_name_array, point_sta


def read_data(filename="sample_data.csv"):
    """
    return bssid, point_name, point_loc
    """
    with open(filename, 'r') as f:
        raw_data = [i.split(",") for i in f.read().split("\n")]
        bssid = raw_data[0][1:]
        data = np.array([[float(j) for j in i] for i in raw_data[1:]])
        
        return bssid, data[:,0], data[:,1:] 

#l is a length but don't know the unit.
def signal_to_l(s):
    return np.power(10,-s/20.0)/100

def distance(p1, p2):
    return np.sqrt(np.sum((p1-p2)**2, axis=1))

def location(loc_list, lr=1e-5, beta=0.95, epoch=100000, fix_c0=False):
    """
    using momentum to calculate numerical solution
    return ini_point, c0, error
    """
    loc_point, loc_distance = loc_list[:, 0:3], loc_list[:, 3]
    ini_point = np.mean(loc_list, axis=0)[0:3]

    ini_data = np.concatenate((ini_point, np.array([1.0])))
    #loc_distance += (np.random.random(loc_distance.shape)-0.5)#for error test

    v = 0
    for _ in range(epoch):
        ini_point, c0 = ini_data[:3], ini_data[3]
        if fix_c0:c0 = 1
        tmp_distance = distance(loc_point, ini_point)
        error = np.sum((tmp_distance-c0*loc_distance)**2)**0.5
        #print("error: ", error)
        if error < 1e-12:
            break

        #for x,y,z
        grad_1 = (ini_point-loc_point).T/(tmp_distance+1e-10)
        grad_2 = 2 * (tmp_distance-c0*loc_distance).reshape((-1, 1))
        grad_xyz = np.sum(grad_1 @ grad_2, axis=1)

        #for c0
        grad_c0 = np.sum(loc_distance*(c0*loc_distance-tmp_distance))
        grad = np.hstack((grad_xyz, grad_c0))
        
        v = beta*v - lr*grad
        ini_data += v
        
        #ini_data -= lr*grad

    print("error: ", error, "     c0: ", c0, "     point: ", ini_point)
    return ini_point, c0, error


if __name__ == "__main__":
    """
    l_list = np.array([[0, 0, 1, 2*0.82],
                       [0, -1, 0, np.sqrt(2)*0.82],
                       [-1, 0, 0, np.sqrt(2)*0.82],
                       [0, 1, 0, np.sqrt(2)*0.82],
                       [1, 0, 0, np.sqrt(2)*0.82]], dtype=np.float64)
    
    ini_point, c0, error = location(l_list)
    print("real c0: ", c0)
    """
    bssid, point_name, point_loc = read_data()

    #point_sta[point_name] = [n, mean, std]
    point_name_array, point_sta = statistics(point_name, point_loc)
    

    loc_list = np.array([[0, 0, 5.08],
                         [8.645, 0 , 5.08],
                         [20.02, 0, 5.38],
                         [-2.4, 2.1, 5.38],
                         [-2.4, 7.105, 5.38],
                         [-2.4, 14.385, 5.38],
                         [8.645,0,0]], dtype=np.float64)
    using_point = np.array([True, False, True, True, False, True, True])#1,3,4,6,7


    with open('source.csv', 'r') as f:
        source = np.array([[float(y) for y in x.split(',')] for x in f.read().split('\n')[:-1]])
        bssid_num, s_point, c0, error = source[:,0], source[:,1:4], source[:,4], source[:,5]
    
    print(c0.shape)
    input()
    for x in range(30,60):
        test_signal = point_loc[x,bssid_num.astype(np.int)]#point2
        test_r = (signal_to_l(test_signal)*c0).reshape((-1,1))
        s_data = np.concatenate((s_point, test_r), axis=1)[0:2]
        ini_point, _, error = location(s_data,lr=1e-5, beta=0.0, epoch=100000, fix_c0=True)
    

    """
    #for source
    with open('mean.csv', 'w') as f:
        for x in range(len(point_sta[0][1])):
            f.write(','.join(list(point_sta[using_point, 0, x].astype(np.str)))+'\n')

    with open("source.csv", 'w') as f:
        for using_bssid in [1,4,6,11,16,17,18,31,34,41,43]:
            length_array = signal_to_l(point_sta[using_point,1 ,using_bssid].reshape((-1,1)))
            loc_data = np.concatenate((loc_list[using_point], length_array), axis=1)
            s_point, c0, error = location(loc_data)
            line = str(using_bssid)+','+\
                   ','.join([str(i) for i in s_point])+','+\
                   str(c0)+','+\
                   str(error)+'\n'
    

            f.write(line)

        print("point", s_point, "c0: ", c0, "error: ", error)
    """
    