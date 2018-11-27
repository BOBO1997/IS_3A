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

class Greedy: public Graph
{
private:
	std::set<int> Q;
	std::vector <float> d;
	std::vector <int> prev;
public:
	Greedy(int num);
	int get_nearest(int focus);
	int greedy(int focus, int goal);
};

Greedy::Greedy(int num) : Graph(num)
{
	for (int i = 0; i < num; i++) Q.insert(i);
	d = std::vector <float> (num, Inf);
	d[0] = 0;
	prev = std::vector <int> (num, 0);
}

int Greedy::get_nearest(int focus)
{
	std::set<int>::iterator i = Q.begin();
	int nearest = *i;
	while (i != Q.end()) {
		if (matrix[focus][nearest] > matrix[focus][*i]) {
			nearest = *i;
		}
		*i++;
	}
	if (matrix[focus][nearest] == Inf) nearest = -1;
	return nearest;
}

int Greedy::greedy(int focus, int goal)
{
	int rank = 0;
	if (focus != goal) {
		Q.erase(focus);
		int exist_path;
		do {
			int nearest_node = get_nearest(focus);
			if (nearest_node < 0) return 1;
			exist_path = greedy(nearest_node, goal);
		} while (exist_path != 0 && !Q.empty());
	}
	std::cout << (char)(focus + 65) << " <- ";
	return 0;
}

int main() 
{
	int num = 10;
	Greedy G = Greedy(num);
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
	int result = G.greedy(0, 9);
	std::cout << std::endl;
	if (result != 0) {
		std::cout << "No Such a Path" << std::endl;
	}
}
