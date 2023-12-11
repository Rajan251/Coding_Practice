from collections import deque
q = deque()
# orders = [,'samosa',,'biryani','burger']
q.appendleft('pizza')
q.appendleft('samosa')
q.appendleft('pasta')
q.appendleft('biryani')
q.appendleft('burger')
q.appendleft(8)
q.appendleft(8)
q.appendleft(10)
print(q.pop())
print(q)
print(q.pop())
print(q.pop())

#----------------------------------------------------------------
wmt_stock_price_queue = []

wmt_stock_price_queue.insert(0,131.10)
wmt_stock_price_queue.insert(0,132.12)
wmt_stock_price_queue.insert(0,135)

print(wmt_stock_price_queue)
print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue)
print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())
#----------------------------------------------------------------