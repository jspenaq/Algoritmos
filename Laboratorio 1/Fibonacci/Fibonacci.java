
import java.math.BigInteger;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Sebastian
 */
public class Fibonacci {
    
    // byte
    static byte fibo(byte n) {
        byte a = 0;
        byte b = 1;
        byte aux;
        for (byte i = 0; i < n; i++) {
            aux = (byte) (a+b);
            a = b;
            b = aux;
        }
        return a;
    }
    
    // short
    static short fibo(short n) {
        short a = 0;
        short b = 1;
        short aux;
        for (short i = 0; i < n; i++) {
            aux = (short) (a+b);
            a = b;
            b = aux;
        }
        return a;
    }
    
    // int
    static int fibo(int n) {
        int a = 0;
        int b = 1;
        int aux;
        for (int i = 0; i < n; i++) {
            aux = a + b;
            a = b;
            b = aux;
        }
        return a;
    }
    
    // long
    static long fibo(long n) {
        long a = 0;
        long b = 1;
        long aux;
        for (long i = 0; i < n; i++) {
            aux = a + b;
            a = b;
            b = aux;
        }
        return a;
    }
    
    // BigInteger
    static BigInteger fiboBig(int n) {
        BigInteger a = BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;
        BigInteger aux;
        for (BigInteger i = BigInteger.ZERO; i.compareTo(BigInteger.valueOf(n)) < 0; i = i.add(BigInteger.ONE)) {
            aux = a.add(b);
            a = b;
            b = aux;
        }        
        return a;
    }
    
    // OF byte
    static byte overflow_byte(){
        byte of = 0;
        for (byte i = 0; i < Byte.MAX_VALUE; i++) {
            //System.out.print("fibonacci de " + i + ": ");
            byte fibo = fibo(i);
            //System.out.println(fibo);
            if (fibo < 0) {
                of = i;
                break;
            }
        }
        return of;
    }
    
    // OF short
    static short overflow_short(){
        short of = 0;
        for (short i = 0; i < Short.MAX_VALUE; i++) {
            //System.out.print("fibonacci de " + i + ": ");
            short fibo = fibo(i);
            //System.out.println(fibo);
            if (fibo < 0) {
                of = i;
                break;
            }
        }
        return of;
    }
    
    // OF int
    static int overflow_int(){
        int of = 0;
        for (int i = 0; i < Integer.MAX_VALUE; i++) {
            //System.out.print("fibonacci de " + i + ": ");
            int fibo = fibo(i);
            //System.out.println(fibo);
            if (fibo < 0) {
                of = i;
                break;
            }
        }
        return of;
    }
    
    // OF long
    static long overflow_long(){
        long of = 0;
        for (long i = 0; i < Long.MAX_VALUE; i++) {
            //System.out.print("fibonacci de " + i + ": ");
            long fibo = fibo(i);
            //System.out.println(fibo);
            if (fibo < 0) {
                of = i;
                break;
            }
        }
        return of;
    }
    
    // OF BigInteger
    static int overflow_BigInteger(){
        int of = 0;
        for (int i = 28785; i < 30000; i++) {
            System.out.print("fibonacci de " + i + ": ");
            BigInteger fibo = fiboBig(i);
            //System.out.println(fibo);
            if (fibo.compareTo(BigInteger.ZERO) < 0) {
                of = i;
                break;
            }
        }
        return of;
    }
    
    public static void main(String[] args) {
        byte of_byte = overflow_byte();
        System.out.println("OVERFLOW: byte n = " + of_byte);
        
        short of_short = overflow_short();
        System.out.println("OVERFLOW: short n = " + of_short);
        
        int of_int = overflow_int();
        System.out.println("OVERFLOW: int n = " + of_int);
        
        long of_long = overflow_long();
        System.out.println("OVERFLOW: long n = " + of_long);
                
        /*int of_BigInteger = overflow_BigInteger();
        System.out.println("OVERFLOW: n = " + of_BigInteger);*/
        System.out.println("OVERFLOW: BigInteger n = No hay");
        
        /* OUTPUT:
        OVERFLOW: byte n = 12
        OVERFLOW: short n = 24
        OVERFLOW: int n = 47
        OVERFLOW: long n = 93
        OVERFLOW: BigInteger n = No hay
        */
        
    }

}
