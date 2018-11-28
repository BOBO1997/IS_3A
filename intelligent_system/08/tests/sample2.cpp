#include <cstdio>
#include <queue>
#include <vector>

int
main()
{
	std::vector<int> a(2, 0); a[0] = 1; a[1] = 2;
	std::vector<int> b(2, 0); b[0] = 1; b[1] = 1;
	std::vector<int> c(2, 0); c[0] = 3; c[1] = 1;
	std::vector<int> d(2, 0); d[0] = 4; d[1] = 2;
    std::priority_queue< std::vector<int>, std::vector< std::vector<int> >, std::greater< std::vector<int> > > q;

	q.push(c);
	q.push(a);
	q.push(b);
	q.push(d);

    while (!q.empty()) {
        std::printf("%d ", q.top()[0]);
        std::printf("%d\n", q.top()[1]);
        q.pop();
    }

    return 0;
}
