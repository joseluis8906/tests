CC = g++ -std=c++11
CFLAGS = -c -lcppdb
LDFLAGS = -lcppdb
SOURCE = src/

all: loteria

loteria: main.o #loteria.o
	$(CC) main.o -o loteria $(LDFLAGS) #loteria.o -o loteria $(LDFLAGS)
	
main.o: $(SOURCE)main.cpp
	$(CC) $(CFLAGS) $(SOURCE)main.cpp
	
#loteria.o: $(SOURCE)loteria.cpp
#	$(CC) $(CFLAGS) $(SOURCE)loteria.cpp
	
clean:
	rm *o loteria
