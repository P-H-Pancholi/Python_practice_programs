k = int(input())
rooms = list(map(int,input().split()))
set_rooms = set(rooms)
print((k*sum(set_rooms) - sum(rooms))//(k-1))
