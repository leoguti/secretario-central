#!/usr/bin/env python3
"""
Sistema RAG (Retrieval Augmented Generation) para análisis de correos
Usa ChromaDB + Ollama embeddings + llama3.2:3b
"""

import requests
import json
import chromadb
from chromadb.config import Settings

# Configuración Ollama
OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2:3b"

# Configuración ChromaDB
CHROMA_PATH = "./chroma_db"

def get_ollama_embedding(text: str) -> list[float]:
    """Genera embedding usando Ollama"""
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text}
    )
    return response.json()["embedding"]

def query_ollama(prompt: str, context: str = "") -> str:
    """Consulta a llama3.2:3b con contexto opcional"""
    full_prompt = f"{context}\n\n{prompt}" if context else prompt
    
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": LLM_MODEL,
            "prompt": full_prompt,
            "stream": False
        }
    )
    return response.json()["response"]

def setup_chroma_client():
    """Inicializa cliente ChromaDB"""
    client = chromadb.Client(Settings(
        persist_directory=CHROMA_PATH,
        anonymized_telemetry=False
    ))
    return client

def load_policies_to_chroma(client, policies_path: str):
    """Carga políticas de trabajo a ChromaDB"""
    # Crear o obtener colección
    collection = client.get_or_create_collection(
        name="politicas_trabajo",
        metadata={"description": "Políticas y procedimientos de Trufi"}
    )
    
    # Leer archivo de políticas
    with open(policies_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Dividir en chunks (por secciones)
    sections = content.split('\n## ')
    
    documents = []
    metadatas = []
    ids = []
    
    for idx, section in enumerate(sections):
        if not section.strip():
            continue
            
        # Extraer título de sección
        lines = section.split('\n')
        title = lines[0].replace('#', '').strip()
        
        documents.append(section)
        metadatas.append({"section": title, "source": "POLITICAS_TRABAJO.md"})
        ids.append(f"policy_{idx}")
    
    # Agregar documentos a ChromaDB
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    
    print(f"✅ Cargadas {len(documents)} secciones de políticas")
    return collection

def query_rag(collection, query: str, n_results: int = 3):
    """Consulta RAG: busca contexto relevante y genera respuesta"""
    print(f"\n🔍 Consulta: {query}")
    
    # 1. Buscar contexto relevante en ChromaDB
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    
    # 2. Construir contexto
    context_parts = []
    print("\n📚 Contexto relevante encontrado:")
    for i, doc in enumerate(results['documents'][0]):
        section = results['metadatas'][0][i]['section']
        print(f"  {i+1}. {section}")
        context_parts.append(f"[{section}]\n{doc[:500]}...")  # Primeros 500 chars
    
    context = "\n\n".join(context_parts)
    
    # 3. Generar respuesta con llama3.2
    prompt = f"""Eres un asistente que analiza correos según las políticas de Trufi Association.

Contexto relevante de las políticas:
{context}

Pregunta: {query}

Responde de forma breve y precisa."""
    
    print("\n💭 Generando respuesta con llama3.2:3b...")
    response = query_ollama(prompt)
    
    return response, results

def test_email_analysis(collection):
    """Prueba con ejemplos de correos"""
    
    test_cases = [
        {
            "from": "jose.landin@giz.de",
            "subject": "Reunión Proyecto México - Rutómetro",
            "body": "Hola Leonardo, necesitamos revisar los avances del Rutómetro en Toluca."
        },
        {
            "from": "leramirez@urbanito.com.pe",
            "subject": "Propuesta GTFS Lima",
            "body": "Hola, estamos interesados en avanzar con la propuesta de GTFS para MOVILIZATE."
        },
        {
            "from": "promotions@godaddy.com",
            "subject": "Renovación dominio EXPEREST.COM",
            "body": "Tu dominio EXPEREST.COM está por vencer. Renueva ahora con 20% descuento."
        }
    ]
    
    for email in test_cases:
        print("\n" + "="*70)
        query = f"""Analiza este correo y dime:
1. ¿Es importante?
2. ¿Qué prioridad tiene? (ALTA/MEDIA/BAJA)
3. ¿Qué acción se debe tomar?

From: {email['from']}
Subject: {email['subject']}
Body: {email['body']}"""
        
        response, _ = query_rag(collection, query, n_results=2)
        print(f"\n✨ Respuesta:\n{response}")

def main():
    """Función principal"""
    print("🚀 Iniciando sistema RAG...")
    
    # 1. Configurar ChromaDB
    client = setup_chroma_client()
    
    # 2. Cargar políticas
    policies_file = "POLITICAS_TRABAJO.md"
    collection = load_policies_to_chroma(client, policies_file)
    
    # 3. Pruebas
    print("\n" + "="*70)
    print("📧 ANÁLISIS DE CORREOS DE PRUEBA")
    print("="*70)
    
    test_email_analysis(collection)
    
    print("\n\n✅ Prueba completada!")

if __name__ == "__main__":
    main()
