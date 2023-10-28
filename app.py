from core.views import CityGrid, TowerGraph


def run_app():
    city = CityGrid(10, 10)
    city.print_grid()
    tower_range = 2
    towers = city.optimize_tower_placement(tower_range)
    print(f"\nOptimal tower placement: {towers}\n")
    city.place_tower(2, 2, tower_range)
    city.place_tower(7, 7, tower_range)

    tower_graph = TowerGraph(city, tower_range)
    start_tower = (0, 0)
    end_tower = (9, 9)

    reliable_path = None
    max_attempts = 3  # Maximum number of path search attempts

    for attempt in range(max_attempts):
        reliable_path = tower_graph.find_reliable_path(start_tower, end_tower)
        if reliable_path:
            break

    if reliable_path:
        print(f"Path with the fewest transitions: {reliable_path}\n")
    else:
        print("No optimal path found after several attempts.")
    # Visualize the city grid, towers, coverage areas, and data transmission path
    city.visualize_city(
        tower_positions=[start_tower, end_tower], data_path=reliable_path
    )


if __name__ == "__main__":
    try:
        run_app()
    except Exception as error:
        print(f"Something went wrong {error}")
