import java.util.ArrayList;

/**
 * @author Sebastian Peña
 */
public class Matrix {

    static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    static int[][] createMatrix(int size, int value) {
        int[][] M = new int[size][size];
        for (int i = 0; i < size; i++) {
            Arrays.fill(M[i], value);
        }
        return M;
    }

    static int[][] multiplyMatrices(int[][] m1, int[][] m2) {
        int[][] result = new int[m1.length][m2[0].length];
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result[i].length; j++) {
                for (int k = 0; k < m1[0].length; k++) {
                    result[i][j] += m1[i][k] * m2[k][j];
                }
            }
        }
        return result;
    }

    static double avgTimes(long[] t) {
        long sum = 0;
        for (long l : t) {
            sum += l;
        }
        return ((double) sum) / t.length;
    }

    public static void main(String[] args) {
        long t0, tf;    // Variables para medir el tiempo en milisegundos
        int test = 10;  // Cantidad de pruebas que se haran por tamaño
        int max = 100;   // Cantidad maxima de tamaños para matrices cuadradas que se multiplicaran
        ArrayList<Double> times = new ArrayList<>(); // Lista para manejar los tiempos

        for (int n = 2; n < max+1; n++) { // n = size
            int m1[][] = createMatrix(n, 1);
            int m2[][] = createMatrix(n, 2);
            int mult[][] = new int[n][n];
            
            
            double sum = 0;
            for (int i = 0; i < test; i++) {
                t0 = System.currentTimeMillis();
                mult = multiplyMatrices(m1, m2);
                tf = System.currentTimeMillis();
                double aux = ((tf - t0) * 0.001 ) / (2 * Math.pow(n, 3.0));
                sum += aux;
            }
            times.add(sum / test); // Avg
            System.out.println("Matrix " + n + ": " + times.get(n-2));
        }
        System.out.println("Times:\n" + (times));

        /* ULTIMAS 11 MATRICES:
        Matrix 90: 2.1262002743484224E-9
        Matrix 91: 3.1184851858683523E-9
        Matrix 92: 1.9905276567765264E-9
        Matrix 93: 1.9891665019388156E-9
        Matrix 94: 1.8661568245957063E-9
        Matrix 95: 2.7409243329931474E-9
        Matrix 96: 2.656159577546296E-9
        Matrix 97: 3.3966163127428996E-9
        Matrix 98: 2.496833802242263E-9
        Matrix 99: 2.2158118270759836E-9
        Matrix 100: 2.0E-9
         */
    }

}
