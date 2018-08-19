import numpy as np


def cal_covariance(data_matrix):
    print ("input matrix is", data_matrix)
    print np.shape(data_matrix)[0]

    # new_covar_matrix = np.empty()
    tmp_array = np.zeros((data_matrix.shape[0]))
    for i, row in enumerate(data_matrix):
        tmp_array[i] = np.mean(row)
    ##############
    # for e in data_matrix:
    #      print e
    # for i in range(0, np.shape(data_matrix))
    ##############
    print ("tmp array is", tmp_array)
    # cal_cov = np.cov(data_matrix)
    # print ("covariance value is", cal_cov)
    # print (np.tril(cal_cov))

m = np.arange(start=0, stop=36000000).reshape(6000, 6000)
cal_covariance(m)
