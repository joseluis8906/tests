CC = g++
#CFLAGS = -c -Wall -I./ -I/usr/include/zdb
CFLAGS = -c -Wall
LDFLAGS = -O3 -L./
LDLIBS = -lsfml-graphics -lsfml-window -lsfml-system
SOURCE = src/


all: comidity

comidity: main.o
	$(CC) main.o -o comidity $(LDFLAGS) $(LDLIBS)
	
main.o: $(SOURCE)main.cpp
	$(CC) $(CFLAGS) $(SOURCE)main.cpp
	
clean:
	rm *o comidity
