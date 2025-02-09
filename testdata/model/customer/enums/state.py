from enum import Enum

class State(Enum):
    """
        Definition of states.

        Author:
            Mirko Werner
        """
    DE_BB = ("Brandenburg", "Brandenburg", "DE-BB", "BB")
    DE_BE = ("Berlin", "Berlin", "DE-BE", "BE")
    DE_BW = ("Baden-Württemberg", "Baden-Württemberg", "DE-BW", "BW")
    DE_BY = ("Bavaria", "Bayern", "DE-BY", "BY")
    DE_HB = ("Bremen", "Bremen", "DE-HB", "HB")
    DE_HE = ("Hesse", "Hessen", "DE-HE", "HE")
    DE_HH = ("Hamburg", "Hamburg", "DE-HH", "HH")
    DE_MV = ("Mecklenburg-Vorpommern", "Mecklenburg-Vorpommern", "DE-MV", "MV")
    DE_NI = ("Lower Saxony", "Niedersachsen", "DE-NI", "NI")
    DE_NW = ("North Rhine-Westphalia", "Nordrhein-Westfalen", "DE-NW", "NW")
    DE_RP = ("Rhineland-Palatinate", "Rheinland-Pfalz", "DE-RP", "RP")
    DE_SH = ("Schleswig-Holstein", "Schleswig-Holstein", "DE-SH", "SH")
    DE_SL = ("Saarland", "Saarland", "DE-SL", "SL")
    DE_SN = ("Saxony", "Sachsen", "DE-SN", "SN")
    DE_ST = ("Saxony-Anhalt", "Sachsen-Anhalt", "DE-ST", "ST")
    DE_TH = ("Thuringia", "Thüringen", "DE-TH", "TH")

    def __init__(self, state_name:str, german:str, international_abbreviation:str, local_abbreviation:str):
        self.state_name = state_name
        self.german = german
        self.international_abbreviation = international_abbreviation
        self.local_abbreviation = local_abbreviation

    @classmethod
    def get_state_by_name(cls, state_name):
        for state in cls:
            if state.state_name == state_name:
                return state
        return None
