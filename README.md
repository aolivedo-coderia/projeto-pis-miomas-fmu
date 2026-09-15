# 🩺 Detecção e Segmentação de Miomas em Ultrassonografias Pélvicas

Repositório oficial e documentação técnica do projeto desenvolvido para a disciplina de **Processamento de Imagem e Sinais (PIS)** do curso de Tecnologia em Inteligência Artificial do **Centro Universitário FMU**.

---

## 👥 Equipe e Contexto

* **Instituição:** FMU | FIAM-FAAM
* **Disciplina:** Processamento de Imagem e Sinais (2026.2)
* **Integrantes:**
  * **Ana Claudia de Souza Oliveira (Anny Olivedo)** — RA: [Seu RA Aqui]
* **Objetivo:** Implementar um pipeline computacional de visão para auxílio à segmentação de miomas uterinos em exames de ultrassonografia, aplicando conceitos de caracterização de imagens, limiarização matemática e validação por métricas padrão-ouro.

---

## 📋 Artefato 1: Ficha Técnica e Caracterização da Imagem

| Parâmetro Técnico | Especificação Utilizada | Justificativa Acadêmica |
| :--- | :--- | :--- |
| **Modalidade** | Ultrassonografia Pélvica / Ginecológica | Exame de rotina para identificação de ecogenicidade tecidual. |
| **Formato** | PNG (Canal Único / Escala de Cinza) | Preservação fiel dos níveis de reflexão e atenuação acústica. |
| **Resolução** | 884 x 896 pixels | Grade espacial otimizada para amostragem segura das estruturas. |
| **Profundidade** | 8 bits (256 tons de cinza) | Dinâmica ideal para distinguir o miométrio do tecido miomatoso. |

---

## ⚙️ Pipeline Metodológico

O algoritmo implementado no script principal (`main.py`) executa o fluxo sequencial de processamento:

1. **Carregamento:** Leitura da imagem ultrassonográfica em matriz de intensidade única.
2. **Análise de Histograma:** Mapeamento estatístico da distribuição dos tons de cinza.
3. **Pré-processamento:** Aplicação de filtro Gaussiano para atenuação do ruído granulado (*speckle*).
4. **Segmentação (Otsu):** Cálculo automático do limiar ótimo de separação de classes.
5. **Pós-Morfologia:** Operações de *Abertura* e *Fechamento* para refinamento e limpeza da máscara binária.
6. **Validação:** Cruzamento métrico de similaridade (Dice / IoU) com a referência padrão.

---

## 🛠️ Tecnologias e Dependências

* **Python** (Versão 3.14+)
* **OpenCV (`cv2`)** — Processamento de imagem e matrizes.
* **SciPy & NumPy** — Computação científica e operações matriciais.
* **Matplotlib** — Plotagem de histogramas e exibição de máscaras.

---

## 🚀 Como Executar o Projeto

Clone o repositório e instale as dependências necessárias executando os comandos abaixo no seu terminal:

```bash
# 1. Instalar bibliotecas essenciais
python -m pip install opencv-python scipy numpy matplotlib

# 2. Executar o script principal
python main.py
