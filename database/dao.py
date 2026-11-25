from database.DB_connect import DBConnect
from model.filiale import Filiale


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    def read_all_filiali(self):
        conn = DBConnect.get_connection()
        if conn is None:
            return []
        try:
            cursore = conn.cursor(dictionary=True)
            try:
                query = "select * from filiale"
                cursore.execute(query)
                result = []
                for row in cursore:
                    filiale = Filiale(**row)
                    result.append(filiale)
                return result
            finally:
                cursore.close()
        finally:
            conn.close()

    def read_all_edges(self):
        conn = DBConnect.get_connection()
        if conn is None:
            return []
        try:
            cursore = conn.cursor(dictionary=True)
            try:
                query = ("""select
                            LEAST(id_filiale_origine, id_filiale_destinazione) as f1, 
                            GREATEST(id_filiale_origine, id_filiale_destinazione) as f2,
                            SUM(importo) as somma_importi,
                            COUNT(*) as num_bonifici
                            from bonifico
                            where id_filiale_origine <> id_filiale_destinazione 
                            group by LEAST(id_filiale_origine, id_filiale_destinazione), 
                            GREATEST(id_filiale_origine, id_filiale_destinazione)""")
                cursore.execute(query)
                result = []
                for row in cursore:
                    result.append(row)
                return result
            finally:
                cursore.close()
        finally:
            conn.close()