/**
  Class for solving a 9x9 sudoku grid using backtracking
  Adapted from 
  http://www.sanfoundry.com/cpp-program-solve-sudoku-problem-backtracking/
 */

class SudokuSolver
{
public:
  /**
    Overarching solver function
   */
  bool SolveSudoku(int grid[9][9]);
  
  /** 
    Searches the grid to find an entry that is still unassigned. 
   */
  bool FindUnassignedLocation(int  grid[9][9], 
                              int& row, 
                              int& col);
  
  /** 
    Returns whether any assigned entry in the specified row matches 
    the given number. 
   */
  bool UsedInRow(int  grid[9][9], 
                 int& row, 
                 int& num);
  
  /** 
    Returns whether any assigned entry in the specified column matches 
    the given number. 
   */
  bool UsedInCol(int  grid[9][9], 
                 int& col, 
                 int& num);

  /** 
    Returns whether any assigned entry within the specified 3x3 box matches 
    the given number. 
   */
  bool UsedInBox(int  grid[9][9], 
                 int& boxStartRow, 
                 int& boxStartCol, 
                 int& num);
  
  /** 
    Returns whether it will be legal to assign num to the given row,col location 
   */
  bool isSafe(int  grid[9][9], 
              int& row, 
              int& col, 
              int& num);

  /**
    Print the sudoku grid
   */
  void printGrid(int grid[9][9]);
private:
  //const int m_unassigned;
  //const int m_N;
};
