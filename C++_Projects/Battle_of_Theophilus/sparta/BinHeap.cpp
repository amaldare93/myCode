#include "BinHeap.h"
//#include "QuadraticProbing.h"
#include <iostream>
#include <limits>
using namespace std;

// constructs empty heap of size capacity
template<typename Type>
BinHeap<Type>::BinHeap( int capacity )
: array( capacity + 1 ), currentSize{ 0 }
{
}

// constructs heap and fills with values in vector
template<typename Type>
BinHeap<Type>::BinHeap( const vector<Type>& items )
: array( items.size( ) + 10 ), currentSize{ static_cast<int>(items.size( )) }
{
    for( int i = 0; i < items.size( ); ++i )
        array[i + 1] = items[i];
    buildHeap( );
}

// isEmpty
template<typename Type>
bool BinHeap<Type>::isEmpty( ) const
{
    return currentSize == 0;
}

// findMin
template<typename Type>
const Type& BinHeap<Type>::findMin( ) const
{
    return array[1];
}

// getSize
template<typename Type>
const int BinHeap<Type>::getSize( ) const
{
    return currentSize;
}


// insert
template<typename Type>
void BinHeap<Type>::insert(const Type& x )       // x is the soldier to be inserted
{
    // if array is full, double its size
    if( currentSize == array.size( ) - 1 )
        array.resize( array.size( ) * 2 );
    
    // percolate up
    int hole = ++currentSize;                   // hole is index of hole in next available slot
    Type copy = x;                              // copy is x is the soldier
    
    array[0] = move( copy );                    // put soldierID into 0 slot (above root, not part of heap)
    while (x < array[hole / 2] && hole > 1 ) {  // while the soldierID is smaller than hole's parent
        array[hole] = move( array[hole / 2] );  //      move the parent down into the hole
        table.updateValue( array[hole].getID( ), hole );    // update new position in hash table
        hole /= 2;                              //      then move the hole up to its parent
    }
    array[hole] = move( array[0] );             // once the hole isnt smaller than it's parent,move x to hole
    table.insert( array[hole].getID( ), hole );             // insert soldier's ID into hash table
    
}


// deleteMin
template<typename Type>
void BinHeap<Type>::deleteMin( )
{
    array[1] = move( array[currentSize--] );
    table.updateValue(array[1].getID( ), 1 );
    percolateDown(1);
}


// makeEmpty
template<typename Type>
void BinHeap<Type>::makeEmpty( )
{
    currentSize = 0;
}

// buildHeap
template<typename Type>
void BinHeap<Type>::buildHeap( )
{
    for( int i = currentSize / 2; i > 0; --i )
        percolateDown( i );
}

// percolateDown
template<typename Type>
void BinHeap<Type>::percolateDown( int hole )
{
    int child;
    Type tmp = move( array[hole] );
    
    while( hole * 2 <= currentSize ) { // while the child exists
        child = hole * 2;                                              // child = left child
        if( child != currentSize && array[child + 1] < array[child] ) // if child isnt last node and right child is less than left child
            ++child;
        if( array[child] < tmp ) {                              // if the child is smaller than the soldier
            array[hole] = move( array[child] );                     // move the child up into the hole
            table.updateValue( array[hole].getID( ), hole );    // update new position in hash table
        } else
            break;
        hole = child;
    }
    array[hole] = move( tmp );                           // move the soldier into the hole
    table.updateValue( array[hole].getID( ), hole );    // update new position in hash table
    array[hole].priority = tmp.priority;               // update priority of soldier

}

// decreaseKey
template<typename Type>
void BinHeap<Type>::decreaseKey( const int ID, int delta ) // pos = soldier id
{
    int hole = table.getPos( ID ); // find soldier in heap
    array[0] = move( array[hole] );
    Type copy = array[0];
    copy.priority -= delta;
    
    while( copy < array[hole / 2] && hole > 1 ){
        array[hole] = move( array[hole / 2] );
        table.updateValue( array[hole].getID( ), hole );    // update new position in hash table
        hole /= 2;
    }
    array[hole] = move( array[0] );
    table.updateValue( array[hole].getID( ), hole );    // update new position in hash table
    array[hole].priority = copy.priority;               // update priority of soldier
    
    
}

// increaseKey
template<typename Type>
void BinHeap<Type>::increaseKey( const int ID, int delta )
{
    int hole = table.getPos( ID );      // set hole to be soldiers position in heap
    array[hole].priority += delta;      // add delta to soldier's priority
    percolateDown( hole );              // percolate soldier down
    
}

// remove
template<typename Type>
void BinHeap<Type>::remove( int ID )
{
    decreaseKey( ID, 100000000 );
    deleteMin( );
    table.remove( ID );
}

// findSoldierPos
template <typename Type>
int BinHeap<Type>::findSoldierPos( const int ID ) const
{
    return table.getPos( ID );
}


// targetSoldier
template<typename Type>
Type& BinHeap<Type>::targetSoldier( const int ID )
{
    return array[ findSoldierPos( ID ) ];
}






