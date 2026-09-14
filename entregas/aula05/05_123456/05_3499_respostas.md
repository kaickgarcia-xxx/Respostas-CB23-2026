# Respostas da Atividade Prática - Aula 05 (Orientação a Objetos e UML)

## Questão 1: Relações de Herança entre as Classes

As classes apresentadas podem ser organizadas em três hierarquias principais de herança:

### 1. Hierarquia de Pessoas e Funcionários
* **Classe Base:** `Pessoa` (Atributos: `nome: str`, `idade: int`).
* **Subclasse Intermediária:** `Funcionário` (Herda `nome` e `idade` de `Pessoa`; adiciona `salario: float` e `carga_horaria: int`).
* **Subclasses Específicas de Funcionário:**
  * `Garçom` (Herda todos os atributos de `Pessoa` e `Funcionário`; possui o método `anotar_pedido`).
  * `Chefe de cozinha` (Herda todos os atributos de `Pessoa` e `Funcionário`; possui o método `preparar`).
  * `Gerente` (Herda todos os atributos de `Pessoa` e `Funcionário`; possui o método `demitir`).

### 2. Hierarquia de Restaurantes
* **Classe Base:** `Restaurante` (Atributos: `nome: str`, `endereco: str`, `telefone: str`).
* **Subclasse:** `Pizzaria` (Herda `nome`, `endereco` e `telefone` de `Restaurante`; adiciona `rodizio: bool`).

### 3. Hierarquia de Iguarias (Comidas)
* **Classe Base:** `Iguaria (comida)` (Atributos: `nome: str`, `preco: float`).
* **Subclasses:**
  * `Pizza` (Herda `nome` e `preco` de `Iguaria`; adiciona `borda_recheada: bool`).
  * `Bolo` (Herda `nome` e `preco` de `Iguaria`; adiciona `formato: str`).

---

## Questão 2: Modelagem da Relação entre Restaurante e Iguaria

A relação entre `Restaurante` e `Iguaria` deve ser modelada como uma **Agregação (1 para N)**.

* **Explicação:** Um restaurante possui um cardápio contendo diversas iguarias (comidas). As iguarias existem independentemente do restaurante.
* **Implementação:** A classe `Restaurante` terá um novo atributo do tipo lista: `cardapio: list[Iguaria]`.

---

## Questão 3: Tipagem dos Argumentos

### `argumento1` — Método `anotar_pedido(argumento1)` em `Garçom`
* **Tipo recomendado:** `list[Iguaria]` (ou uma instância da classe `Pedido`).
* **Justificativa:** Ao anotar um pedido, o garçom recebe uma lista com os itens alimentícios escolhidos pelo cliente.

### `argumento2` — Método `preparar(argumento2)` em `Chefe de cozinha`
* **Tipo recomendado:** `Iguaria` (ou subclasses `Pizza` / `Bolo`).
* **Justificativa:** O chefe de cozinha prepara um item alimentício específico do cardápio.

### `argumento3` — Método `demitir(argumento3)` em `Gerente`
* **Tipo recomendado:** `Funcionário` (ou subclasses `Garçom`, `Chefe de cozinha`).
* **Justificativa:** O gerente realiza a demissão de um colaborador específico do estabelecimento.
