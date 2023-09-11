import UserInterface as UI
import EaiRouterComplet as Eai


if __name__ == "__main__":
    SystemsID=UI.GoWindow()
    arbre_xml = Eai.configurer_fichier_xml(SystemsID)
    chemin_fichier_xml = "chemin_vers_le_fichier_genere.xml"
    arbre_xml.write(chemin_fichier_xml, encoding="UTF-8", xml_declaration=True)
    print(f"Fichier XML généré avec succès : {chemin_fichier_xml}")