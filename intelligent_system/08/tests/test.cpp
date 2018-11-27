#include <iostream>
#include <vector>
#include <functional>

int main()
{
	std::vector<int> a(2, 0);
	std::vector<int> b(2, 0);
	a[0] = 0; a[1] = 2;
	b[0] = 2; b[1] = 2;
	std::cout << std::less< std::vector<int> >()(a, b) << std::endl;
}
