import sys, os
sys.path.append(os.pardir)
from mnist import download_mnist

(x_train,t_train),(x_test,t_test) = download_mnist(flatten = True, noromalize = False)