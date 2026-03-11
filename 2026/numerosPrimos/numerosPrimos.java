import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class numerosPrimos{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arrayNumPrimos;
        int soma;

        System.out.println("Insira o número limite: ");
        int limite = scanner.nextInt();

        arrayNumPrimos = crivoEratostenes(limite);
        soma = somaPrimos(arrayNumPrimos);

        System.out.printf("Os números primos de 2 a %d são: ", limite);
        System.out.println(arrayNumPrimos);
        System.out.printf("A soma do primeiro valor com o último dos números primos é: %d", soma);
        
        scanner.close();
    }

    static ArrayList<Integer> crivoEratostenes(int limite){
        boolean[] numerosPrimos = new boolean[limite+1];
        Arrays.fill(numerosPrimos, true);
        ArrayList<Integer> primos = new ArrayList<>();

        for(int numero = 2; numero <= (int) Math.sqrt(limite); numero++){
            if(numerosPrimos[numero]){
                for(int multiplo = numero * numero; multiplo <= limite; multiplo += numero){
                    numerosPrimos[multiplo] = false;
                }
            }
        }

        for(int indice = 2; indice< numerosPrimos.length; indice++){
            if(numerosPrimos[indice] == true){
                primos.add(indice);
            }
        }

        return primos;
    }
    static int somaPrimos(ArrayList<Integer> arrayNumerosPrimos){
        int ultimoValor = arrayNumerosPrimos.size() - 1;
        int soma = arrayNumerosPrimos.get(0) + arrayNumerosPrimos.get(ultimoValor);

        return soma;
    }
}
    