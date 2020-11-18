from typing import List


class Hund:
    """ Hund stellt einen Gast für das Hundehotel dar
    """

    def __init__(self, name: str, alter: int, allergie_liste: List[str]):
        """ initialisiert ein Hundeobjekt

        Parameters
        ----------
        name: str
            Name von Hund
        alter: int
            Alter von Hund
        allergie_liste: list of list[str]
            Liste mit Allergenen
        """
        self.name = name  #: str: hundename
        self.alter = alter  #: int: alter des hundes
        self.allergie_liste = allergie_liste  #: list of str: Nahrungsmittel auf die Hund allergisch regiert

    def __str__(self):
        """liefert String repräsentation eines Hundeobjektes

        Returns
        -------
            String darstellung des Hundes
        """
        return f'Hund(Name:{self.name} Alter:{self.alter} Allergien:{self.allergie_liste})'

    def ist_allergisch(self, allergen: str) -> bool:
        """ überprüft ob hund allergisch auf etwas

        Die Funktion gleicht den eingegebenen Parameter allergen mit den vorhandenen Werten
        in allergie_liste ab. True wenn in liste, false wenn nicht.

        Parameters
        ----------
        allergen: str
            zu überprüfendes allergen
        Returns
        -------
            true falls hund allergisch drauf; false wenn nicht
        """
        return allergen in self.allergie_liste


# schneller Testcode, den ich nur zum rumprobieren verwende
if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 10, ['semmel', 'extrawurst'])
    print(rex)
    print(rex.ist_allergisch("semmel"))
    print(rex.ist_allergisch("brot"))

    # pass
