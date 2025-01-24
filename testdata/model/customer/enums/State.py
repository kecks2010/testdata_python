from enum import Enum

class State(Enum):
    DE_BB = ("Brandenburg", "DE-BB", "BB")
    DE_BE = ("Berlin", "DE-BE", "BE")
    DE_BW = ("Baden-Württemberg", "DE-BW", "BW")
    DE_BY = ("Bayern", "DE-BY", "BY")
    DE_HB = ("Bremen", "DE-HB", "HB")
    DE_HE = ("Hessen", "DE-HE", "HE")
    DE_HH = ("Hamburg", "DE-HH", "HH")
    DE_MV = ("Mecklenburg-Vorpommern", "DE-MV", "MV")
    DE_NI = ("Niedersachsen", "DE-NI", "NI")
    DE_NW = ("Nordrhein-Westfalen", "DE-NW", "NW")
    DE_RP = ("Rheinland-Pfalz", "DE-RP", "RP")
    DE_SH = ("Schleswig-Holstein", "DE-SH", "SH")
    DE_SL = ("Saarland", "DE-SL", "SL")
    DE_SN = ("Sachsen", "DE-SN", "SN")
    DE_ST = ("Sachsen-Anhalt", "DE-ST", "ST")
    DE_TH = ("Thüringen", "DE-TH", "TH")

    def __init__(self, state_name, international_abbreviation, local_abbreviation):
        self.state_name = state_name
        self.international_abbreviation = international_abbreviation
        self.local_abbreviation = local_abbreviation

    @classmethod
    def get_state_by_name(cls, state_name):
        for state in cls:
            if state.state_name == state_name:
                return state
        return None
