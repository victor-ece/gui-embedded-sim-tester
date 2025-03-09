# Project 3: Software Verification Simulation

## Overview
This project involves creating a simulation of verification software.

## GUI Implementation
The GUI is implemented using Python's `tkinter` library. The GUI has the following components:
- **File Selection**: Allows the user to select a Python code file.
- **Test Execution Menu**: Provides options to run the selected code file and compare it's output with a desired output file.

## Main Program in C++
The main program is written in C++ and consists of the following classes:
- **FlashModule**: Manages the filename of the code to be executed.
- **TestModule**: Contains methods to run the code file and compare its output with a desired output.
- **ReportingModule**: Reports the result of the test execution.

## Makefile
The Makefile automates the compilation of the C++ code and provides targets to run the Python GUI and clean up compiled files.

## How to Run
1. Compile the C++ code:
```sh
make
```
2. Run the Python GUI:
```sh
make run_gui
```
3. Use the GUI to select a code file and execute tests.

## Cleaning Up
To clean up compiled files, run:
```sh
make clean
```