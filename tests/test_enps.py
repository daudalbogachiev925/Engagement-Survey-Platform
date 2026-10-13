from src.enps import compute_enps

def test_enps_all_promoters():
    assert compute_enps([10, 10, 9]) == 100.0

def test_enps_all_detractors():
    assert compute_enps([0, 1, 2]) == -100.0

def test_enps_neutral():
    assert compute_enps([7, 8, 7]) == 0.0
