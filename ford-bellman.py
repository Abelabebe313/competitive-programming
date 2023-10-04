#include <iostream>
#include <vector>
#include <climits>
#include <tuple>

void solution() {
    int n, m;
    std::cin >> n >> m;
    std::vector<std::tuple<int, int, int>> graph;

    for (int i = 0; i < m; i++) {
        int v, u, w;
        std::cin >> v >> u >> w;
        graph.push_back(std::make_tuple(v, u, w));
    }

    std::vector<int> dist(n + 1, INT_MAX);
    dist[1] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (const auto& edge : graph) {
            int u, v, w;
            std::tie(u, v, w) = edge;

            if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        if (dist[i] == INT_MAX) {
            dist[i] = 30000;
        }
    }

    for (int i = 1; i <= n; i++) {
        std::cout << dist[i] << " ";
    }
}

int main() {
    solution();
    return 0;
}