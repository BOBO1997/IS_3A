OBJ = collapse.c

CC = g++
CFLAGS = -Wall 
.PHONY: all
all: collapse
collapse: $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $@
.PHONY: clean
clean:
	-rm collapse
