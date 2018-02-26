import java.util.Arrays;

/**
 *
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

    static int[][] addMatrices(int[][] m1, int[][] m2) {
        int[][] result = new int[m1.length][m1[0].length];
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result.length; j++) {
                result[i][j] = m1[i][j] + m2[i][j];
            }
        }
        return result;
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
    
    static long avgTimes(long[] t) {
        int sum = 0;
        for (long l : t) {
            sum += l;
        }
        return sum / t.length;
    }
    
    public static void main(String[] args) {
        long t0, tf;    // Variables para medir el tiempo en milisegundos
        int test = 10;  // Cantidad de pruebas que se haran
        long[] times = new long[test];

        int size = 500;
        int m1[][] = createMatrix(size, 1);
        int m2[][] = createMatrix(size, 2);
        
        System.out.println("Addition:");
        int add[][];
        for (int i = 0; i < test; i++) {
            t0 = System.currentTimeMillis();
            add = addMatrices(m1, m2);
            tf = System.currentTimeMillis();
            times[i] = tf - t0;
        }
        //printMatrix(add);
        System.out.println("Times: " + Arrays.toString(times));
        System.out.println("Average: " + avgTimes(times) + " miliseconds");
        System.out.println("--------------------");
        
        System.out.println("Multiplication:");
        int mult[][];
        for (int i = 0; i < test; i++) {
            t0 = System.currentTimeMillis();
            mult = multiplyMatrices(m1, m2);
            tf = System.currentTimeMillis();
            times[i] = tf - t0;
        }
        //printMatrix(mult);
        System.out.println("Times:" + Arrays.toString(times));
        System.out.println("Average: " + avgTimes(times) + " miliseconds");
        
        /* OUTPUT:
        Addition:
        Times: [16, 0, 0, 0, 0, 0, 16, 0, 0, 0]
        Average: 3 miliseconds
        --------------------
        Multiplication:
        Times:[468, 457, 797, 816, 801, 786, 802, 782, 786, 771]
        Average: 726 miliseconds
        */
    }

}
