# Solution - 30 Aug 2024

---
## [2699. Modify Graph Edge Weights](https://leetcode.com/problems/modify-graph-edge-weights)

### cpp
```cpp
class Solution {
public:
    void runDijkstra(const vector<vector<pair<int, int>>>& adjList, vector<vector<int>>& edges, vector<vector<int>>& dist, int source, int diff, int run) {
        int n = adjList.size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.push({0, source});
        dist[source][run] = 0;

        while(pq.size()) {
            auto [currDist, currNode] = pq.top();
            pq.pop();

            if(currDist > dist[currNode][run])
                continue;
            
            for(auto &neighbor: adjList[currNode]) {
                int next = neighbor.first, edgeIndex = neighbor.second;
                int weight = edges[edgeIndex][2];

                if(weight == -1)
                    weight = 1;
                
                if(run == 1 && edges[edgeIndex][2] == -1) {
                    int newWeight = diff + dist[next][0] - dist[currNode][1];
                    if(newWeight > weight)
                        edges[edgeIndex][2] = weight = newWeight;
                }

                if(dist[next][run] > dist[currNode][run] + weight) {
                    dist[next][run] = dist[currNode][run] + weight;
                    pq.push({dist[next][run], next});
                }
            }
        }
    }

    vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int source, int destination, int target) {
        vector<vector<pair<int, int>>> adjList(n);

        for(int i=0; i<edges.size(); ++i) {
            int a = edges[i][0], b = edges[i][1];
            adjList[a].emplace_back(b, i);
            adjList[b].emplace_back(a, i);
        }

        vector<vector<int>> dist(n, vector<int>(2, INT_MAX));
        dist[source][0] = dist[source][1] = 0;

        runDijkstra(adjList, edges, dist, source, 0, 0);
        int diff = target - dist[destination][0];
        if(diff < 0) return {};

        runDijkstra(adjList, edges, dist, source, diff, 1);
        if(dist[destination][1] < target) return {};

        for(auto &edge: edges)
            if(edge[2] == -1)
                edge[2] = 1;
        
        return edges;
    }
};
```
