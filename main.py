from ethiopia.search_ethiopia import EthiopiaSearch

# Full state space graph for Ethiopia travel (figure 1)
ETHIOPIA_GRAPH = {

    "Addis Ababa": ["Adama", "Debre Birhan", "Ambo", "Fiche"],


    "Adama": ["Batu", "Assela", "Addis Ababa"],
    "Batu": ["Shashemene", "Adama"],
    "Shashemene": ["Hawassa", "Batu", "Wolaita Sodo"],
    "Hawassa": ["Shashemene", "Dilla"],
    "Dilla": ["Hawassa", "Bule Hora"],
    "Bule Hora": ["Dilla", "Yabelo"],
    "Yabelo": ["Bule Hora", "Moyale"],
    "Moyale": ["Yabelo"],


    "Debre Birhan": ["Kemise", "Debre Sina", "Addis Ababa"],
    "Kemise": ["Debre Birhan", "Dessie"],
    "Dessie": ["Kemise", "Woldia"],
    "Woldia": ["Dessie", "Lalibela", "Alamata"],
    "Lalibela": ["Woldia", "Sekota"],
    "Sekota": ["Lalibela", "Adigrat"],
    "Adigrat": ["Axum", "Mekele", "Sekota"],
    "Axum": ["Adigrat", "Shire"],
    "Shire": ["Axum", "Humera"],
    "Mekele": ["Adigrat", "Alamata"],
    "Alamata": ["Mekele", "Woldia"],


    "Ambo": ["Nekemte", "Addis Ababa"],
    "Nekemte": ["Gimbi", "Ambo"],
    "Gimbi": ["Nekemte", "Assosa"],
    "Assosa": ["Gimbi"],

    "Assela": ["Dodola", "Adama"],
    "Dodola": ["Bale", "Assela"],
    "Bale": ["Dodola", "Goba"],
    "Goba": ["Bale", "Sof Oumer"],
    "Sof Oumer": ["Goba"],
    "Wolaita Sodo": ["Shashemene", "Arba Minch"],
    "Arba Minch": ["Wolaita Sodo", "Konso"],
    "Konso": ["Arba Minch", "Yabelo"],


    "Fiche": ["Debre Libanos", "Addis Ababa"],
    "Debre Libanos": ["Fiche"],
    "Debre Sina": ["Debre Birhan"]
}


def main():
    search_system = EthiopiaSearch(ETHIOPIA_GRAPH)

    start_city = "Lalibela"
    target_city = "Debre Sina"

    bfs_route = search_system.bfs(start_city, target_city)
    dfs_route = search_system.dfs(start_city, target_city)

    print(f"BFS Path ({start_city} -> {target_city}):")
    print(" -> ".join(bfs_route) if bfs_route else "No path found")

    print(f"\nDFS Path ({start_city} -> {target_city}):")
    print(" -> ".join(dfs_route) if dfs_route else "No path found")


if __name__ == "__main__":
    main()
