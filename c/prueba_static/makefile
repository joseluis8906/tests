CC = g++
CFLAGS = -c -Wall -std=c++11
LDFLAGS = -O3 
LDLIBS = 
SOURCE = src/
EXE = prueba

all: $(EXE)

$(EXE): main.o 
	$(CC) main.o $(LDFLAGS) $(LDLIBS)
	
main.o: $(SOURCE)main.cpp
	$(CC) $(SOURCE)main.cpp $(CFLAGS)
		
clean:
	rm *o $(EXE)
