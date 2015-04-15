#ifndef __project2__Soldier__
#define __project2__Soldier__

#include <string>

using namespace std;

class Soldier
{
public:
    
    Soldier( int ID = 0, bool spartan = false );
    
    bool isSpartan( ) const;
    const int getID( ) const;
    
    bool operator<(const Soldier& rh) const;
    bool operator<=(const Soldier& rh) const;

    int priority;
    int wounds = 0;

private:
    int soldierID;
    bool spartan;
    
    
};


#endif /* defined(__project2__Soldier__) */
