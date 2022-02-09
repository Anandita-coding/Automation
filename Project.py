try:
    from googlesearch import search
except ImportError:
    print("There was an error importing the module")

query = "colab"

for i in search(query,tld = "co.in",num = 10, stop = 10, pause = 2):
    print(i)
