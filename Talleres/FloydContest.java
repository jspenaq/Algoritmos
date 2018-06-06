// Contest: https://www.hackerrank.com/contests/cleverly-hidden-floyd-warshall/challenges/30-pointer
// https://github.com/kennyledet/Algorithm-Implementations/blob/master/Floyd_Warshall/Java/dalleng/FloydWarshall.java

import java.io.*;
import java.util.*;

public class FloydWarshall {

    // graph represented by an adjacency matrix
    public double[][] graph;
    
    static FastReader fr = new FastReader();

    public FloydWarshall(int n) {
        this.graph = new double[n][n];
        initGraph();
    }

    public void initGraph() {
        for (int i = 0; i < graph.length; i++) {
            String line = fr.nextLine().trim();
            //System.out.println(line);
            int j = 0;
            for (char c : line.toCharArray()) {
                //System.out.println("char = " + c);
                //System.out.println("j vale antes de ++: " + j);
                if (i == j) {
                    graph[i][j] = 0;
                }
                else if(c == 'Y') {
                    graph[i][j] = 1;
                    //System.out.println("G = 1");
                }
                else {
                    //System.out.println("\t INFINITY: i = " + i + ", j = " + j);
                    graph[i][j] = Double.POSITIVE_INFINITY;
                }
                j++;
                
            }
        }
    }

    // all-pairs shortest path
    public double[][] floydWarshall() {
        double[][] distances;
        int n = this.graph.length;
        distances = Arrays.copyOf(this.graph, n);

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    distances[i][j] = Math.min(distances[i][j], distances[i][k] + distances[k][j]);
                }
            }
        }

        return distances;
    }

    public static void main(String[] args) throws Exception{
        int N = fr.nextInt();
        int D = fr.nextInt();
        FloydWarshall fw = new FloydWarshall(N);
        double[][] mat = fw.floydWarshall();
        double max = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (mat[i][j] > max) {
                    max = mat[i][j];
                }
            }
        }
        int res = (int)max * D;
        if (res >= 0 && res < 2147000000)
            System.out.println(res);
        else 
            System.out.println("-1");
    }

    static class FastReader {

        BufferedReader br;
        StringTokenizer st;

        FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        FastReader(String fileName) {
            try {
                File file = new File(fileName);
                br = new BufferedReader(new FileReader(file));
            } catch (Exception e) {
                //System.out.println(e.toString());
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }

    } // end FastReader

}
