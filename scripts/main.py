from sklearn.datasets import fetch_openml
mnist = fetch_openml("mnist_784", version =1)
mnist.keys()
dict_keys(["data"]) a