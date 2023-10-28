from core.views import CityGrid, TowerGraph


def run_app():
    city = CityGrid(10, 10)
    city.print_grid()
    tower_range = 2
    towers = city.optimize_tower_placement(tower_range)
    print(f"\nОптимальное размещение башен: {towers}\n")
    city.place_tower(2, 2, tower_range)
    city.place_tower(7, 7, tower_range)

    tower_graph = TowerGraph(city, tower_range)
    start_tower = (0, 0)
    end_tower = (9, 9)

    reliable_path = tower_graph.find_reliable_path(start_tower, end_tower)
    if reliable_path:
        print(f"Путь с наименьшим числом переходов: {reliable_path}\n")
    else:
        print("Оптимального пути не найдено.")

    # Визуализация городской сетки, башен, зон покрытия и пути передачи данных
    city.visualize_city(
        tower_positions=[start_tower, end_tower], data_path=reliable_path
    )


if __name__ == "__main__":
    try:
        run_app()
    except Exception as error:
        print(f"Something went wrong {error}")
