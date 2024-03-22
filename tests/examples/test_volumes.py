import pytest
from volumes import get_cube_volume, get_cylinder_volume, get_sphere_volume, get_tank_volume

def test_cylinder_volume():
    # Test with positive radius and height
    assert get_cylinder_volume(3, 5) == 141.37
    
    # Test with zero radius and positive height
    assert get_cylinder_volume(0, 5) == 0.0
    
    # Test with positive radius and zero height
    assert get_cylinder_volume(3, 0) == 0.0
    
    # Test with negative radius and positive height (assuming your function handles negative values gracefully)
    assert get_cylinder_volume(-2, 4) == 50.27
    
    # Test with large values
    assert get_cylinder_volume(100, 200) == 6283185.31
    
    
pytest.main()