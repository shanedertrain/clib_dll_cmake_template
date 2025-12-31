using System;
using System.Runtime.InteropServices;

internal static class MyLib
{
    [DllImport("mylib", CallingConvention = CallingConvention.Cdecl)]
    internal static extern Int32 mylib_add_i32(Int32 a, Int32 b);
}

public static class Program
{
    public static int Main()
    {
        int got = MyLib.mylib_add_i32(2, 3);
        Console.WriteLine($"mylib_add_i32(2, 3) = {got}");
        return (got == 5) ? 0 : 2;
    }
}
