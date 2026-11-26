from database.dao import DAO
import networkx as nx

from model import filiale


class Model:
    def __init__(self):
        self.lista_filiali = None
        self.dizionario_filiali = {}
        self.lista_edges = None
        self.dizionario_edges = {}
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def get_filiali(self):
        if self.lista_filiali is None:
            dao = DAO()
            self.lista_filiali = dao.read_all_filiali()
        # Creo il dizionario
        for filiale in self.lista_filiali:
            self.dizionario_filiali[filiale.id] = filiale
        return self.lista_filiali

    def get_edges(self):
        if self.lista_edges is None:
            dao = DAO()
            self.lista_edges = dao.read_all_edges()
            for edge in self.lista_edges:
                chiave = (edge["f1"], edge["f2"])
                self.dizionario_edges[chiave] = edge
        return self.lista_edges

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        # TODO
        self.G.clear()
        filiali = self.get_filiali()
        for filiale in filiali:
            self.G.add_node(filiale)
        collegamenti = self.get_edges()
        for edge in collegamenti:
            if edge["num_bonifici"] > 0:
                media = edge["somma_importi"]/ edge["num_bonifici"]
                if media >= threshold:
                    u = self.dizionario_filiali.get(edge["f1"])
                    v = self.dizionario_filiali.get(edge["f2"])
                    if u is not None and v is not None and u != v:
                        self.G.add_edge(u, v, weight=media)
        return

    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return list(self.G.edges(data=True))
