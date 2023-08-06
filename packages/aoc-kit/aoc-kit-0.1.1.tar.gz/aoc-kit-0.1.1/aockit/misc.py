from typing import Any, Dict, List, Tuple

direction_2D_hor_vert = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_2D_hor_vert_diag = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 1),
    (1, 1),
    (1, -1),
    (-1, -1),
]


def neighbor_2D_iter(
    the_map: dict[tuple[int, int], Any],
    at: tuple[int, int],
    directions: List[Tuple[int, int]],
):
    for x_off, y_off in directions:
        x = at[0] + x_off
        y = at[1] + y_off
        yield x, y, the_map.get((x, y), None)


def neighbor_2D_hor_vert_iter(the_map: Dict[Tuple[int, int], Any], at: Tuple[int, int]):
    yield from neighbor_2D_iter(the_map, at, direction_2D_hor_vert)


def neighbor_2D_hor_vert_diag_iter(
    the_map: Dict[Tuple[int, int], Any], at: Tuple[int, int]
):
    yield from neighbor_2D_iter(the_map, at, direction_2D_hor_vert_diag)


def get_min_max(the_map: Dict[Tuple[int, int], Any]):
    min_x = min([x for x, _ in the_map])
    min_y = min([y for _, y in the_map])
    max_x = max([x for x, _ in the_map])
    max_y = max([y for _, y in the_map])

    return min_x, max_x, min_y, max_y


def map_iterator(the_map: Dict[Tuple[int, int], Any], extend=0):
    min_x, max_x, min_y, max_y = get_min_max(the_map)
    for y in range(min_y - extend, max_y + 1 + extend):
        for x in range(min_x - extend, max_x + 1 + extend):
            yield x, y


def map_row_iterator(the_map: Dict[Tuple[int, int], Any], extend=0):
    min_x, max_x, min_y, max_y = get_min_max(the_map)
    for y in range(min_y - extend, max_y + 1 + extend):
        yield [(x, y) for x in range(min_x - extend, max_x + 1 + extend)]


def print_map(the_map: Dict[Tuple[int, int], Any]):
    for row in map_row_iterator(the_map):
        out = ""
        for x, y in row:
            if the_map.get((x, y)):
                out += "#"
            else:
                out += " "
        print(out)
