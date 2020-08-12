CC		= g++
DEBUG=yes
CFLAGS	=  -m32 `pkg-config gtkmm-2.4 --cflags` -W -Wall -ansi -pedantic
LDFLAGS =
EXEC	= result
RM		= rm -f
RM_WINDOWS = del /s /q

RECWILDCARD	=	$(foreach d,$(wildcard $(1:=/*)),$(call RECWILDCARD,$d,$2) $(filter $(subst *,%,$2),$d))


SRC_C = $(call RECWILDCARD,.,*.cpp)

OBJ		= $(SRC_C:.cpp=.o)

all: $(EXEC)
ifeq ($(DEBUG),yes)
	@echo "Generation en mode debug"
else
	@echo "Generation en mode release"
endif

$(EXEC): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(EXEC)

.PHONY: clean fclean re

clean:
ifeq ($(OS),Windows_NT)
	$(RM_WINDOWS) *.o
else
	$(RM) -rf $(OBJ)
endif

fclean: clean
ifeq ($(OS),Windows_NT)
	del /s /q $(EXEC).exe
else
	$(RM) -rf $(EXEC)
endif

re: fclean all