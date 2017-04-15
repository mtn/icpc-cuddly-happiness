
#include <iostream>
#include <queue>
#include <unordered_set>

using namespace std;



int main()
{
    int width;
    int numP;
    cin >> width;
    cin >> numP;

    cout << numP << '\n';

    int* walls = new int[numP+2];
    walls[0] = 0;
    walls[numP + 1] = width;

    for (int i = 0; i < numP; i++)
    {
        cin >> walls[i+1];
        cout << walls[i + 1] << " ";
    }
    cout << '\n';

    priority_queue<int> pq;
    for (int l = 0; l < numP + 1; l++)
    {
        for (int r = 1; r < numP + 2; r++)
        {
            pq.push(walls[r] - walls[l]);
        }
    }

    unordered_set<int> included;
    bool hasOne = 0;
    while(!pq.empty())
    {
        int a = pq.top();
        pq.pop();
        if (included.find(a) == included.end())
        {
            included.insert(a);
            if (hasOne)
                cout << " " << a;
            else cout << a;
        }
    }
    cout << '\n';
}
