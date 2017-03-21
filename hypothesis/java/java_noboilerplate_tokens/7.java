public class Seven
{
    public static int pow(int base, int exp) {
  	   int result = 0;
      if(exp == 0)
        result = 1;
      else
        result = base * pow(base, exp - 1);
      return result;
    }
}
