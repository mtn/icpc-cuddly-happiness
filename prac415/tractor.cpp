
#include <iostream>
#include <unordered_set>
#include <utility>

using namespace std;

struct pair_hash{
    inline std::size_t operator()(const pair<unsigned int, unsigned int>&v)const{
        return v.first ^ v.second;
    }
};

unordered_set<pair<unsigned int, unsigned int>, pair_hash> visited;
unsigned int width;
unsigned int height;

int memofunction(unsigned int x, unsigned int y, unsigned int n)
{
    if (x < 0 || y < 0 || x >= width || y >= height) return 0;
    if (visited.find(pair<unsigned int,unsigned int>(x, y)) != visited.end()) return 0;
    int out = 1+memofunction(x+(1 << (n-1)), y, n+1)+memofunction(x, y+(1<<(n-1)), n+1);
    visited.insert(pair<unsigned int,unsigned int>(x, y));
    return out;
}
int main(){
    int numTrials;
    cin >> numTrials;
    for(int i = 0; i < numTrials; i++){
        cin >> width >> height;
        width++;
        height++;
        visited.clear();

        cout << memofunction(0,0,1) << '\n';
    }
}
