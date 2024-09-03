from mypubsub import MyPubSub

print("Called from entry.py")

p = MyPubSub()
p.publish('topic1', 'hello world')
