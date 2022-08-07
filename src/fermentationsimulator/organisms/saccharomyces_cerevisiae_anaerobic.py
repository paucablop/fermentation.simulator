from dataclasses import dataclass
from kineticmodels.uptake_models import Monod


class SaccharomycesCerevisiaeAnaerobic:
    """
    Saccharomyces cerevisiae anaerobic model.
    """

    def __init__(self, parameters: dict):

        #: Name of the organism
        self.name: str = "Saccharomyces cerevisiae"

        #: Compounds in the model
        self.compounds: dict = {}

        #: Parameters in the model
        self.parameters: dict = parameters

        #: List of all reactions in the model
        self.glucose_uptake: Monod = Monod(self.parameters["glucose_uptake"])


