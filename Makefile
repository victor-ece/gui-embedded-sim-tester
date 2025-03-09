# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall

# File names
CXX_SRC = main.cpp
CXX_EXEC = main
PYTHON_GUI = gui.py

# Targets
all: $(CXX_EXEC)

# Compile the C++ code
$(CXX_EXEC): $(CXX_SRC)
	$(CXX) $(CXXFLAGS) $(CXX_SRC) -o $(CXX_EXEC)
	@echo "C++ program compiled successfully."

# Run the Python GUI
run_gui: $(CXX_EXEC)
	@echo "Running the Python GUI..."
	python3 $(PYTHON_GUI)

# Clean up compiled files
clean:
	rm -f $(CXX_EXEC)
	@echo "Cleaned up the compiled files."