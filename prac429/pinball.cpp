
#include <iostream>
#include <list>

using namespace std;

class Line
{
   public:
	int x0, x1, y0, y1;
   Line(int x0_, int y0_, int x1_, int y1_) 
   {
	if (y0_ < y1_)
	{
	    y0 = y0_;
	    x0 = x0_;
            y1 = y1_;
	    x1 = x1_;
	}
	else
	{
	    y0 = y1_;
	    x0 = x1_;
	    y1 = y0_;
	    x1 = x0_;
	}
   }

   int isBelow(int x, int y)
   {
	if ((x0 <= x && x <= x1) || (x1 <= x && x <= x0))
	{
	   int yAtX = ((y0-y1)*(x-x1)/(x0-x1)) + y1;
	   if (y >= yAtX) return 1;
	}
	return 0;
   }

   int isAbove(Line* other)
   {
	int fixedX0 = x0 < x1 ? x0 : x1;
	int fixedX1 = x0 < x1 ? x1 : x0;
	int fixedX2 = other->x0 < other->x1 ? other->x0 : other->x1;
	int fixedX3 = other->x0 < other->x1 ? other->x1 : other->x0;

	if (fixedX2 <= fixedX1)
	{
		int otherY = ((y0-y1)*(fixedX2-x1)/(x0-x1))+y1;
		return otherY > ((other->x0 < other->x1) ? other->y0 : other->x1);
	}
	if (fixedX0 <= fixedX3)
	{
		int otherY = ((other->y0-other->y1)*(fixedX0-other->x1)/(other->x0-other->x1))+other->y1;
		return ((x0 < x1) ? y0 : y1) > otherY;
	}
	return y0 > other->y0;
   }

   int print()
   {
	cout << "(" << x0 << ", " << y0 << ") --> (" << x1 << ", " << y1 << ")\n";
   }

};


int main()
{
	int N;
	cin >> N;

	list<Line*> lines;
	for (int i = 0; i < N; i++)
	{
		int x0,x1,y0,y1;
		cin >> x0 >> y0 >> x1 >> y1;
		Line* newLine = new Line(x0, y0, x1, y1);
		list<Line*>::iterator it = lines.begin();
		for (;it != lines.end(); ++it)
		{
			if (newLine->y0 > (*it)->y0)
			{
				lines.insert(it, newLine);
				break;
			}
		}
		if (it == lines.end())
			lines.push_back(newLine);
	}

	int xAt;
	int yAt = 1000001;
	cin >> xAt;
	
	list<Line*>::iterator it = lines.begin();
	
	for (;it != lines.end(); ++it)
	{
		(*it)->print();
		cout << xAt << ", " << yAt << '\n';
		if ((*it)->isBelow(xAt, yAt))
		{
		    
		    xAt = (*it)->x0;
		    yAt = (*it)->y0;	
		}
	}

	cout << xAt << '\n';
}
