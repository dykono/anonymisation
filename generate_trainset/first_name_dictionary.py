import acora

from generate_trainset.match_acora import get_acora_object, get_matches
from generate_trainset.modify_strings import get_title_case
from resources.config_provider import get_config_default


def get_first_name_dict() -> set:
    """
    Build a dictionary of French first names
    :rtype: a set of names
    """
    config = get_config_default()

    file1 = config["first_name_dict_1"]
    file2 = config["first_name_dict_2"]

    firs_name = set()
    with open(file1) as f1:
        for line in f1.readlines():
            fields = line.split(";")
            # all names start with a Upcase letter and finishes with a space
            text = fields[3].strip() + " "
            if len(text) >= 5:
                firs_name.add(text)

    with open(file2, encoding="ISO-8859-1") as f2:
        for line in f2.readlines():
            fields = line.split(";")
            text = fields[0].strip() + " "
            if len(text) >= 5:
                firs_name.add(get_title_case(text))

    firs_name.remove("Elle ")
    firs_name.remove("France ")
    firs_name.remove("Mercedes ")
    return firs_name


def get_first_name_matcher():
    """
    Build a matcher of first name based on a French names dictionary
    :return: Acora matcher
    """
    first_name_dict = get_first_name_dict()
    return get_acora_object(list(first_name_dict),
                            ignore_case=False)


def get_first_name_matches(matcher: acora._cacora.UnicodeAcora, text: str) -> list:
    """
    Find match of first name in a text if the word enfant is present
    :param matcher: Dictionary based matcher
    :param text: original text
    :return: list of offsets
    """
    offsets = get_matches(matcher, text, "PARTIE_PP")
    # names include a space so we fix the point by removing 1 to the offset
    results = [(start, end - 1, type_name) for start, end, type_name in offsets]

    if "enfant" in text:
        return results
    else:
        return []
