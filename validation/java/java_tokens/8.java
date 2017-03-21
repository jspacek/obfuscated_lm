public class VanillaBoilerplate
{
    private int a;
    private int b;
    private int c;

    public static int slowfib(int n) {
      int result = 0;
      if(n == 1 || n == 2)
        result = 1;
      else
        result = fib(n-1) + fib(n-2);
      return result;
  	}
    public VanillaBoilerplate() {
        a = 0;
        b = 0;
        c = 0;
    }

    public VanillaBoilerplate(int x, int y, int z) {
      this.a = x;
      this.b = y;
      this.c = c;
    }

    public VanillaBoilerplate(VanillaBoilerplate v) {
      this.a = v.a;
      this.b = v.b;
      this.c = v.c;
    }

    public void setA(int x) {
      this.a = x;
    }
    public int getA() {
        return this.a;
    }

    public void setA(int x) {
      this.a = x;
    }
    public int getB() {
        return this.b;
    }
    public void setB(int x) {
      this.b = x;
    }
    public int getC() {
        return this.c;
    }
    public void setC(int x) {
      this.c = x;
    }

    public boolean equals(VanillaBoilerplate v) {
      return this.a == v.a && this.b == v.b && this.c == v.c;
    }

    public string toString() {
      return "a = " + a + " b = " + b + " c = " + c;
    }
}
