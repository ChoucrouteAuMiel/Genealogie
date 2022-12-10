class IndividualCreator:
    def __init__(self, bddRelay) -> None:
        self.relay = bddRelay

    def addIndividual(self, individual):
        self.relay.execute(individual, self.createIndividual)

    @staticmethod
    def createIndividual(tx, individual):
        result = tx.run("CREATE (individual:Individual) "
                        "SET individual.id = $id "
                        "SET individual.name = $name "
                        "SET individual.firstName = $firstname "
                        "SET individual.lastName = $lastname "
                        "SET individual.birthDate = $birthdate "
                        "SET individual.birthPlace = $birthplace "
                        "SET individual.deathDate = $deathdate "
                        "SET individual.deathPlace = $deathplace "
                        "SET individual.sex = $sex "
                        "SET individual.job = $job ",
                        id = individual.id,
                        name = individual.lastName + " - " + individual.firstName,
                        firstname = individual.firstName,
                        lastname = individual.lastName,
                        birthdate = individual.birthDate,
                        birthplace = individual.birthPlace,
                        deathdate = individual.deathDate,
                        deathplace = individual.deathPlace,
                        sex = individual.sex,
                        job = individual.job)
