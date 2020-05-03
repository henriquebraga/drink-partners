from drink_partners.contrib.utils.points_distance import (
    get_coordinate_distance_points
)


class TestCalculatePointsDistance:

    def test_should_get_coordinate_distance_points(self):
        point_a = [4, 0]
        point_b = [6, 6]

        assert get_coordinate_distance_points(
            a=point_a,
            b=point_b
        ) == 6.324555320336759
