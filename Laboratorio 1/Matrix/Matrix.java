import java.util.ArrayList;
import java.util.Arrays;

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
        //System.out.println("Times:\n" + (times));

        /* OUTPUT:
        Matrix 2: 0.0
        Matrix 3: 0.0
        Matrix 4: 0.0
        Matrix 5: 0.0
        Matrix 6: 0.0
        Matrix 7: 0.0
        Matrix 8: 0.0
        Matrix 9: 0.0
        Matrix 10: 0.0
        Matrix 11: 0.0
        Matrix 12: 0.0
        Matrix 13: 0.0
        Matrix 14: 0.0
        Matrix 15: 0.0
        Matrix 16: 0.0
        Matrix 17: 0.0
        Matrix 18: 0.0
        Matrix 19: 0.0
        Matrix 20: 0.0
        Matrix 21: 8.638375985314761E-8
        Matrix 22: 0.0
        Matrix 23: 0.0
        Matrix 24: 0.0
        Matrix 25: 0.0
        Matrix 26: 4.267182521620391E-8
        Matrix 27: 0.0
        Matrix 28: 0.0
        Matrix 29: 0.0
        Matrix 30: 2.962962962962963E-8
        Matrix 31: 0.0
        Matrix 32: 0.0
        Matrix 33: 0.0
        Matrix 34: 0.0
        Matrix 35: 0.0
        Matrix 36: 0.0
        Matrix 37: 1.4806625471344243E-8
        Matrix 38: 0.0
        Matrix 39: 0.0
        Matrix 40: 0.0
        Matrix 41: 0.0
        Matrix 42: 1.0797969981643452E-8
        Matrix 43: 0.0
        Matrix 44: 0.0
        Matrix 45: 0.0
        Matrix 46: 8.218952905399852E-9
        Matrix 47: 0.0
        Matrix 48: 0.0
        Matrix 49: 0.0
        Matrix 50: 5.999999999999999E-9
        Matrix 51: 0.0
        Matrix 52: 0.0
        Matrix 53: 5.373563411406732E-9
        Matrix 54: 0.0
        Matrix 55: 4.808414725770098E-9
        Matrix 56: 0.0
        Matrix 57: 4.049829097212098E-9
        Matrix 58: 0.0
        Matrix 59: 3.895237585147459E-9
        Matrix 60: 0.0
        Matrix 61: 3.304241324163696E-9
        Matrix 62: 3.3567184720217514E-9
        Matrix 63: 0.0
        Matrix 64: 3.0517578125E-9
        Matrix 65: 2.7309968138370504E-9
        Matrix 66: 2.7826474107465842E-9
        Matrix 67: 0.0
        Matrix 68: 2.5442703032770204E-9
        Matrix 69: 2.2830424737221813E-9
        Matrix 70: 2.3323615160349856E-9
        Matrix 71: 2.0954930136262925E-9
        Matrix 72: 2.143347050754458E-9
        Matrix 73: 2.0564653986843765E-9
        Matrix 74: 1.8508281839180304E-9
        Matrix 75: 1.896296296296296E-9
        Matrix 76: 3.530944744131798E-9
        Matrix 77: 3.395154348097509E-9
        Matrix 78: 1.6858005023685499E-9
        Matrix 79: 1.6225896937159132E-9
        Matrix 80: 3.0273437499999996E-9
        Matrix 81: 1.5053411385271365E-9
        Matrix 82: 1.3602530433394756E-9
        Matrix 83: 2.710799650918961E-9
        Matrix 84: 1.3497462477054314E-9
        Matrix 85: 2.523916140850804E-9
        Matrix 86: 1.2577508898587545E-9
        Matrix 87: 2.353823748714888E-9
        Matrix 88: 1.1739293764087152E-9
        Matrix 89: 2.269603344260528E-9
        Matrix 90: 3.223593964334705E-9
        Matrix 91: 2.0568732077004025E-9
        Matrix 92: 1.9905276567765264E-9
        Matrix 93: 2.921588299722635E-9
        Matrix 94: 1.8661568245957063E-9
        Matrix 95: 2.7409243329931474E-9
        Matrix 96: 2.656159577546296E-9
        Matrix 97: 2.574854301595424E-9
        Matrix 98: 2.496833802242263E-9
        Matrix 99: 1.5974457357989653E-9
        Matrix 100: 2.35E-9
        */
    }

}
