# Variables
CC = gcc
CFLAGS = -Wall -g
OBJ_DIR = build
SRC_DIR = src
SCRIPTS_DIR = scripts
DOC_DIR = documentation
DOCS_SUBDIR = docs
DOXYFILE = Doxyfile

all: create_dirs docs $(OBJ_DIR)/main

create_dirs:
	mkdir -p $(OBJ_DIR) $(DOC_DIR)/$(DOCS_SUBDIR)

$(OBJ_DIR)/main: $(OBJ_DIR)/main.o $(OBJ_DIR)/student.o $(OBJ_DIR)/course.o
	$(CC) $(CFLAGS) -o $@ $^

$(OBJ_DIR)/main.o: $(SRC_DIR)/main.c
	$(CC) $(CFLAGS) -c -o $@ $<

$(OBJ_DIR)/student.o: $(SRC_DIR)/student.c $(SRC_DIR)/student.h
	$(CC) $(CFLAGS) -c -o $@ $<

$(OBJ_DIR)/course.o: $(SRC_DIR)/course.c $(SRC_DIR)/course.h
	$(CC) $(CFLAGS) -c -o $@ $<

$(DOXYFILE):
	doxygen -g

.PHONY: docs
docs: $(DOXYFILE)
	doxygen $(DOXYFILE)

.PHONY: clean
clean:
	rm -rf $(OBJ_DIR)