
import java.util.Scanner;
import java.lang.Comparable;
import java.util.PriorityQueue;
import java.util.HashSet;

import java.lang.Math;

public class KitchenSink
{
  public static SinkState startState(int[] capacities)
  {
    int[] fluidLevels = new int[capacities.length];
    fluidLevels[0] = capacities[0];
    for (int i = 1; i < capacities.length; i++)
      fluidLevels[i] = 0;
    return new SinkState(0, fluidLevels);
  }

  public static SinkState newState(int[] capacities, SinkState state, int start, int end)
  {
    if (start == end) return null;
    // Get the amount of liquid to transfer from cup start to cup end
    // this maxed out at the capacity of cup end and the total liquid in start
    int transfer = Math.min(state.fluidLevels[start], capacities[end] - state.fluidLevels[end]);
    if (transfer == 0) return null;

    int[] newlevels = new int[state.fluidLevels.length];
    for (int i = 0; i < newlevels.length; i++)
    {
      newlevels[i] = state.fluidLevels[i] + (i == start ? -transfer : i == end ? transfer : 0);
    }
    return new SinkState(state.fluidTransfered + transfer, newlevels);
  }

  public static class SinkState implements Comparable<SinkState>
  {
    private int fluidTransfered;
    private int[] fluidLevels;

    public SinkState(int fluidTransfered, int[] fluidLevels)
    {
      this.fluidTransfered = fluidTransfered;
      this.fluidLevels = fluidLevels;
    }

    public int getFirst()
    {
      return this.fluidLevels[0];
    }

    public int getFluid()
    {
      return this.fluidTransfered;
    }

    public int compareTo(SinkState other)
    {
      return this.fluidTransfered - other.fluidTransfered;
    }

    public boolean equals(Object o)
    {
      if (o == null) return false;
      if (!(o instanceof SinkState)) return false;
      SinkState other = (SinkState) o;
      if (this.fluidTransfered < other.fluidTransfered) return false;
      for (int i = 0; i < this.fluidLevels.length; i++)
      {
        if (this.fluidLevels[i] != other.fluidLevels[i]) return false;
      }
      return true;
    }

    public int hashCode()
    {
      int hashCode = 0;
      for (int i = 0; i < this.fluidLevels.length; i++)
      {
        hashCode <<= 6;
        hashCode |= this.fluidLevels[i];
      }
      return hashCode;
    }

    public String toString()
    {
      String str = this.fluidTransfered + ": (";
      for (int i = 0; i < this.fluidLevels.length; i++)
      {
        if (i != 0) str += ", ";
        str += fluidLevels[i];
      }
      return str + ")";
    }
  }

  public static void main(String[] args)
  {
    // Create a new scanner of standard input
    Scanner scanner = new Scanner(System.in);

    int numBuckets = scanner.nextInt();
    int[] capacities = new int[numBuckets];
    for (int i = 0; i < numBuckets; i++)
    {
      capacities[i] = scanner.nextInt();
    }
    int goal = scanner.nextInt();

    SinkState startState = startState(capacities);
    PriorityQueue<SinkState> pq = new PriorityQueue<SinkState>();
    HashSet<SinkState> set = new HashSet<SinkState>();
    pq.add(startState);
    set.add(startState);

    while (pq.size() > 0)
    {
      // Get and remove first element from queue
      SinkState cur = pq.poll();
      if (cur.getFirst() == goal)
      {
        System.out.println(cur.getFluid());
        return;
      }

      for (int start = 0; start < numBuckets; start++)
      {
        for (int end = 0; end < numBuckets; end++)
        {
          SinkState next = newState(capacities, cur, start, end);
          if (next != null && !set.contains(next))
          {
            pq.add(next);
            set.add(next);
          }
        }
      }
    }
    System.out.println("impossible");
  }
}
