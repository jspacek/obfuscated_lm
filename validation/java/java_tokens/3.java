import java.awt.Rectangle;

public class VanillaBoilerplate
{
    private int a;
    private int b;
    private int c;

    public static void ohsocreative() {
      Rectangle r1 = new Rectangle(0,0,5,5);
  		System.out.println("In method go. r1 " + r1 + "\n");
  		r1.setSize(10, 15);
  		System.out.println("In method go. r1 " + r1 + "\n");
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
