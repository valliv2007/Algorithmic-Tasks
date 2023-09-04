from collections import deque
search_queue = deque()
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['tom'] = []
graph['jonny'] = []


def person_is_seller(name):
    return name[-1] == 'm'
def search(name):
    searched =[]
    search_queue = deque()
    search_queue += graph[name]
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


search('you')
