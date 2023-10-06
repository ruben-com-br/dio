enum class Nivel { BASICO, INTERMEDIARIO, DIFICIL }

class Usuario(val nome: String)

data class ConteudoEducacional(var nome: String, val duracao: Int = 60)

data class Formacao(val nome: String, var conteudos: List<ConteudoEducacional>) {

    val inscritos = mutableListOf<Usuario>()

    fun matricular(usuario: Usuario) {
        inscritos.add(usuario)
        println("Usuário ${usuario.nome} matriculado na formação $nome")
    }
}

fun main() {
    // Criando alguns objetos para testar a matrícula
    val disciplinaKotlin = ConteudoEducacional("Introdução ao Kotlin", 120)
    val disciplinaPOO = ConteudoEducacional("Programação Orientada a Objetos", 180)
    val formacaoKotlin = Formacao("Formação Kotlin", listOf(disciplinaKotlin, disciplinaPOO))

    val usuario1 = Usuario("João")
    val usuario2 = Usuario("Maria")

    formacaoKotlin.matricular(usuario1)
    formacaoKotlin.matricular(usuario2)
}

