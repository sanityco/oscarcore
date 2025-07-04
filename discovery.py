class Discovery:
    """
    Node keşif ve kayıt mekanizması.
    """

    def __init__(self, node_id: str):
        self.node_id = node_id
        # Basit node listesi
        self.known_nodes = {node_id}

    def register_node(self, node_id: str):
        """
        Yeni bir node kaydet.
        """
        self.known_nodes.add(node_id)
        print(f"[Discovery] Node registered: {node_id}")

    def unregister_node(self, node_id: str):
        """
        Bir node'u kaldır.
        """
        if node_id in self.known_nodes:
            self.known_nodes.remove(node_id)
            print(f"[Discovery] Node unregistered: {node_id}")

    def list_nodes(self):
        """
        Bilinen node'ları döndür.
        """
        return list(self.known_nodes)

    def is_known(self, node_id: str) -> bool:
        """
        Node biliniyor mu?
        """
        return node_id in self.known_nodes
