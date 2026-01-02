# 🎬 Agentic RAG Anime Recommender System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://appudtzei3tyyttd6xjhwur.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Star](https://img.shields.io/github/stars/Ratnesh-181998/Agentic-RAG-Anime-Recommender-System?style=social)](https://github.com/Ratnesh-181998/Agentic-RAG-Anime-Recommender-System)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/ratneshkumar1998/)

![Banner](assets/banner.png)

> **A production-grade, Agentic Retrieval-Augmented Generation (RAG) system for semantic anime discovery. Powered by Groq, LangChain, and ChromaDB.**

---

## 📍 Contents
- [🌟 Overview & Core Mission](#-overview--core-mission)
- [🏷️ Tech Stack & Keywords](#️-tech-stack--keywords)
- [🏗️ System Architecture](#️-system-architecture)
- [� Project Structure](#-project-structure)
- [�📱 Interactive UI Showcase](#-interactive-ui-showcase)
- [🚀 LLMOps & Deployment Playbook](#-llmops--deployment-playbook)
- [� Performance Benchmarks](#-performance-benchmarks)
- [�🛠️ Developer Setup](#️-developer-setup)
- [�️ Future Roadmap](#️-future-roadmap)
- [📞 Contact & Networking](#-contact--networking)

---

## 🌟 Overview & Core Mission

### 🎯 The Challenge
In a world with thousands of anime titles, generic category-based recommendation systems fail to capture the **nuance of human emotion, atmosphere, and complex plot themes**. 

### ✅ The Solution
The **Agentic RAG Anime Recommender** is an advanced AI platform that implements **Semantic Search** and **Personalized Discovery** using a **Content-Based Filtering** approach enhanced by Large Language Models (**LLMs**). It understands the "vibe" of a query and provides a reasoning layer that explains the logic behind every suggestion.

> **Pro Tip**: Use queries like *"Find me an anime that feels like a lonely evening in a cyberpunk city"* to see the power of semantic retrieval.

---

## 🌐🎬 Live Demo
🚀 **Try it now:**
- **Streamlit Profile** - https://share.streamlit.io/user/ratnesh-181998
- **Project Demo** - https://agentic-rag-anime-recommender-system-dhsvh7zgrejeed2ghprr3d.streamlit.app/

---

## 🏷️ Tech Stack & Keywords

### 🧠 Expertise Matrix

| Category | Keywords & Skills |
| :--- | :--- |
| **🤖 AI/ML** | **LLM (Llama 3.1)**, **RAG**, **Agentic AI**, **Semantic Search**, **Vector Embeddings (MiniLM)**, **Contextual Retrieval** |
| **🛠️ Tech Stack** | **Groq LPU Acceleration**, **LangChain**, **ChromaDB (HNSW Index)**, **HuggingFace Transformers**, **Python**, **Streamlit Premium UI** |
| **☁️ LLMOps / AIOps** | **Docker Containerization**, **Kubernetes (K8s)**, **GKE**, **CI/CD Pipelines (GitHub Actions)**, **Grafana Observability** |
| **🎯 Domain** | **Recommender Systems**, **Content-Based Filtering**, **Cold Start Mitigation**, **Persona-Based Discovery** |

---

## 🏗️ System Architecture

### 📊 Tactical Data Flow
```mermaid
graph LR
    subgraph Data Layer
    CSV[(Anime Metadata)] --> EMD[HuggingFace Embeddings]
    EMD --> VDB[(ChromaDB)]
    end

    subgraph Logic Layer
    User([User Query]) --> VDB
    VDB -- Top-K Matches --> RE[Groq Reasoning Engine]
    RE -- Agentic Insight --> UI
    end

    subgraph Presentation Layer
    UI[[Streamlit Premium UI]]
    end
```

### 🖼️ Architecture & Workflow Visuals

<details>
<summary><b>📐 View High-Level & Low-Level Design (HLD/LLD)</b></summary>

![HLD & LLD](assets/hld_lld.png)
</details>

<details>
<summary><b>🔄 View Agentic Workflow Detail</b></summary>

![Workflow](assets/workflow.png)
</details>

### 🔍 Process Deep Dive
1.  **Ingestion Phase**: CSV metadata is normalized, tokenized, and transformed into 384-dimensional dense vectors using `all-MiniLM-L6-v2`.
2.  **Indexing Phase**: **ChromaDB** maintains a persistent HNSW index for sub-10ms nearest neighbor search.
3.  **Inference Phase**: **Groq (LPU)** processes retrieved context and user intent to generate a reasoned analysis.
4.  **Presentation Phase**: Real-time rendering of results with interactive UX feedback loops and CSS transitions.

---

## � Project Structure

```text
├── Code/                   # Application Pipeline, Logic & UI Components
├── Dataset Used/           # Raw Metadata Source (CSV)
├── Project Doc/            # Detailed Documentation & Checklists
├── assets/                 # Brand Assets, Architecture Diagrams & UI Screenshots
├── README.md               # Hero Documentation & Professional Overview
├── LICENSE                 # MIT Open Source License
├── requirements.txt        # Python Dependencies
├── Dockerfile              # Containerization Script
├── setup.py                # Package Configuration
├── chroma_db/               # Persistent Vector Database (ChromaDB)
└── llmops-k8s.yaml         # Kubernetes Orchestration Blueprint
```

---

## 📱 Interactive UI Showcase & Tab Guide

The application features a premium, multi-tab interface designed for both casual discovery and technical deep-dives.

### � Tab 1: Demo Project (Core Experience)
*   **Purpose**: The central interaction point for users to get recommendations.
*   **Features**:
    *   **⚡ Quick Try Grid**: 16 categorized buttons (e.g., *Cyberpunk*, *Dark Fantasy*) for one-click exploration.
    *   **🔍 Semantic Search Bar**: A deep-learning powered input where users can describe their "ideal vibe" in natural language.
    *   **💾 Query History**: Persistent track of previous searches with the ability to copy or download results as `.txt` files.
    *   **🧠 AI Reasoning Engine**: Not just a list, but a detailed analysis of *why* each anime was recommended.

### 📖 Tab 2: About Project (The Vision)
*   **Purpose**: Outlines the problem statement and the architectural "Why".
*   **Features**:
    *   **💡 Problem vs. Solution**: A clear breakdown of the challenges in traditional recommendation systems and how Agentic RAG solves them.
    *   **🎯 Project Goals**: Highlighting scalability, sub-second latency, and semantic accuracy.

### 🔧 Tab 3: Tech Stack (Technical Pedigree)
*   **Purpose**: A live monitor and description of the underlying technology.
*   **Features**:
    *   **📡 Live Pulse**: Real-time metrics for LLM latency (Groq) and Vector DB status.
    *   **🛠️ Component Breakdown**: Detailed logic behind choosing **ChromaDB**, **LangChain**, and **HuggingFace**.
    *   **📊 Tech Comparison**: A tabular comparison of this stack vs. traditional alternatives.

### 🏗️ Tab 4: Architecture (Systems Design)
*   **Purpose**: For engineers to understand the data flow and orchestration.
*   **Features**:
    *   **📐 HLD/LLD Diagrams**: Visual maps of the multi-phase pipeline (Ingestion → Retrieval → Reasoning).
    *   **🔄 Workflow Detail**: Step-by-step logic of how a query is transformed and reasoned upon.

### 📋 Tab 5: System Logs (Observability)
*   **Purpose**: Full transparency into the application's backend health.
*   **Features**:
    *   **📜 Live Event Stream**: Real-time logging of API calls, database queries, and error handling.
    *   **🎛️ Filter & Search**: Ability to filter logs by `INFO`, `SUCCESS`, `WARNING`, or `ERROR`.
    *   **📊 Log Metrics**: Statistical breakdown of system success rates and event counts.

---

## 🚀 LLMOps & Deployment Playbook

### 🏗️ CI/CD Pipeline
Integrated with **GitHub Actions** for automated:
- Code Quality Linting (`Pylint`, `Flake8`)
- Container Image Builds
- Registry Push (Artifact Registry / ECR)

### ☁️ Cloud Strategy

| Provider | Method | Command Snippet |
| :--- | :--- | :--- |
| **GCP** | GKE (Kubernetes) | `kubectl apply -f llmops-k8s.yaml` |
| **AWS** | EKS (Fargate) | `eksctl create cluster --name anime-rag` |
| **Cloud** | Streamlit Cloud | Auto-deploy from `main` branch |

---

## 🛠️ Production Deployment (GCP + K8s)

For professional infrastructure, we utilize **Google Cloud Platform (GCP)** with **Ubuntu 24.04 LTS** and **Minikube** for local Kubernetes orchestration.

### 1. VM Provisioning (GCP)
- **Machine Type**: `E2-Standard-4` (4 vCPU, 16 GB RAM)
- **Boot Disk**: 256 GB SSD (Ubuntu 24.04 LTS)
- **Networking**: Allow Port `8501` (Streamlit Default)

### 2. Kubernetes Orchestration
```bash
# Point Docker to Minikube context
eval $(minikube docker-env)

# Build & Deploy
docker build -t llmops-app:latest .
kubectl apply -f llmops-k8s.yaml

# Expose Service
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
```

---

## 📊 Enterprise Monitoring (Grafana)

We implement **Full-Stack Observability** using **Grafana Cloud** via Helm charts to monitor cluster health and application metrics.

### 🔍 Monitoring Steps:
1. **Namespace isolation**: `kubectl create ns monitoring`
2. **HELM Integration**:
   ```bash
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update
   helm upgrade --install grafana-k8s-monitoring grafana/k8s-monitoring \
     --namespace "monitoring" --values my-grafana-values.yaml
   ```
3. **Dashboarding**: Real-time visualization of Pod CPU, Memory spikes, and LLM API latency.

---

## 📊 Performance Benchmarks

| Metric | Target | Real-World Performance (Groq) |
| :--- | :--- | :--- |
| **Vector Search Latency** | < 20ms | ~12ms |
| **LLM Inference (TPS)** | > 200 | ~240 (LPU Optimized) |
| **UI Load Time** | < 2s | ~1.4s |
| **Scale Capability** | 10k Records | Tested at 14k+ entries |

---

## 🛠️ Developer Setup

### 📦 Prerequisites
- **Python 3.11+**
- **Git LFS** (Handles large `.bin` and `.sqlite3` files up to 2GB)
- **Groq API Key** (Get it at [Groq Console](https://console.groq.com/))

### 🚀 Quick Start
```bash
# Clone & Initialize LFS
git clone https://github.com/Ratnesh-181998/Agentic-RAG-Anime-Recommender-System.git
git lfs install
git lfs pull

# Environment Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run Local Server
streamlit run Code/app/premium_dashboard.py
```

### �️ Environment Variables
| Variable | Description | Source |
| :--- | :--- | :--- |
| `GROQ_API_KEY` | Core LLM Inference Key | [Groq Cloud](https://console.groq.com/keys) |

---

## 🛤️ Future Roadmap

- [ ] **Multimodal Search**: Search using images/frames from anime.
- [ ] **Streaming Responses**: Real-time token streaming in the UI.
- [ ] **Collaborative Filtering**: Integration of Hybrid-RAG (User-ratings + Semantic).
- [ ] **Grafana Integration**: Export logs to a dedicated monitoring dashboard.

---

## 📞 Contact & Networking

**Ratnesh Kumar Singh | Data Scientist (AI/ML Engineer)**
*4+ Years of Professional Experience in Building Production AI Systems*

- 💼 **LinkedIn**: [Connect with me](https://www.linkedin.com/in/ratneshkumar1998/)
- 🐙 **GitHub**: [Review my Repos](https://github.com/Ratnesh-181998)
- 🌐 **Live Project**: [Explore the App](https://agentic-rag-anime-recommender-system-dhsvh7zgrejeed2ghprr3d.streamlit.app/)

---

## 📜 License
Licensed under the **MIT License**. Feel free to fork and build upon this innovation.

---
*Built with passion for the AI Community. 🚀*
