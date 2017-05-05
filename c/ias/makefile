CC = g++ -std=c++11
CFLAGS = -c -lcppdb -lcrypto
LDFLAGS = -lcppdb -lcrypto
SOURCE = src/

all: ias

ias: main.o user.o db.o
	$(CC) main.o user.o db.o -o ias $(LDFLAGS)
	
main.o: $(SOURCE)main.cpp
	$(CC) $(CFLAGS) $(SOURCE)main.cpp
	
user.o: $(SOURCE)user.cpp
	$(CC) $(CFLAGS) $(SOURCE)user.cpp
	
db.o: $(SOURCE)db.cpp
	$(CC) $(CFLAGS) $(SOURCE)db.cpp
	
clean:
	rm *o ias
