from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.lista_filiali = None
        self.dizionario_filiali = {}
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def get_filiali(self):
        if self.lista_filiali is None:
            self.lista_filiali = DAO.read_all_filiali()
        # Creo il dizionario
        for filiale in self.lista_filiali:
            self.dizionario_filiali[filiale.id] = filiale
        return self.lista_filiali

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        # TODO
        self.G.clear()
        nodi = self.get_filiali()
        for n in nodi:
            self.G.add_node(n)

        archi = DAO.read_all_edges()
        for arco in archi:
            num = arco["num_bonifici"]
            if num > 0:
                ##
            u = self.dizionario_filiali[arco.id_filiale_origine]
            v = self.dizionario_filiali[arco.id_filiale_destinazione]
            self.G.add_edge(u, v)

    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
