CC = g++
CFALGS = -Wall
GREEDY = greedy.cpp
DIJKSTRA = dijkstra.cpp


.PHONY: clean

greedy: $(GREEDY)
	$(CC) $(CFLAGS) -o $@ $^

dijkstra: $(DIJKSTRA)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm greedy dijkstra
