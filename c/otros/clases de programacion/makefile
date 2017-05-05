CC = g++ -std=c++11
CFLAGS = -c 

all: archivos

archivos: main.o db.o persona.o
	$(CC) main.o db.o persona.o -o archivos
	
main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp
	
db.o: db.cpp
	$(CC) $(CFLAGS) db.cpp
	
persona.o: persona.cpp
	$(CC) $(CFLAGS) persona.cpp
	
clean:
	rm -rf *o archivos
