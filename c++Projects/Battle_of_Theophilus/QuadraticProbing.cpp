
#include "QuadraticProbing.h"
#include <iostream>
using namespace std;


// constructor
template <typename KeyType>
HashTable<KeyType>::HashTable( int size ) : array( nextPrime( size ) )
{
    makeEmpty( );
}

// contains
template <typename KeyType>
bool HashTable<KeyType>::contains( const KeyType& x ) const
{
    return isActive( x );
}

// makeEmpty
template <typename KeyType>
void HashTable<KeyType>::makeEmpty( )
{
    currentSize = 0;
    for( auto & entry : array )
        entry.info = EMPTY;
}

// insert
template <typename KeyType>
bool HashTable<KeyType>::insert( const KeyType& x, int index )
{
    array[x].key = x;
    array[x].value = index;    // location of soldier in heap
    array[x].info = ACTIVE;
    
    // Rehash
    if( ++currentSize > array.size( ) / 2 )
        rehash( );
    
    return true;
}

// remove
template <typename KeyType>
bool HashTable<KeyType>::remove( const KeyType& x )
{
    if( !isActive( x ) )
        return false;
    
    array[x].info = DELETED;
    return true;
}

// updateValue
template <typename KeyType>
bool HashTable<KeyType>::updateValue( const KeyType& key, int index )
{
    if( !isActive( key ) )
        return false;
    
    array[key].value = index;
    return true;
    
    
}

// getPos
template <typename KeyType>
int HashTable<KeyType>::getPos( const KeyType& key ) const
{
    if( !isActive( key ) )
        return 0;
    
    return array[key].value;
}


// isActive
template <typename KeyType>
bool HashTable<KeyType>::isActive( int currentPos ) const
{
    return array[currentPos].info == ACTIVE;
}


// rehash
template <typename KeyType>
void HashTable<KeyType>::rehash( )
{
    vector<HashEntry> oldArray = array;
    
    // Create new double-sized, empty table
    array.resize( nextPrime( 2 * oldArray.size( ) ) );
    for( auto & entry : array )
        entry.info = EMPTY;
    
    // Copy table over
    currentSize = 0;
    for( auto & entry : oldArray )
        if( entry.info == ACTIVE )
            insert( move( entry.key ), entry.value );
}

// myhash
template <typename KeyType>
size_t HashTable<KeyType>::myhash( const KeyType &x ) const
{
    static hash<KeyType> hf;
    return hf( x ) % array.size( );
}

// isPrime
template <typename KeyType>
bool HashTable<KeyType>::isPrime( int n )
{
    if( n == 2 || n == 3 )
        return true;
    
    if( n == 1 || n % 2 == 0 )
        return false;
    
    for( int i = 3; i * i <= n; i += 2 )
        if( n % i == 0 )
            return false;
    
    return true;
}

// nextPrime
template <typename KeyType>
int HashTable<KeyType>::nextPrime( int n )
{
    if( n % 2 == 0 )
        ++n;
    
    while( !isPrime( n ) )
        n += 2;
    
    return n;
}
