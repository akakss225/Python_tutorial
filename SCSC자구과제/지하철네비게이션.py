# BFS를 사용하여 최소거리 경로를 찾을 수 있다.
# 다익스트라 알고리즘은 최소 cost를 가지는 경로를 찾을 수 있는 알고리즘이다.
# 여기서 cost는 시간일 수 있고, 시간, 신호등, 주변 경관 등을 적절하게 점수화 한 것일 수도 있다.
# 예를들어 시간이 오래걸리거나 신호등이 많거나 차선이 좁으면 상승하는 cost 함수를 만들 수 있다면, 이 cost함수를 최소화 하는 경로를 찾을 수 있다는 의미이다.
# 이를 이용하면 네비게이션 알고리즘에서 최단경로, 최소시간, 최소비용, 최적 경로라는 이름으로 경로를 탐색하고 사용자는 이 중 적절한 경로를 선택하도록 하는 것이 가능하다.
# 다익스트라 알고리즘은 현재 노드를 통해 연결된 노드로 가는 것과 다른 경로를 통해 가는 cost를 비교하여 더 작은 cost가 있을 경우, 업데이트 하는 방법이다.

import folium
import csv
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from folium.map import Marker

form_class = uic.loadUiType("/Users/sumin/Desktop/All_things/Programming_Languages/Python/Subway.ui")[0]

f = open('/Users/sumin/Desktop/All_things/Programming_Languages/Python/subway.csv')
graph = list(csv.reader(f))

f2 = open('/Users/sumin/Desktop/All_things/Programming_Languages/Python/subwayLocation.csv')
location = list(csv.reader(f2))


def new_func(graph):
    nodes = set()
    for edge in graph:
        nodes.add(edge[0])
        nodes.add(edge[1])
    return nodes

nodes = new_func(graph)


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        for i in graph:
            self.List.addItem(i[0])
        
        self.Add.clicked.connect(self.locationAdd)
        self.Delete.clicked.connect(self.locationDelete)
        self.Run.clicked.connect(self.programRun)
        self.List.itemDoubleClicked.connect(self.locationAdd)
        self.SelectedList.itemDoubleClicked.connect(self.locationDelete)

    def locationAdd(self):
        self.SelectedList.addItem(graph[self.List.currentRow()][0])
    
    def locationDelete(self):
        self.removeItemRow = self.SelectedList.currentRow()
        self.SelectedList.takeItem(self.removeItemRow)
    
    def programRun(self):
        start = self.SelectedList.item(0).text()
        end = self.SelectedList.item(1).text()
        find = findLocation(dj.getPath(start, end), location)
        point_Map(find)
        


class Dijkstra:
    def __init__(self,nodes):
        # 그래프를 받고, 그 그래프의 각 노드를 딕셔너리 형태로 받는다.
        self.g = {}
        # 최단거리를 구하기위한 새로운 딕셔너리 생성
        self.dist = {}
        for node in nodes:
            self.g[node] = {}
            self.dist[node] = [float("inf"), "none"]

    def setEdge(self,a,b,w,bidirection=True):
        self.g[a][b] = w
        if bidirection == True: self.g[b][a] = w

    def getPath(self,start,end):
        dictfilt = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
        visits = set()
        curNode = start
        self.dist[curNode][0] = 0
        while True:
            visits.add(curNode)
            nodes.remove(curNode)
            neighbors = self.g[curNode]

            for node in neighbors:
                if min(self.dist[node][0], self.dist[curNode][0] + int(self.g[curNode][node])) < self.dist[node][0]:
                    self.dist[node][0] = min(self.dist[node][0], self.dist[curNode][0] + int(self.g[curNode][node]))
                    self.dist[node][1] = curNode

            if len(nodes) > 0:
                curNode = min(dictfilt(self.dist, nodes), key=dictfilt(self.dist, nodes).get)
            else:
                break

        path = [end]
        dist = []

        while end != start:
            path.append(self.dist[end][1])
            dist.append(self.dist[end][0])
            end = self.dist[end][1]

        return path[::-1]


dj = Dijkstra(nodes)
for g in graph:
    dj.setEdge(g[0],g[1],g[2])

def findLocation(nodes, location):
    point = []
    for node in nodes:
        for i in location:
            if node[-4::-1] == i[0][-1::-1]:
                point.append([float(i[1]),float(i[2])])
                break
    return point


def point_Map(nodes):
    m = folium.Map(
        location=nodes[0],
        tiles='openstreetmap',
        zoom_start=13,
        )
    for point in nodes:
        folium.Marker(
            point,
            icon=folium.Icon(color='red')
            ).add_to(m)
    folium.PolyLine(nodes,color='red').add_to(m)
    m.save('map2.html')
'''
point = findLocation(dj.getPath('종로3가(1)','성내(2)'),location)

point_Map(point)
'''

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

f.close()
