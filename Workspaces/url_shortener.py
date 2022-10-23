import pyshorteners

url = input("enter your url: ")
s = pyshorteners.Shortener().tinyurl.short(url)
print("your shorted is",s)

# enter your url: https://github.com/taberkkaya/Python
# your shorted is https://tinyurl.com/2b7gwn49