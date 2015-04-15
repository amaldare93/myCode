
#include "Soldier.h"
#include <string>
#include <stdlib.h>
#include <time.h>
#include <iostream>
using namespace std;


// constructor
Soldier::Soldier( int ID, bool spartan )
: soldierID(ID), spartan(spartan)
{    
    if(spartan){
        // priority between 1 and 50
        priority = (rand() % 50) + 1;
    } else {
        // priority between 51 and 1000
        priority = (rand() % 950) + 51;
    }
}

// isSpartan
bool Soldier::isSpartan() const
{
    if(spartan)
        return true;
    else
        return false;
}

// getID
const int Soldier::getID( ) const
{
    return soldierID;
}

// < operator
bool Soldier::operator<(const Soldier& rh) const
{
    if( priority < rh.priority )
        return true;
    else
        return false;
    
}

// <= operator
bool Soldier::operator<=(const Soldier& rh) const
{
    if( priority <= rh.priority )
        return true;
    else
        return false;
    
}