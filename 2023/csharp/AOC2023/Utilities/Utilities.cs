using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AOC2023.Utilities
{

        public struct Position
        {
            public int x;
            public int y;
            public Position(int xvalue, int yvalue)
            {
                x = xvalue;
                y = yvalue;
            }
            public bool isValid()
            {
                return x != -1 && y != -1;
            }

            public override bool Equals(Object other)
            {
                return x == ((Position)other).x && y == ((Position)other).y;
            }
            public override int GetHashCode()
            {
                return base.GetHashCode();
            }
            static public bool operator ==(Position first, Position second)
            {
                return first.x == second.x && first.y == second.y;
            }

            static public bool operator !=(Position first, Position second)
            {
                return !(first.x == second.x && first.y == second.y);
            }
            static public Position operator +(Position first, Position second)
            {
                return new Position(first.x + second.x, first.y + second.y);
            }
        }

    public struct ItemStringValue
    {
        public string stringValue;
        public int intValue;

        public ItemStringValue(string xvalue, int yvalue)
        {
            stringValue = xvalue;
            intValue = yvalue;
        }
        public bool isValid()
        {
            return stringValue != "";
        }

        public override bool Equals(Object other)
        {
            return stringValue == ((ItemStringValue)other).stringValue && intValue == ((ItemStringValue)other).intValue;
        }
        public override int GetHashCode()
        {
            return base.GetHashCode();
        }
        static public bool operator ==(ItemStringValue first, ItemStringValue second)
        {
            return first.stringValue == second.stringValue;
        }

        static public bool operator !=(ItemStringValue first, ItemStringValue second)
        {
            return first.stringValue != second.stringValue;
        }       
    }

}
