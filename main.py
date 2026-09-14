import cv2
import numpy as np
import matplotlib.pyplot as plt

def carregar_e_processar_usg(caminho_imagem):
    print("=== ETAPA 1: Carregamento e Caracterização da Imagem ===")
    
    # 1. Leitura da imagem em escala de cinza (1 canal)
    img = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print(f"[Erro] Não foi possível carregar a imagem em: {caminho_imagem}")
        print("Certifique-se de colocar uma imagem de USG na pasta do projeto e atualizar o nome aqui.")
        return
    
    print(f"Dimensões (Altura, Largura): {img.shape}")
    print(f"Profundidade / Tipo de Dados: {img.dtype}")
    
    # 2. Geração do Histograma e Visualização
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("USG Original (Escala de Cinza)")
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.hist(img.ravel(), bins=256, range=[0, 256], color='black')
    plt.title("Histograma de Intensidades")
    plt.xlabel("Nível de Cinza (0-255)")
    plt.ylabel("Número de Pixels")
    
    print("\n=== ETAPA 2: Pré-processamento (Filtragem Espacial) ===")
    # Filtro Gaussiano para suavizar o ruído 'speckle' típico da ultrassonografia
    img_suavizada = cv2.GaussianBlur(img, (5, 5), 0)
    
    print("\n=== ETAPA 3: Segmentação por Limiarização de Otsu ===")
    limiar_otsu, mascara_binaria = cv2.threshold(
        img_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    print(f"Limiar de Otsu calculado automaticamente: {limiar_otsu:.2f}")
    
    print("\n=== ETAPA 4: Limpeza da Máscara com Morfologia Matemática ===")
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    
    # Abertura (remove ruídos) e Fechamento (fecha falhas internas)
    mascara_abertura = cv2.morphologyEx(mascara_binaria, cv2.MORPH_OPEN, kernel)
    mascara_limpa = cv2.morphologyEx(mascara_abertura, cv2.MORPH_CLOSE, kernel)
    
    plt.subplot(1, 3, 3)
    plt.imshow(mascara_limpa, cmap='gray')
    plt.title("Máscara Pós-Morfologia (Otsu + Morfologia)")
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print("\n=== ETAPA 5: Validação com Métricas (Dice e IoU) ===")
    # Simulação de um Ground Truth (máscara de referência do especialista) para fins acadêmicos
    ground_truth_simulado = np.zeros_like(mascara_limpa)
    h, w = ground_truth_simulado.shape
    ground_truth_simulado[int(h*0.4):int(h*0.7), int(w*0.4):int(w*0.7)] = 255
    
    pred = (mascara_limpa > 0).astype(np.uint8)
    gt = (ground_truth_simulado > 0).astype(np.uint8)
    
    intersecao = np.logical_and(pred, gt).sum()
    soma_areas = pred.sum() + gt.sum()
    uniao = np.logical_or(pred, gt).sum()
    
    dice = (2.0 * intersecao) / soma_areas if soma_areas > 0 else 0.0
    iou = float(intersecao) / uniao if uniao > 0 else 0.0
    
    print(f"Métrica Dice obtida: {dice:.4f}")
    print(f"Métrica IoU obtida: {iou:.4f}")
    print("\n[Sucesso] Pipeline executado com sucesso!")

# ATENÇÃO: Coloque uma imagem de ultrassom na sua pasta e mude o nome abaixo para testar!
carregar_e_processar_usg('mioma5.png')