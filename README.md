# 🩺 Detecção e Segmentação de Miomas em Ultrassonografias Pélvicas

Repositório oficial do projeto desenvolvido para a disciplina de **Processamento de Imagem e Sinais (PIS)** do curso de Tecnologia em Inteligência Artificial do **Centro Universitário FMU**.

---

## 👥 Equipe e Contexto
* **Instituição:** FMU | FIAM-FAAM
* **Disciplina:** Processamento de Imagem e Sinais (2026.2)
* **Objetivo:** Implementar um pipeline computacional de visão para auxílio à segmentação de miomas uterinos em exames de ultrassonografia, aplicando conceitos de caracterização de imagens, limiarização matemática e validação por métricas padrão-ouro.

---

## 📋 Artefato 1: Ficha Técnica da Imagem
* **Modalidade:** Ultrassonografia pélvica / ginecológica (USG em escala de cinza).
* **Origem e Licença:** Imagens de domínio público com licença acadêmica verificada.
* **Formato de Arquivo:** PNG (preservando o canal único de intensidade correspondente à reflexão/atenuação acústica).
* **Resolução Espacial:** Grade otimizada (ex: $884 \times 896$ pixels), garantindo amostragem segura acima do limite de Nyquist para estruturas de interesse.
* **Profundidade de Intensidade:** Escala de cinza de 8 bits ($2^8 = 256$ níveis de cinza), ideal para preservar as variações de ecogenicidade do miométrio e do mioma.

---

## ⚙️ Pipeline Metodológico

O sistema implementado no script principal (`main.py`) executa as seguintes etapas sequenciais:

1. **Carregamento e Conversão:** Leitura da imagem em canal único (escala de cinza).
2. **Diagnóstico por Histograma:** Mapeamento da distribuição de intensidades para análise prévia das características luminais da ultrassonografia.
3. **Pré-processamento (Filtragem Espacial):** Aplicação de filtro Gaussiano para atenuação do ruído granulado (*speckle*) característico de exames ultrassonográficos.
4. **Segmentação (Limiarização de Otsu):** Cálculo matemático automático do limiar ótimo de intensidade para separação de classes.
5. **Pós-processamento (Morfologia Matemática):** Execução de operações de *Abertura* (remoção de ruídos isolados) e *Fechamento* (preenchimento de falhas internas na máscara).
6. **Validação Quantitativa:** Comparação da máscara gerada com a referência (*Ground Truth*) utilizando as métricas **Dice** e **IoU (Intersection over Union)**.

---

## 🛠️ Tecnologias Utilizadas
* **Python** (Versão 3.14+)
* **OpenCV** (`cv2`) para manipulação e processamento de imagens.
* **SciPy** e **NumPy** para operações matriciais e processamento científico.
* **Matplotlib** para visualização gráfica de histogramas e máscaras.

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio