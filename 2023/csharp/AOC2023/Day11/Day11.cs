using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Text.RegularExpressions;
using AOC2023.Utilities;


namespace AOC2023
{
    class Day11
    {
        public string input = @"..F7.
.FJ|.
SJ.L7
|F--J
LJ...";


        public void Solve()
        {
            var lines = input.Split("\r\n");

          /*  var expandedRows = (from row in Enumerable.Range(0, lines.length)
                             where lines[row].All(c => c == '.')
                             select row).ToList();
            
            var expandedCols = (from col in Enumerable.Range(0, lines[0].Length)
                                where lines.All(row => row[col] == '.')
                                select col).ToList();

            var galaxiesLoc = (from row in Enumerable.Range(0, lines.Length)
                               from col in Enumerable.Range(0, lines[0].Length)
                               where lines[row][col] == '#'
                               select new Position(row, col)).ToList();
*/
            var watch = Stopwatch.StartNew();
            SolveA();
            watch.Stop();
            Debug.WriteLine($"Elapsed {watch.ElapsedMilliseconds}ms");

            watch = Stopwatch.StartNew();
            SolveB();
            watch.Stop();
            Debug.WriteLine($"Elapsed {watch.ElapsedMilliseconds}ms");
        }

        public void SolveA()
        {
           

        }

        public void SolveB()
        {
           
        }
    }
}
