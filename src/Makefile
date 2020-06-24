all:
	g++ sql.cpp -o sql.so -fPIC -shared -l sqlite3
clean:
	rm *.so
# CC=g++
# CFLAGS=-l sqlite3 -I.
# DEPS = sql.cpp libsqlite3/sqlite3.h libsqlite3/sqlite3ext.h
# OBJ = sql.o libsqlite3/sqlite3.o

# %.o: %.c $(DEPS)
# 	$(CC) -c -o $@ $< $(CFLAGS)

# all: $(OBJ)
# 	gcc -o $@ $^ $(CFLAGS)
# # all: sql.so sqlite3.so
# # 	g++ sql.cpp -o sql.so -fPIC -shared
# clean:
# 	rm *.so
# CC=g++
# CFLAGS= -Wall -g -O -fPIC -l sqlite3
# RM= rm -rf
# .PHONY: all clean

# all: library.so
# clean:
# 	$(RM) *.o *.so

# library.so: sql.o libsqlite3/sqlite3.o
# 	$(LINK.c) -shared $^ -o $@

# sql.o: sql.cpp
# sqlite3.o: libsqlite3/sqlite3.c