import java.io.*;
import java.util.*;

public class Main {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
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
    }
    
    static class Pair {
        int id;
        int mark;
        
        Pair(int id, int mark) {
            this.id = id;
            this.mark = mark;
        }
    }
    
    public static void main(String[] args) {
        FastReader sc = new FastReader();
        PrintWriter out = new PrintWriter(System.out);
        
        int testCase = sc.nextInt();
        
        for (int t = 0; t < testCase; t++) {
            int n = sc.nextInt();
            int[] ids = new int[n];
            int[] marks = new int[n];
            
            for (int i = 0; i < n; i++) {
                ids[i] = sc.nextInt();
            }
            
            for (int i = 0; i < n; i++) {
                marks[i] = sc.nextInt();
            }
            
            Pair[] students = new Pair[n];
            for (int i = 0; i < n; i++) {
                students[i] = new Pair(ids[i], marks[i]);
            }
            
            int swaps = 0;
            for (int i = 0; i < n; i++) {
                int maxIndex = i;
                for (int j = i + 1; j < n; j++) {
                    if (students[j].mark > students[maxIndex].mark || 
                        (students[j].mark == students[maxIndex].mark && students[j].id < students[maxIndex].id)) {
                        maxIndex = j;
                    }
                }
                if (maxIndex != i) {
                    Pair temp = students[i];
                    students[i] = students[maxIndex];
                    students[maxIndex] = temp;
                    swaps++;
                }
            }
            
            out.println(swaps);
            for (Pair p : students) {
                out.println(p.id + " " + p.mark);
            }
        }
        
        out.close();
    }
}
