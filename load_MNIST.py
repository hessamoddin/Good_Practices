# Load the MNIST dataset


from keras.datasets import imdb
import cPickle, gzip, numpy
import wget


max_features = 20000
maxlen = 100  # cut texts after this number of words (among top max_features most common words)
batch_size = 32
file_url =  'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz'
file_name = wget.download(file_url)
f = gzip.open(file_name, 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()

print('Loading data...')

(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features,

 
 
