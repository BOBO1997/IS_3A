OBJ = collision.c

# CC = g++
CC = gcc
CFLAGS = -Wall 
.PHONY: all
all: collision
collapse: $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $@
.PHONY: clean
clean:
	-rm collision
