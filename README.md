# Verificação e Validação: Cálculo da Média de Três Notas com TDD

Este repositório contém uma implementação do cálculo da média de três notas utilizando Test-Driven Development (TDD). O projeto foi desenvolvido em uma única branch, seguindo o processo de TDD com as fases **Red**, **Green** e **Refactor** para garantir a precisão e a robustez do algoritmo.

## 📋 Objetivo

O objetivo deste projeto é aplicar o TDD para desenvolver um algoritmo que calcule a média de três notas, garantindo sua funcionalidade e lidando com diferentes cenários e casos de borda através de testes unitários.

---

## 📁 Estrutura do Projeto

```plaintext
Verificacao-e-Validacao/
├── media_calculadora.py         # Código para calcular a média das notas
└── test_media_calculadora.py     # Testes unitários para validação do cálculo
```

- **`media_calculadora.py`**: Contém a função `calcular_media` que implementa o cálculo da média de três notas.
- **`test_media_calculadora.py`**: Inclui os testes unitários para validar o cálculo da média em diversos cenários.

---

## ⚙️ Como Executar

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/Lufine/Verificacao-e-Validacao.git
   cd Verificacao-e-Validacao
   ```
2. **Instale o Python** (caso ainda não o tenha).

3. **Execute os Testes**:
   ```bash
   python -m unittest test_media_calculadora.py
   ```

## 🧪 Testes Implementados

Os testes cobrem diferentes cenários, incluindo:

- **Cálculo básico**: Verifica a média de valores comuns.
- **Notas iguais a zero**: Valida se o cálculo é feito corretamente com notas mínimas.
- **Notas no valor máximo**: Verifica se a média é calculada corretamente para notas máximas.
- **Notas decimais**: Confirma a precisão com números decimais, arredondando para duas casas decimais.

---

## 🛠️ Processo de Desenvolvimento (TDD)

O processo de desenvolvimento seguiu as fases do TDD:

1. **Fase Red**: Escrevemos os testes unitários antes da implementação da função.
2. **Fase Green**: Implementamos a função `calcular_media` para passar nos testes.
3. **Fase Refactor**: Melhoramos a função para garantir arredondamento preciso e qualidade do código, mantendo o comportamento original.
