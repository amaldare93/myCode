#ifndef __project2__BinHeap__
#define __project2__BinHeap__

#include "QuadraticProbing.cpp"
//#include "Soldier.h"
#include <vector>
using namespace std;

template <typename Type>
class BinHeap {
public:

    BinHeap( int capacity = 100 );
    BinHeap( const vector<Type>& items );
    
    bool isEmpty( ) const;
    const Type& findMin( ) const;
    const int getSize( ) const;
    
    void insert( const Type& x );
    void insertSimple( const int x );
    void deleteMin( );
    void deleteMin( Type& minItem );
    void makeEmpty( );
    
    void decreaseKey( const int ID, int delta );   // moves towrds top of heap
    void increaseKey( const int ID, int delta );   // moves towards bottom of heap
    void remove( int ID );
    int findSoldierPos( const int ID ) const;
    Type& targetSoldier( const int ID );
    
private:
    
    int currentSize;
    vector<Type> array;
    
    HashTable<int> table;
    
    void buildHeap( );
    void percolateDown( int hole );
    
    
};


#endif /* defined(__project2__BinHeap__) */
