# 📦 Ambiente Conda: gestos

## 📋 Descrição
Este ambiente foi configurado para tarefas de **Visão Computacional** e **Deep Learning**, utilizando **Python 3.10** e bibliotecas otimizadas para processamento de imagem, cálculos matemáticos e integração com hardware.

---

## 🔧 Especificações do Core

- **Python:** 3.10.19  
- **Ambiente:** gestos  
- **Localização:** `C:\Users\UMALAB\anaconda3\envs\gestos`

---

## 📚 Bibliotecas Principais

### 👁️ Visão Computacional

| Biblioteca | Versão | Função |
|---|---|---|
| mediapipe | 0.10.20 | Rastreamento de mãos, pose e objetos |
| opencv-python | 4.12.0.88 | Processamento de imagem base |
| opencv-contrib-python | 4.11.0.86 | Módulos extras como SIFT e SURF |

### 🧠 Matemática e Deep Learning

| Biblioteca | Versão | Função |
|---|---|---|
| numpy | 1.26.4 | Base numérica estável para computação científica |
| jax | 0.6.2 | Aceleração de hardware para machine learning |
| jaxlib | 0.6.2 | Backend computacional para JAX |
| scipy | 1.15.3 | Algoritmos científicos avançados |

### 📊 Visualização

| Biblioteca | Versão | Função |
|---|---|---|
| matplotlib | 3.10.8 | Geração de gráficos e visualizações |
| pillow | 12.1.0 | Manipulação básica de imagens |

### 🔌 Hardware e Comunicação

| Biblioteca | Versão | Função |
|---|---|---|
| sounddevice | 0.5.3 | Captura e processamento de áudio |
| pyserial | 3.5 | Comunicação com Arduino e microcontroladores |

---

## 🚀 Comandos Úteis

### Ativar o ambiente

```bash
conda activate gestos
```

### Exportar o ambiente (backup)

```bash
conda env export > gestos_environment.yml
```

---

## 🤖 Integração com Hardware

Como o ambiente inclui **pyserial**, ele pode ser utilizado para conectar sistemas de **visão computacional** a dispositivos físicos.

Exemplos de aplicações:

- Controle de **braço robótico** via gestos
- Acionamento de **luzes ou motores** com reconhecimento de mãos
- Interface gestual para **robótica educacional**

Nesse fluxo, bibliotecas como **MediaPipe** detectam os gestos e o **PySerial** envia comandos para um **Arduino ou outro microcontrolador**.

---

## 📁 Uso recomendado

Este ambiente é adequado para projetos que envolvem:

- Reconhecimento de gestos
- Interfaces homem‑máquina (HMI)
- Prototipagem de sistemas robóticos
- Experimentos de visão computacional
- Integração entre software e hardware

---

**Ambiente mantido para desenvolvimento de visão computacional aplicada.**

