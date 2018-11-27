#include <iostream>
#include <vector>
#include <array>
#include <limits>
#include <set>
#include <iomanip>

class Board
{
protected:
	std::array<std::array<int, 3>, 2> a;
	int space_pos_x;
	int space_pos_y;
	int pre_space_x;
	int pre_space_y;
public:
	Board();
	void move(int from_i, int from_j, int to_i, int to_j);
};

Board::Board()
{
	a[0][0] = 4;
	a[0][1] = 3;
	a[0][2] = 5;
	a[1][0] = 2;
	a[1][1] = 1;
	a[1][2] = 6;
	space_pos_x = 1;
	space_pos_y = 2;
	pre_space_x = 1;
	pre_space_y = 2;
}

void Board::move(int from_i, int from_j, int to_i, int to_j)
{
	if (a[from_i][from_j] == 6) {
		
	}
	a[to_i][to_j] = a[from_i][from_j];
	a[from_i][from_j] = 6;
}

class Astar : Board
{
private:
	std::vector < std::vector <int> > space_orbit;
public:
	Astar();
	void can_move();
	void astar();
};

Astar::Astar() : Board()
{
	space_orbit = std::vector < std::vector <int> > (2, std::vector <int> (1, 0));
	space_orbit[0][0] = 1;
	space_orbit[0][1] = 2;
}

void Astar::astar()
{

}

int main()
{
	Board b = Board();
}
