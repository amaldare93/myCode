/*
 *  Anthony Maldarelli
 *  CSCI 235
 *
 *  Homework #2
 *
 */

#ifndef _Square_Matrix__
#define _Square_Matrix__

#include <iostream>
using namespace std;

class Square_Matrix{
    
public:
    // Constructors / Destructors
    Square_Matrix();
    Square_Matrix(int size);
    ~Square_Matrix();

    // Returns size
    int Get_Size() const;
    
    // Returns value of matrix[rol,col]
    int Get_Elem(const int row, const int col) const;
    
    // Sets size, *Does not retain previous data
    void Set_Size(const int new_size);
    
    // Sets value to matrix[row,col]
    void Set_Elem(const int new_val, const int row, const int col);
    
    // OPERATORS
    // Equality
    bool operator ==(const Square_Matrix& mx2);
    
    // Addition
    Square_Matrix operator +(const Square_Matrix& mx2);
    
    // Assignment
    Square_Matrix& operator =(const Square_Matrix& rh);
    
    // EXTRAS
    // Print entire matrix
    void Print_Matrix() const;

    
private:
    
    int** matrix;
    
    int size;
    
};

#endif
