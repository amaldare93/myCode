
#ifndef __project2__QuadraticProbing__
#define __project2__QuadraticProbing__

#include <vector>
#include <algorithm>
#include <functional>
#include <string>
using namespace std;

template <typename KeyType>
class HashTable
{
public:
    HashTable( int size = 101 );
    
    bool contains( const KeyType& key ) const;
    void makeEmpty( );
    bool insert( const KeyType& key, int index );
    bool remove( const KeyType& key );
    enum EntryType { ACTIVE, EMPTY, DELETED };
    
    bool updateValue( const KeyType& key, int index );
    int getPos( const KeyType& key ) const;

    
private:
    struct HashEntry
    {
        KeyType key;        // soldierID
        int value;          // heap position
        EntryType info;     // ACTIVE, EMPTY, or DELETED
        
        HashEntry( const KeyType key = 0, int index = 1, EntryType i = EMPTY )
        : key{ key }, value{ index }, info{ i } { }
    };
    
    vector<HashEntry> array;
    int currentSize;
    
    bool isActive( int currentPos ) const;
    void rehash( );
    size_t myhash( const KeyType& x ) const;
    
    bool isPrime( int n );
    int nextPrime( int n );
    
};




#endif /* defined(__project2__QuadraticProbing__) */
