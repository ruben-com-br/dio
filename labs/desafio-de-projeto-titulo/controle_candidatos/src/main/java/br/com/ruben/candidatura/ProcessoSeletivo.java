package br.com.ruben.candidatura;

import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class ProcessoSeletivo {
  public static void main(String[] args) {
    String [] candidatos = {"FELIPE","MARCIA","JULIA","PAULO","AUGUSTO"};
    imprimirSelecionados();
    for(String candidato:candidatos){
      entrandoEmContato(candidato);
    }
  }

  static void entrandoEmContato(String candidato){
    int tentativasRealizadas = 1;
    boolean continarTentando = true;
    boolean atendeu = false;
    do {
      atendeu = atender();
      continarTentando = !atendeu;
      if ( continarTentando ) tentativasRealizadas ++;
      else System.out.println("CONTATO REALIZADO COM SUCESSO!");
    } while ( continarTentando && tentativasRealizadas < 3 ); 

    if ( atendeu ) System.out.println("CONEGUIMOS CONTATO COM " + candidato + " NA " + tentativasRealizadas);
    else System.out.println("NÃO CONSEGUIMOS CONTATO COM " + candidato + " NÚMERO MÁXIMO");
  }

  static boolean atender() {
     return new Random().nextInt(3) == 1;
  }

  static void imprimirSelecionados(){
    String [] candidatos = {"FELIPE","MARCIA","JULIA","PAULO","AUGUSTO"};

    System.out.println("Imprimindo a lita de candidatos informandoo índice do elemento");

    for(int indice=0; indice < candidatos.length; indice++){
      System.out.println("O candidato de nº " + (indice+1) + " é " + candidatos[indice]);
    }

    System.out.println("Forma abreviada de interação por each");

    for(String candidato:candidatos){
      System.out.println("O candidato selecionado foi " + candidato);
    }
  }


  static void selecaoCandidatos(){
    String [] candidatos = {"FELIPE","MARCIA","JULIA","PAULO","AUGUSTO","MONICA","FABRICIO","MIRELA","DANIELA"};

    int candidatosSelecionados = 0;
    int candidatoAtual = 0;
    double salarioBase = 2000.0;
    while( candidatosSelecionados < 5 && candidatoAtual < candidatos.length){
      String candidato = candidatos[candidatoAtual];
      double salarioPretendido = valorPretendido();

      System.out.println("O candidato " + candidato + " solicitou este valor de salário " + salarioPretendido);
      if(salarioBase >= salarioPretendido){
        System.out.println("LIGAR PARA O CANDIDATO");
        candidatosSelecionados++;
      }
      candidatoAtual++;
    }


  }



  static double valorPretendido(){
    return ThreadLocalRandom.current().nextDouble(1800,2200);
  }

  static void analisarCandidato(double salarioPretendido){
    double salarioBase = 2000.0;
    if(salarioBase > salarioPretendido){
      System.out.println("LIGAR PARA O CANDIDATO");
    } else if (salarioBase == salarioPretendido){
      System.out.println("LIGAR PARA O CANDIDATO COM CONTRA PROPOSTA");
    } else {
      System.out.println("AGUARDANDO O RESULTADO DOS DEMAIS CANDIDATOS");
    }
  }
}
