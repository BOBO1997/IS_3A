CC = g++
CFALGS = -Wall
GREEDY = greedy.cpp
DIJKSTRA = dijkstra.cpp
ASTAR = astar.cpp

.PHONY: all clean

all: greedy dijkstra astar

greedy: $(GREEDY)
	$(CC) $(CFLAGS) -o $@ $^

dijkstra: $(DIJKSTRA)
	$(CC) $(CFLAGS) -o $@ $^
	
astar: $(ASTAR)
	$(CC) $(CFLAGS) -o $@ $^


clean:
	rm greedy dijkstra astar
