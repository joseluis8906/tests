CC = g++ -std=c++11
CFLAGS = -c -lcppcms -lcppdb
LDFLAGS = -lcppcms -lcppdb
SOURCE = src/

all: cdi

cdi: cdi.o contaduria.o
	$(CC) cdi.o contaduria.o -o cdi $(LDFLAGS)

cdi.o: $(SOURCE)cdi.cpp
	$(CC) $(CFLAGS) $(SOURCE)cdi.cpp

contaduria.o: $(SOURCE)contaduria.cpp
	$(CC) $(CFLAGS) $(SOURCE)contaduria.cpp
	
clean:
	rm -rf *o cdi
