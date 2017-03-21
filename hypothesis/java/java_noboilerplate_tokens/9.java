public class Nine
{
  private static boolean isSquare(char[][] mat) {
		final int numRows = 10;
		int row = 0;
		boolean square = true;
		while( square && row < numRows ) {
		    square = ( mat[row] != null) && (mat[row].length == numRows);
        row++;
		}
		return square;
	}
}
