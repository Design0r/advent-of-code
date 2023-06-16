using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

class Day1
{
    static void Main()
    {
        string filePath = "./day_01/input.txt";
        string[] input = File.ReadAllLines(filePath);
        List<List<int>> list = new();
        List<int> tempList = new();
        List<int> elfBagList = new();
        string elfCount =
        foreach (string line in input)
        {
            bool successfulParse = int.TryParse(line, out int number);

            if (successfulParse)
            {
                tempList.Add(number);
                continue;
            }

            list.Add(new List<int>(tempList));
            tempList.Clear();
        }

        foreach (List<int> elfBag in list)
            elfBagList.Add(elfBag.Sum());

        elfBagList.Sort();
        Console.WriteLine($"Part 1: {elfBagList.Last()}");
        int slice = elfBagList.GetRange(elfBagList.Count - 3, 3).Sum();
        Console.WriteLine($"Part 2: {slice}");
    }
}