import sys
import os
import time
import hashlib
import chromadb
import networkx as nx
import matplotlib.pyplot as plt

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(WORKSPACE_DIR, "chroma_db_storage")
GRAPH_PATH = os.path.join(WORKSPACE_DIR, "l3_knowledge_graph.gml")


# 纯本地哈希 embedding（完全离线，零网络依赖）
class LocalHashEmbedding:
    def __init__(self):
        pass
    
    def name(self):
        return "local_hash_embedding"
    
    def __call__(self, input):
        embeddings = []
        for text in input:
            # 使用 SHA256 哈希生成 384 维伪向量
            hash_bytes = hashlib.sha256(text.encode('utf-8')).digest()
            # 扩展到 384 维
            extended = (hash_bytes * 12)[:384]
            embedding = [float(b) / 255.0 for b in extended]
            embeddings.append(embedding)
        return embeddings


client = chromadb.PersistentClient(path=CHROMA_PATH)
vector_db = client.get_or_create_collection(
    name="agent_episodic_v2",
    embedding_function=LocalHashEmbedding()
)


def inject_l2_memory(content, tags="system"):
    doc_id = f"mem_{int(time.time())}"
    vector_db.add(documents=[content], metadatas=[{"tags": tags, "timestamp": time.time()}], ids=[doc_id])
    print(f"[L2] Memory saved! ID: {doc_id}")


def recall_l2_memory(query, top_k=2):
    results = vector_db.query(query_texts=[query], n_results=top_k)
    if not results['documents'][0]: return "No related memory."
    return "\n".join([f"- {doc}" for doc in results['documents'][0]])


def load_graph():
    if os.path.exists(GRAPH_PATH):
        return nx.read_gml(GRAPH_PATH)
    else:
        G = nx.DiGraph()
        nx.write_gml(G, GRAPH_PATH)
        return G


graph_db = load_graph()


def add_l3_relation(entity1, entity2, relation):
    graph_db.add_edge(entity1, entity2, relation=relation)
    nx.write_gml(graph_db, GRAPH_PATH)
    print(f"[L3] Relation added: {entity1} -[{relation}]-> {entity2}")


def visualize_graph():
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph_db, seed=42)
    if len(graph_db.nodes) == 0:
        plt.text(0.5, 0.5, "Knowledge Graph is Empty.\nUse 'learn' command to add nodes.", 
                 horizontalalignment='center', verticalalignment='center', fontsize=12)
    else:
        nx.draw(graph_db, pos, with_labels=True, node_color='lightblue', edge_color='gray', 
                node_size=2500, font_size=10, font_weight='bold')
        edge_labels = nx.get_edge_attributes(graph_db, 'relation')
        nx.draw_networkx_edge_labels(graph_db, pos, edge_labels=edge_labels, font_size=8)
    
    img_path = os.path.join(WORKSPACE_DIR, "agent_brain_map.png")
    plt.title("Agent L3 Knowledge Graph")
    plt.savefig(img_path)
    print(f"[L3] Brain map generated: {img_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    command = sys.argv[1]
    
    if command == "learn":
        text, e1, e2, rel = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        inject_l2_memory(text)
        add_l3_relation(e1, e2, rel)
    elif command == "think":
        query, target_node = sys.argv[2], sys.argv[3]
        print("[L2] Episodic memory recall:\n" + recall_l2_memory(query))
        if graph_db.has_node(target_node):
            for u, v, data in graph_db.edges(target_node, data=True):
                print(f"- [L3] Graph rule: {u} must [{data['relation']}] to {v}")
    elif command == "map":
        visualize_graph()
```

复制走推上去吧 🚀
