#include <iostream>
#include <vector>
using namespace std;
class Graph
{
private:
    int V;
    vector<vector<int>> adjList;
public:
    Graph(int vertices)
    {
        V = vertices;
        adjList.resize(V);
    }
    void addEdge(int u, int v)
    {
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }
    
    void printGraph()
    {
        for (int i = 0; i < V; i++)
        {
            cout << "Adjacency list of vertex " << i << ": ";
            for (int v : adjList[i])
            {
                cout << v << " ";
            }
            cout << endl;
        }
    }
};

int main()
{
    int V = 5;

    Graph graph(V);

    graph.addEdge(0, 1);
    graph.addEdge(0, 4);
    graph.addEdge(1, 2);
    graph.addEdge(1, 3);
    graph.addEdge(1, 4);
    graph.addEdge(2, 3);
    graph.addEdge(3, 4);

    graph.printGraph();

    return 0;
}
