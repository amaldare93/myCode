/*
 *  Anthony Maldarelli
 *  CSCI 235
 *  3/18/14
 *
 *  Homework #2
 *
 */


#include "Square_Matrix.h"
#include <iostream>
#include <vector>
#include <time.h>
#include <cstdlib>
using namespace std;

void sudoku(const int size);
bool col_Check(const Square_Matrix& mx, const int row, const int col, const int cellValue);
void gen_Row(vector<int> pool, Square_Matrix& mx, const int n);
void sort_Row(Square_Matrix& mx, const int n);
bool big_Check(const Square_Matrix& mx, const int bottom);


int main(){
    
    sudoku(9);
    
    
    return 0;
}

// Creates a size x size matrix and fills with random numbers from 1 - size
// with no repetitions in any row or collumn
void sudoku(const int size){
    
    Square_Matrix puzz(size);
    srand(time(NULL)); // uses system clock to generate random seed
    
    // Creates a vector of numbers from 1 to size
    vector<int> num_pool;
    for (int i = 0; i < size; i++) {
        num_pool.push_back(i+1);
    }
    

    for (int i = 0; i < size; i++) {
        // Fills row with random numbers from num_pool
        // no repetitions in rows
        gen_Row(num_pool, puzz, i);
        do{
            // Sorts each row so that there are no repitions in collumns above
            sort_Row(puzz, i);
        } while (big_Check(puzz, i)); // Re-checks all collumns for repetitions
        // sort_Row will keep running while there is any repetitions
    }
    
    // Prints completed matrix
    puzz.Print_Matrix();
    
}

bool col_Check(const Square_Matrix& mx, const int row, const int col, const int cellValue){
    
    // Checks if there is a repetition in a collumn
    for (int i = 0; i < row; i++) {
        if (mx.Get_Elem(i, col) == mx.Get_Elem(row, col)) {
            return true;
        }
    }
    
    return false;
}



void gen_Row(vector<int> pool, Square_Matrix& mx, const int n){
    
    // Generate Random Row
    unsigned long poolsize = pool.size();
    for (int j = 0; j < poolsize; j++) {
        int fill = rand() % pool.size();
        mx.Set_Elem(pool[fill], n, j);
        pool.erase(pool.begin() + fill);
    }
    
}

void sort_Row(Square_Matrix& mx, const int n){
    int size = mx.Get_Size();
    for (int j = 0; j < mx.Get_Size(); j++) {                           // for every collumn in row n
        if (col_Check(mx, n, j, mx.Get_Elem(n, j))){              // if there is a repetition in the collumn
            for (int k = 1 % size; k < size; k++) {                     // cycle through cells to the right
                if (col_Check(mx, n, j, mx.Get_Elem(n, (j+k) % size))) {// if that cell would fit
                    int temp = mx.Get_Elem(n, j);                       // swap the two cells
                    mx.Set_Elem(mx.Get_Elem(n, (j+k) % size), n, j);
                    mx.Set_Elem(temp, n, (j+k) % size);
                }
            }
        }
    }
}

bool big_Check(const Square_Matrix& mx, const int bottom){
    
    // Checks if there is any repetition in any of the collumns
    for (int j = 0; j < mx.Get_Size(); j++) {
        if (col_Check(mx, bottom, j, mx.Get_Elem(bottom, j))){
            return true;
        }
    }
    return false;
}






