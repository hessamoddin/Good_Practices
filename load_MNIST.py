# Load the MNIST dataset

# Pickles MNIST
import cPickle, gzip, numpy
import wget


file_url =  'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz'

file_name = wget.download(file_url)

 
 
# Load the dataset
f = gzip.open(file_name, 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()
