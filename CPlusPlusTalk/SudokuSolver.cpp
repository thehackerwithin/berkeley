/**
  Class for solving a 9x9 sudoku grid using backtracking
  Adapted from 
  http://www.sanfoundry.com/cpp-program-solve-sudoku-problem-backtracking/
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include "SudokuSolver.H"
using namespace std;

// Overarching solver function
bool SudokuSolver::SolveSudoku(int grid[9][9])
{
  // Dummy initialization: FindUnassignedLocation will
  // reinitialize this and change row and col to the 
  // indicies of the first unassigned location it finds
  int row = 0; 
  int col = 0;
  // If every location is assigned legally, the puzzle 
  // is solved
  if (!FindUnassignedLocation(grid, row, col))
    {
      return true;
    }
  // Take the unassigned location found above
  for (int num = 1; num <= 9; num++)
    {
      if (isSafe(grid, row, col, num))
        {
          grid[row][col] = num;
          if (SolveSudoku(grid))
            {
              return true;
            }
          grid[row][col] = 0; // Any unassigned space gets a 0
        }
    }
  return false;
}
 
// Searches the grid to find an entry that is still unassigned
// row and col are passed in by reference so we can use their 
// new values outside the scope of this function
bool SudokuSolver::FindUnassignedLocation(int  grid[9][9], 
                                          int& row, 
                                          int& col)
{
  for (row = 0; row < 9; row++)
    {
      for (col = 0; col < 9; col++)
        {
          // if the current entry is unassigned, i.e. has the 
          // value 0, break the loop, so we can put a number 
          // in the current row and column
          if (grid[row][col] == 0)
            {
              return true;
            }
        }
    }
  // If that entry is assigned, return false
  return false;
}
 
// Returns whether any assigned entry n the specified row matches 
// the given number
bool SudokuSolver::UsedInRow(int  grid[9][9], 
                             int& row, 
                             int& num)
{
  for (int col = 0; col < 9; col++)
    {
      if (grid[row][col] == num)
        {
          return true;
        }
    }
  return false;
}
 
/* Returns whether any assigned entry in the specified column matches 
   the given number. */
bool SudokuSolver::UsedInCol(int  grid[9][9], 
                             int& col, 
                             int& num)
{
  for (int row = 0; row < 9; row++)
    {
      if (grid[row][col] == num)
        {
          return true;
        }
    }
  return false;
}
 
// Returns whether any assigned entry within the specified 3x3 box matches 
// the given number
// Note that each box's indices are in [0,3) x [0,3), whereas the grid's 
// indices are in [0,9) x [0,9)
bool SudokuSolver::UsedInBox(int  grid[9][9], 
                             int& boxStartRow, 
                             int& boxStartCol, 
                             int& num)
{
  for (int row = 0; row < 3; row++)
    {
      for (int col = 0; col < 3; col++)
        {
          int gridRow = row + boxStartRow;
          int gridCol = col + boxStartCol;
          if (grid[gridRow][gridCol] == num)
            {
              return true;
            }
        }
    }
  return false;
}
 
// Returns whether it will be legal to assign num to the given row,col location
// Note that each box's indices are in [0,3) x [0,3), whereas the grid's 
// indices are in [0,9) x [0,9)
bool SudokuSolver::isSafe(int  grid[9][9], 
                          int& row, 
                          int& col, 
                          int& num)
{
  int boxStartRow = row - row % 3;
  int boxStartCol = col - col % 3;
  return !UsedInRow(grid, row, num) && !UsedInCol(grid, col, num) &&
         !UsedInBox(grid, boxStartRow, boxStartCol, num);
}
 
// Print grid
void SudokuSolver::printGrid(int grid[9][9])
{
  for (int row = 0; row < 9; row++)
    {
      for (int col = 0; col < 9; col++)
        {
          cout<<grid[row][col]<<"  ";
        }
      cout<<endl;
    }
}
 
