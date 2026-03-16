# 📂 Documentação do Ambiente: gestos

Este documento detalha a configuração, instalação e uso do ambiente de desenvolvimento focado em **Visão Computacional Aplicada** e **Integração com Hardware**.

---

## 📋 Visão Geral

O ambiente **gestos** foi projetado para rodar modelos de detecção de pontos de referência (*landmarks*) em tempo real via **MediaPipe**, com processamento de imagem otimizado pelo **OpenCV** e capacidade de resposta física através de protocolos **Serial**.

---

## 🛠️ Configuração do Sistema

### Pré‑requisitos

* Anaconda ou Miniconda instalado
* Python **3.10.19** (versão escolhida pela estabilidade com pacotes de ML)
* Câmera funcional para testes de visão computacional

---

## ⚙️ Instalação Passo a Passo

Para replicar o ambiente exatamente como configurado:

### 1. Criação do Container

```bash
conda create -n gestos python=3.10.19 -y
conda activate gestos
```

### 2. Dependências de Processamento e ML

```bash
pip install numpy==1.26.4 scipy==1.15.3 jax==0.6.2 jaxlib==0.6.2
```

### 3. Dependências de Visão e Interface

```bash
pip install opencv-python==4.12.0.88 opencv-contrib-python==4.11.0.86 mediapipe==0.10.20
```

### 4. Hardware e Utilitários

```bash
pip install sounddevice==0.5.3 pyserial==3.5 matplotlib==3.10.8 pillow==12.1.0
```

---

## 🏗️ Arquitetura do Código de Exemplo

O script de teste básico segue o fluxo clássico de um pipeline de **Visão Computacional em tempo real**:

1. **Entrada**
   Captura de frames utilizando `cv2.VideoCapture`.

2. **Pré‑processamento**
   Conversão de cores de **BGR → RGB**.

3. **Inferência**
   Processamento pelo modelo `mp.solutions.hands`.

4. **Saída de Dados**
   Coordenadas normalizadas `(x, y, z)` dos **21 pontos da mão**.

5. **Ação (Opcional)**
   Envio de comandos via `serial.Serial` para microcontroladores.

---

## 🚨 Notas de Manutenção (Realismo Técnico)

### Conflitos de Versão

O **MediaPipe** é sensível a versões do `protobuf`. Caso ocorra erro de importação, evite atualizar o pacote manualmente sem validar compatibilidade com **jax**.

### Performance

Para maior fluidez, mantenha:

```python
static_image_mode=False
```

Isso permite que o MediaPipe utilize **tracking entre frames**, evitando detecção completa a cada ciclo.

### Comunicação Serial

O `pyserial` bloqueia a porta **COM** enquanto o script está rodando.

Sempre finalize o script antes de tentar enviar um novo firmware para o **Arduino**.

---

## 🚀 Como Executar

Sempre ative o ambiente antes de rodar qualquer script:

```bash
conda activate gestos
python seu_script.py
```

---

**Ambiente mantido por:** UMALAB
**Última atualização:** Março de 2026
