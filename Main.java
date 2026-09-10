package com.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Calculadora calculadora = new Calculadora();
        Scanner scanner = new Scanner(System.in);

        boolean salir = false;

        while (!salir) {
            System.out.println("\n--- CALCULADORA ---");
            System.out.println("1. Sumar");
            System.out.println("2. Restar");
            System.out.println("3. Multiplicar");
            System.out.println("4. Dividir");
            System.out.println("5. Salir");
            System.out.print("Elige una opcion: ");

            int opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.println("vamos a sumar");
                    System.out.print("Ingresa el primer numero: ");
                    double a = scanner.nextDouble();
                    System.out.print("Ingresa el segundo numero: ");
                    double b = scanner.nextDouble();
                    double resultadoSuma = calculadora.suma(a, b);
                    System.out.println(" el resultado de la suma es: " + resultadoSuma);
                    break;

                case 2:
                    System.out.println("vamos a restar");
                    System.out.print("Ingresa el primer numero: ");
                    double c = scanner.nextDouble();
                    System.out.print("Ingresa el segundo numero: ");
                    double d = scanner.nextDouble();
                    double resultadoResta = calculadora.resta(c, d);
                    System.out.println(" el resultado de la resta es: " + resultadoResta);
                    break;

                case 3:
                    System.out.println("vamos a multiplicar");
                    System.out.print("Ingresa el primer numero: ");
                    double e = scanner.nextDouble();
                    System.out.print("Ingresa el segundo numero: ");
                    double f = scanner.nextDouble();
                    double resultadoMultiplicacion = calculadora.multipliacion(e, f);
                    System.out.println(" el resultado de la multiplicacion es: " + resultadoMultiplicacion);
                    break;

                case 4:
                    System.out.println("vamos a dividir");
                    System.out.print("Ingresa el primer numero: ");
                    double g = scanner.nextDouble();
                    System.out.print("Ingresa el segundo numero: ");
                    double h = scanner.nextDouble();
                    if (h == 0) {
                        System.out.println("Error: no se puede dividir entre cero.");
                    } else {
                        double resultadoDivision = calculadora.divsion(g, h);
                        System.out.println(" el resultado de la division es: " + resultadoDivision);
                    }
                    break;

                case 5:
                    salir = true;
                    System.out.println("Saliendo del programa...");
                    break;

                default:
                    System.out.println("Opcion invalida, intenta de nuevo.");
            }
        }

        scanner.close();
    }
}

