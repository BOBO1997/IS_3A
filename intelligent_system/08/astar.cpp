#include <iostream>
#include <vector>
#include <iomanip>
#include <limits>
#include <queue>
#include <functional>

#define MAX_PATTERN 360
#define SIZE 6

class Astar
{
private:
	int states[MAX_PATTERN][SIZE];
	int space_pos[MAX_PATTERN];
	int init_state[SIZE];
	int goal_state[SIZE];
	int prev_state[MAX_PATTERN];
	int check_table[MAX_PATTERN * 2];
	std::priority_queue< std::vector <int>, std::vector< std::vector <int> >, std::less< std::vector<int> > > open;
	std::priority_queue<int> closed;
public:
	Astar(int* init_board);
	int convert_to_index(int* state);
	int calc_diff(int* state);
};

Astar::Astar(int* init_board)
{
	std::memcpy(init_state, init_board, SIZE);
	for (int i = 0; i < 5; i++) goal_state[i] = i + 1;
	goal_state[5] = 0;
	std::vector<int> a(2, 0);
	a[0] = calc_diff(init_state);
	a[1] = convert_to_index(init_state);
	open.push(a);
}

int Astar::convert_to_index(int* state)
{
	int temp[SIZE];
	std::memcpy(temp, state, SIZE);
	int fact_table[SIZE] = {120, 24, 6, 2, 1, 0};
	int index = 0;
	for (int i = 0; i < SIZE - 1; i++) {
		index += fact_table[i] * temp[i];
		for (int j = i + 1; j < SIZE; j++) {
			if (temp[i] < temp[j]) temp[j]--;
		}
	}
	return index;
}

int Astar::calc_diff(int* state)
{
	int total_diff = 0;
	for (int i = 0; i < SIZE; i++) {
		if (state[i] != i + 1 && state[i] != 0) total_diff++;
	}
	return total_diff;
}

int main()
{
	int init_board[SIZE] = {4, 3, 5, 2, 1, 0};
	Astar I = Astar(init_board);
}
