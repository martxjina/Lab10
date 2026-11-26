import flet as ft
from flet import value

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        # TODO
        valore = (self._view.importo_medio_minimo.value or "").strip()
        try:
            soglia = float(valore)
        except ValueError:
            self._view.show_alert("Inserisci un importo numerico valido")
            return

        if soglia < 0:
            self._view.show_alert("La soglia non può essere negativa")
            return

        self._model.costruisci_grafo(soglia)

        # Recuperiamo i dati dal model
        num_filiali = self._model.get_num_nodes()
        num_collegamenti = self._model.get_num_edges()
        collegamenti = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di filiali: {num_filiali}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di collegamenti: {num_collegamenti}"))

        for i, (u, v, attr) in enumerate(collegamenti, start=1):
            peso = attr.get("weight",0)
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{i}) [{u} -> {v}] -- Importo medio per bonifico: € {peso:.2f}"))
        self._view.update()
