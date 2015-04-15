/*
 *  Anthony Maldarelli
 *  CSCI 235
 *
 *  Homework #2
 *
 */


#include "Square_Matrix.h"
#include <iostream>
using namespace std;

// Default constructor
Square_Matrix::Square_Matrix(){
    size = 0;
    matrix = new int*[size];
    for (int i = 0; i < size; i++) {
        matrix[i] = new int[size];
    }
}

// Constructor, size = n
Square_Matrix::Square_Matrix(int n){
    size = n;
    matrix = new int*[size];
    for (int i = 0; i < size; i++) {
        matrix[i] = new int[size];
    }
}

// Destructor
Square_Matrix::~Square_Matrix(){
    for (int i = 0; i < size; i++) {
        delete [] matrix[i];
    }
    delete [] matrix;
}

// Returns size of matrix
int Square_Matrix::Get_Size() const{
    return size;
}

// Returns element stored in matrix[row, col]
int Square_Matrix::Get_Elem(const int row, const int col) const{
    return matrix[row][col];
}

// Sets size to matrix, *Does not retain previous data
void Square_Matrix::Set_Size(const int new_size){
    
    // Deletes old matrix
    for (int i = 0; i < size; i++) {
        delete [] matrix[i];
    }
    delete [] matrix;
    
    // Creates new matrix with new_size
    size = new_size;
    matrix = new int*[size];
    for (int i = 0; i < size; i++) {
        matrix[i] = new int[new_size];
    }
}

// Sets value to matrix[row,col]
void Square_Matrix::Set_Elem(const int new_val, const int row, const int col){
    
    // Checks if location exists
    if (row >= size || col >= size) {
        cout << "ERROR: Location [" << row << "," << col << "] does not exist.\n";
    } else {
        matrix[row][col] = new_val;
    }
}

// OPERATORS
// Equality
bool Square_Matrix::operator ==(const Square_Matrix& mx2){
    
    if (size != mx2.Get_Size()) {
        return false;
    }
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (matrix[i][j] != mx2.Get_Elem(i, j)) {
                return false;
            }
        }
    }
    return true;
}

// Addition
Square_Matrix Square_Matrix::operator +(const Square_Matrix& mx2){
    
    Square_Matrix sum;
    sum.Set_Size(size);
    
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            sum.Set_Elem(matrix[i][j] + mx2.Get_Elem(i, j), i, j);
        }
    }
    
    return sum;
}

// Assignment
Square_Matrix& Square_Matrix::operator =(const Square_Matrix& rh){
    
    bool eq = true;
    
    // Check if a = a
    if (size == rh.Get_Size()) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (matrix[i][j] != rh.Get_Elem(i, j)) {
                    eq = false;
                }
            }
        }
    } else {
        eq = false;
    }
    
    if (eq == false) {
        
        //Deletes old Matrix, Sets Size
        Set_Size(rh.Get_Size());
        
        // Assign values to new matrix
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                matrix[i][j] = rh.Get_Elem(i, j);
            }
        }
    }
    return *this;
}

// Print entire matrix
void Square_Matrix::Print_Matrix() const {
    for (int i = 0; i < size; i++) {
        cout << "[ ";
        for (int j = 0; j < size; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << "]" << endl;
    }
}










