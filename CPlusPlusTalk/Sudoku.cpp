/**
  C++ Program to Solve Sudoku Problem using BackTracking
  Adapted from 
  http://www.sanfoundry.com/cpp-program-solve-sudoku-problem-backtracking/
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include "SudokuSolver.H"
using namespace std;
 
int main()
{
  // Initialize the sudoku grid
  int grid[9][9];
  
  // Specify the name of the sudoku grid file to be read in
  string gridFileName;
  cout << "Enter the name of the sudoku grid file to be read in:" << endl;
  cin >> gridFileName;
  
  // If I were really following good coding practices,  
  // I'd insert some kind of check to make sure that the 
  // grid file is formatted properly
  
  // Read in the sudoku grid
  string line;
  ifstream sfile;
  sfile.open(gridFileName);
  if (sfile.is_open())
    {
      // Initialize a loop to read in the grid 
      // row by row (line by line)
      int row = 0;
      while (getline (sfile, line))
        {
          // Read in each entry in the given line, 
          // i.e. the value in each column in the 
          // given row
          istringstream ss(line);
          int col = 0;
          while(ss >> grid[row][col])
            {
              col++;
            }
          // End loop over columns
          row++;
        }
      // End loop over rows/lines
      sfile.close();
    }
  // If the file can't be opened, print an error message
  else cout << "Unable to open file"; 
  
  // Declare and run the solver, then print out the solution, 
  // or if no solution exists, say so
  SudokuSolver solver;
  if (solver.SolveSudoku(grid) == true)
    {
      solver.printGrid(grid);
    }
  else
    cout<<"No solution exists"<<endl;
  return 0;
}
