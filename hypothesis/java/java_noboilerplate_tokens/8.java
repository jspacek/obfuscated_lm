public class Eight
{
    public static int slowfib(int n) {
      int result = 0;
      if(n == 1 || n == 2)
        result = 1;
      else
        result = slowfib(n-1) + slowfib(n-2);
      return result;
  	}
}
