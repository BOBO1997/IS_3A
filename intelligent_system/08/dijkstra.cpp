#include <iostream>
#include <vector>
#include <limits>
#include <set>
#include <iomanip>

#define Inf std::numeric_limits<float>::infinity()

class Graph
{
protected:
	int num_nodes;
private:
	std::vector < std::vector <float> > matrix;
public:
	Graph(int num);
	float get_dist(int i, int j);
	void add_edge(int i, int j, float e);
	void print_matrix();
};

Graph::Graph(int num)
{
	num_nodes = num;
	matrix = std::vector < std::vector <float> > (num_nodes, std::vector <float> (num_nodes, Inf));
}

void Graph::add_edge(int i, int j, float e)
{
	matrix[i][j] = e;
	matrix[j][i] = e;
}

float Graph::get_dist(int i, int j)
{
	return matrix[i][j];
}

void Graph::print_matrix()
{
	for (int i = 0; i < num_nodes; i++) {
		for (int j = 0; j < num_nodes; j++) {
			std::cout << std::setw(4) << matrix[i][j];
		}
		std::cout << "\n" << std::endl;
	}
}

class Dijkstra : public Graph
{
private:
	std::set<int> Q;
	std::vector <float> d;
	std::vector <int> prev;
public:
	Dijkstra(int num);
	int get_min_node();
	void print_d();
	void print_prev();
	void print_course(int node);
	void dijkstra(int goal);
};

Dijkstra::Dijkstra(int num) : Graph(num)
{
	for (int i = 0; i < num; i++) Q.insert(i);
	d = std::vector <float> (num, Inf);
	d[0] = 0;
	prev = std::vector <int> (num, 0);
}

int Dijkstra::get_min_node()
{
	std::set<int>::iterator i = Q.begin();
	int min_node = *i;
	while (i != Q.end()) {
		if (d[min_node] > d[*i]) {
			min_node = *i;
		}
		*i++;
	}
	return min_node;
}

void Dijkstra::print_d()
{
	for (int i = 0; i < num_nodes; i++) std::cout << std::setw(4) << d[i];
	std::cout << std::endl;;;
}

void Dijkstra::print_prev()
{
	for (int i = 0; i < num_nodes; i++) std::cout << std::setw(4) << prev[i];
	std::cout << std::endl;;;
}

void Dijkstra::print_course(int node)
{
	if (prev[node] != 0) print_course(prev[node]);
	std::cout << " -> " << (char)(node + 65);
}

void Dijkstra::dijkstra(int goal)
{
	while (!Q.empty()) {
		int min_node = get_min_node();
		Q.erase(min_node);
		for (int i = 0; i < num_nodes; i++) {
			if (get_dist(min_node, i) != Inf && d[i] > d[min_node] + get_dist(min_node, i)) {
				d[i] = d[min_node] + get_dist(min_node, i);
				prev[i] = min_node;
			}
		}
	}
	std::cout << (char)65;
	print_course(goal);
	std::cout << std::endl;
}

int main() 
{
	int num = 10;
	Dijkstra G = Dijkstra(num);
	G.add_edge(0, 1, 1);
	G.add_edge(1, 2, 2);
	G.add_edge(0, 3, 2);
	G.add_edge(3, 4, 1);
	G.add_edge(4, 5, 2);
	G.add_edge(5, 6, 1);
	G.add_edge(2, 6, 1);
	G.add_edge(6, 7, 1);
	G.add_edge(7, 8, 1);
	G.add_edge(7, 9, 2);
	G.dijkstra(9);
}
