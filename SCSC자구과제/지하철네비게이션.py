# BFS를 사용하여 최소거리 경로를 찾을 수 있다.
# 다익스트라 알고리즘은 최소 cost를 가지는 경로를 찾을 수 있는 알고리즘이다.
# 여기서 cost는 시간일 수 있고, 시간, 신호등, 주변 경관 등을 적절하게 점수화 한 것일 수도 있다.
# 예를들어 시간이 오래걸리거나 신호등이 많거나 차선이 좁으면 상승하는 cost 함수를 만들 수 있다면, 이 cost함수를 최소화 하는 경로를 찾을 수 있다는 의미이다.
# 이를 이용하면 네비게이션 알고리즘에서 최단경로, 최소시간, 최소비용, 최적 경로라는 이름으로 경로를 탐색하고 사용자는 이 중 적절한 경로를 선택하도록 하는 것이 가능하다.
# 다익스트라 알고리즘은 현재 노드를 통해 연결된 노드로 가는 것과 다른 경로를 통해 가는 cost를 비교하여 더 작은 cost가 있을 경우, 업데이트 하는 방법이다.

import folium
import csv
import tkinter as tk
import webbrowser

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        
        
