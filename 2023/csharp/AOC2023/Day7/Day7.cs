using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Text.RegularExpressions;

namespace AOC2023
{
    class Day7
    {
        public string input = @"32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483";

        public void Solve()
        {
            var watch = Stopwatch.StartNew();
            SolveA();
            watch.Stop();
            Debug.WriteLine($"Elapsed {watch.ElapsedMilliseconds}ms");

            watch = Stopwatch.StartNew();
            SolveA();
            watch.Stop();
            Debug.WriteLine($"Elapsed {watch.ElapsedMilliseconds}ms");
        }


        private void SolveA()
        {
            var lines = input.Split("\r\n");

            
            Debug.WriteLine($"total ");
        }
    }
}
