from match_text.match_company_names import get_company_names


def test_match_company_names():
    text1 = "La Société TotoT Titi est responsable avec la SA Turl-ututu Et Consors de ce carnage."
    assert get_company_names(text1) == [(3, 21, "ORGANIZATION_1"), (46, 70, "ORGANIZATION_1")]
    text2 = "Vu l'absence de l'Association pour l'Insertion et l'Accompagnement en Limousin (ASIIAL) assignée ;"
    assert get_company_names(text2) == [(18, 87, "ORGANIZATION_1")]
    text3 = "Condamner solidairement les Sociétés OCM et OCS aux entiers dépens."
    assert get_company_names(text3) == [(28, 47, "ORGANIZATION_1")]
    text4 = "La SARL ENZO & ROSSO n'est pas facile à extraire."
    assert get_company_names(text4) == [(3, 20, "ORGANIZATION_1")]
    text5 = "la Caisse Nationale des Caisses d'Epargne était "
    assert get_company_names(text5) == [(3, 41, "ORGANIZATION_1")]
    text6 = "le Syndicat des Copropriétaires de la Résidence Le Jardin de la Galère, ce qui"
    assert get_company_names(text6) == [(3, 70, "ORGANIZATION_1")]
    text7 = "SA CAISSE D'EPARGNE ET DE PREVOYANCE PROVENCE ALPES C ORSE LA CAISSE D'EPARGNE ET, " \
            "Banque coopérative"
    assert get_company_names(text7) == [(0, 81, "ORGANIZATION_1")]
    text8 = "représentée et assistée par Me Grégory PILLIAR de l'AARPI ESCLAPEZ SINELLE PILLIARD pour"
    assert get_company_names(text8) == [(52, 83, 'ORGANIZATION_1')]
    text9 = "représentée par Me Joseph MAGNAN de la SCP MAGNAN PAUL MAGNAN JOSEPH, avocat"
    assert get_company_names(text9) == [(39, 68, 'ORGANIZATION_1')]
