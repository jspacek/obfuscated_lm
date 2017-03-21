public class Four
{
    private int size;

    public void add(int value) {
        int pos = 0;
        while(pos < size && value > pos) {
            pos++;
        }
    }
}
