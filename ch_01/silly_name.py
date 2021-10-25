from random import choice

ADJ = ["Warty", "Hoary", "Breezy", "Dapper", "Edgy", "Feisty", "Gutsy",
       "Hardy", "Intrepid", "Jaunty", "Karmic", "Lucid", "Maverick", "Natty",
       "Oneiric", "Precise", "Quantal", "Raring", "Saucy", "Trusty", "Utopic",
       "Vivid", "Wily", "Xenial", "Yakkety", "Zesty", "Artful", "Bionic",
       "Cosmic", "Disco", "Eoan", "Focal", "Groovy"]

NOUN = ["Warthog", "Hedgehog", "Badger", "Drake", "Eft", "Fawn", "Gibbon",
        "Heron", "Ibex", "Jackalope", "Koala", "Lynx", "Meerkat", "Narwhal",
        "Ocelot", "Pangolin", "Quetzal", "Ringtail", "Salamander", "Tahr",
        "Unicorn", "Vervet", "Werewolf", "Xerus", "Yak", "Zapus", "Aardvark",
        "Beaver", "Cuttlefish", "Dingo", "Ermine", "Fossa", "Gorilla",
        "Axolotl"]


def get_silly_name(adj, noun, second_adj=False):
    
    new_adj = " "  if not second_adj else f" and {choice(adj)} "
    return f"{choice(adj)}{new_adj}{choice(noun)}"


if __name__ == "__main__":
    print(get_silly_name(ADJ, NOUN))
    print(get_silly_name(ADJ, NOUN, True))