#include "BinHeap.cpp"
#include "Soldier.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <vector>
using namespace std;

void vecDelete( vector<int>& vec, int index );

double average( vector<double>& set );
double stanDev( vector<double>& set );

int main(int argc, const char * argv[])
{
    ///////// INPUTS //////////////
    int i = atoi( argv[1] );
    int nSpartans = atoi( argv[2] );
    int nPersians = atoi( argv[3] );

    // stats
    double sWins = 0;
    double pWins = 0;
    vector<double> sSurvivors;
    vector<double> pSurvivors;
    
    clock_t start;
    clock_t end;
    double runTime;
    vector<double> runTimes;
    
    srand( time( NULL ) );
    

    for( int j = 0; j < i; j++ )
    {
        // start clock
        start = clock( );
        
        // build heap and soldier vectors
        BinHeap<Soldier> heap;
        vector<int> livingSpartans;
        vector<int> livingPersians;
    
        // generate soldiers, and insert into heaps
        for( int i = 1; i <= nSpartans; i++ )
        {
            heap.insert( Soldier( i, true ) );
            livingSpartans.push_back( i );
        }
        for( int i = nSpartans+1; i <= nPersians + nSpartans; i++ )
        {
            heap.insert( Soldier( i, false ) );
            livingPersians.push_back( i );
        }
    
        // Event simulation
        while( !livingSpartans.empty( ) || !livingPersians.empty( ) )
        {
            if( heap.findMin( ).isSpartan( ) ) // if Spartan
            {
                // select random, living persian from livingPersians vector
                int randIndex = rand( ) % livingPersians.size( );
                int targetID = livingPersians[ randIndex ];
            
                // Kill (remove from heap, hash, and vector)
                heap.remove( targetID );
                vecDelete( livingPersians, randIndex );
            
                // fall back in heap
                heap.increaseKey( heap.findMin( ).getID( ), ( rand( ) % 6) + 1 );
            }
            else // if persian
            {
                // roll dice (5% or 1 in 20)
                int d20 = ( rand( ) % 20 ) + 1;
                if( d20 == 1 )
                {
                    // select random, living spartan from livingSpartans
                    int randIndex = rand( ) % livingSpartans.size( );
                    int targetID = livingSpartans[ randIndex ];
            
                    // Attack
                    if( heap.targetSoldier( targetID ).wounds < 2 )
                    {
                        heap.targetSoldier( targetID ).wounds++;
                        heap.increaseKey( targetID, (rand( ) % 4 ) + 1 );
                    }
                    else if( heap.targetSoldier( targetID ).wounds == 2 )
                    {
                        // remove spartan
                        heap.remove( targetID );
                        vecDelete( livingSpartans, randIndex );
                    
                        // spartan fury
                        for( int i = 0; i < livingSpartans.size( ); i++ )
                        {
                            heap.decreaseKey( livingSpartans[i] , ( rand( ) % 2 ) + 1 );
                        }
                    }
                }
                // fall back in heap
                heap.increaseKey( heap.findMin( ).getID( ), (rand( ) % 51) + 10 );
            }
            if( livingSpartans.empty( ) )
            {
                pSurvivors.push_back( livingPersians.size( ) );
                cout << "Persians Win with " << livingPersians.size( ) << " soldiers remaining. ";
                pWins++;
                break;
            }
            else if ( livingPersians.empty( ) )
            {
                sSurvivors.push_back(livingSpartans.size( ) );
                cout << "Spartans Win with " << livingSpartans.size( ) << " soldiers remaining. ";
                sWins++;
                break;
            }
        }
        // end clock
        end = clock( );
        runTime = difftime( end, start ) / CLOCKS_PER_SEC;
        runTimes.push_back( runTime );
        cout << "Time: " << runTime << endl;
    }

    cout << "\nPersian Victories: " << pWins << endl;
    cout << "Spartan Victories: " << sWins << endl << endl;
    
    cout << "Average Run Time: " << average( runTimes ) << " seconds" << endl;
    cout << "Standard Deviation: " << stanDev( runTimes ) << endl << endl;
    
    cout << "Average Persian Survivors: " << average( pSurvivors ) << endl;
    cout << "Standard Deviation: " << stanDev( pSurvivors ) << endl << endl;

    cout << "Average Spartan Survivors: " << average( sSurvivors ) << endl;
    cout << "Standard Deviation: " << stanDev( sSurvivors ) << endl << endl;

    return 0;
}

    
void vecDelete( vector<int>& vec, int index )
{
    vec[ index ] = vec.back( );
    vec.pop_back( );
}

double average( vector<double>& set )
{
    double sum = 0;
    for( int i = 0; i < set.size(); i++ )
    {
        sum += set[i];
    }
    return sum / set.size();
}

double stanDev( vector<double>& set )
{
    double mean = average( set );
    vector<double> difSquared;
    for( int i = 0; i < set.size(); i++ )
    {
        difSquared.push_back( pow( (set[i] - mean), 2 ) );
    }
    
    return sqrt( average( difSquared ) );
}

















