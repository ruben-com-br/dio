import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) {
        // Cria um objeto Scanner para receber as entradas do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicita o número da conta
        System.out.print("Por favor, digite o número da Conta: ");
        int numeroConta = scanner.nextInt();

        // Solicita o número da agência
        System.out.print("Por favor, digite o número da Agência: ");
        String agencia = scanner.next();

        // Solicita o nome do cliente
        System.out.print("Por favor, digite o nome do Cliente: ");
        scanner.nextLine(); // Consumir a quebra de linha pendente
        String nomeCliente = scanner.nextLine();

        // Solicita o saldo inicial da conta
        System.out.print("Por favor, digite o saldo inicial: ");
        double saldo = scanner.nextDouble();

        // Fecha o Scanner
        scanner.close();

        // Exibe a mensagem final com os dados informados
        String mensagem = "Olá " + nomeCliente + ", obrigado por criar uma conta em nosso banco, sua agência é "
                + agencia + ", conta " + numeroConta + " e seu saldo " + saldo + " já está disponível para saque.";
        System.out.println(mensagem);
    }
}
