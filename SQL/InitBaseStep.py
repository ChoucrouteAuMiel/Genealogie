class Bdd:
    def __init__(self, relay) -> None:
        self.relay = relay

    def initConstraint(self):
        self.relay.execute()

    @staticmethod
    def initDBConstraints(tx):
        tx.run("CREATE CONSTRAINT ON (city:City) ASSERT city.name IS UNIQUE "
                "CREATE CONSTRAINT ON (individu:Individu) ASSERT individu.id IS UNIQUE ")
        