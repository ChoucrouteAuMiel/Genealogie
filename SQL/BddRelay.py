from neo4j import GraphDatabase, basic_auth
from neo4j.work import result

class Relay:
    def __init__(self, uri, user, pwd) -> None:
        self.driver = GraphDatabase.driver(uri, auth=basic_auth(user, pwd))
    
    def close(self):
        self.driver.close()

    def execute(self, functionToExecute, **individual):
        with self.driver.session() as session:
            exeCmd = session.write_transaction(functionToExecute, individual)

    @staticmethod
    def createCouple(tx, refId, spouseId):
        result = tx.run("MATCH(Individu.refId)"
                        "WHERE(refId = Individu.individuId) "
                        "CREATE (c:couple{})"
                        )
