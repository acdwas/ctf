package com.example.mynative;

public class MainActivity {
    static {
        System.loadLibrary("mynative");
    }


    public final native String stringFromJNI();

    public final native String webFromJNI();



    public static void main(String[] args) {
        // Wywołanie funkcji natywnej
        String result = new MainActivity().stringFromJNI();
        String result1 = new MainActivity().stringFromJNI();
        System.out.println(result);
        System.out.println(result1);
    }
}

