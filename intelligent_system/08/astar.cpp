#include <iostream>
#include <vector>
#include <iomanip>
#include <cstdlib>
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
	int goal_index;
	int prev_state[MAX_PATTERN];
	int noc_state[MAX_PATTERN]; // none -> 0, open -> 1, closed -> 2
	std::priority_queue< std::vector <int>, std::vector< std::vector <int> >, std::less< std::vector<int> > > open;
	std::priority_queue<int> closed;
public:
	Astar(int* init_board);
	int* move(int* state, int pre_space, int space);
	int convert_to_index(int* state);
	int calc_diff(int* state);
	std::vector<int> get_transitions(int parent_index);
	void astar();
};

Astar::Astar(int* init_board)
{
	std::memcpy(init_state, init_board, SIZE);
	for (int i = 0; i < 5; i++) goal_state[i] = i + 1;
	goal_state[5] = 0;
	goal_index = convert_to_index(goal_state);
	std::vector<int> init_node(2, 0);
	init_node[0] = calc_diff(init_state);
	init_node[1] = convert_to_index(init_state);
	prev_state[init_node[1]] = 0;
	noc_state[init_node[1]] = 1;
	open.push(init_node);
	std::memcpy(states[init_node[1]], init_state, SIZE);
	std::memcpy(states[goal_index], goal_state, SIZE);
	space_pos[init_node[1]] = 5;
	space_pos[goal_index] = 5;
}

int* Astar::move(int* state, int pre_space, int post_space)
{
	int* after_state;
	std::memcpy(after_state, state, SIZE);
	int temp = after_state[pre_space];
	after_state[pre_space] = after_state[post_space];
	after_state[pre_] = temp;
	return after_state;
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

std::vector<int> Astar::get_transitions(int parent_index)
{
	int grandp_index = prev_state[parent_index]; //親の状態の前の状態
	int* parent_state = states[parent_index];
	if (space_pos[parent_index] == 0) { 
		//親の前の状態に該当するならば、それは候補に含めない
		int* after_state = ;
		int after_index = convert_to_index(after_state);
		if (grandp_index == convert_to_index(after_state)) {
			;
		} 
		std::vector<int> cand(1, 0);
		return cand;
	}
	if (space_pos[parent_index] == 1) {
	
		std::vector<int> cand(1, 0);
		return cand;
	}
	if (space_pos[parent_index] == 2) {
	
		std::vector<int> cand(1, 0);
		return cand;
	}
	if (space_pos[parent_index] == 3) {
	
		std::vector<int> cand(1, 0);
		return cand;
	}
	if (space_pos[parent_index] == 4) {
	
		std::vector<int> cand(1, 0);
		return cand;
	}
	if (space_pos[parent_index] == 5) {
	
		std::vector<int> cand(1, 0);
		return cand;
	}
}

void Astar::astar()
{
	if (open.empty()) {
		std::cout << "Cannot reach the goal" << std::endl;
		std::exit(0);
	}
	while (1) {
		std::vector<int> min_cost_node = open.top();
		if (min_cost_node[1] == goal_index) {
			break;
		}
		noc_state[min_cost_node[1]] = 2;
		closed.push(min_cost_node[1]);
		std::vector<int> transitions = get_transitions(min_cost_node[1]);
		for (int i = 0; i < transitions.size(); i++) {
			int* child_state = NULL;
			int f = calc_diff(child_state) + min_cost_node[0] + 1;
			if (noc_state[transitions[i]] == 0) {
				std::vector<int> child(2, 0);
				child[0] = min_cost_node[0]; // 嘘
				child[1] = transitions[i];
				open.push(child);
				prev_state[transitions[i]] = min_cost_node[1];
			}
			else if (noc_state[transitions[i]] == 1 && 1) {
				
			}
			else if (noc_state[transitions[i]] == 2 && 1) {
				
			}
		}
	}
}

int main()
{
	int init_board[SIZE] = {4, 3, 5, 2, 1, 0};
	Astar I = Astar(init_board);
}
