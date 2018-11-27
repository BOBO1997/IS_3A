#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <typeinfo>

int main()
{
    int a[] = {5, 4, 6, 3, 7, 2, 8, 1, 9, 0};
    auto c = [](int l, int r) { if (l % 2 == 0) return r % 2 != 0 || l >= r; else return r % 2 != 0 && l < r; };
    std::priority_queue<int, std::vector<int>, decltype(c)> q(c);

    for (size_t i(0); i < sizeof(a) / sizeof(a[0]); ++i) {
        q.push(a[i]);
    }

    while (!q.empty()) {
        std::printf("%d\n", q.top());
        q.pop();
    }
	std::cout << (typeid(c) == typeid(true)) << std::endl;
    return 0;
}
