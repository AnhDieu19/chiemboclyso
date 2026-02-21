"""
Pytest Test Suite for Tu Vi Application
Comprehensive automated testing for CI/CD integration
"""
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chart import generate_birth_chart, generate_birth_chart_lunar
from interpretation import generate_overall_interpretation
from core import get_fortune_periods


class TestChartGeneration:
    """Test chart generation functionality"""
    
    def test_basic_chart_generation(self):
        """Test basic chart generation with valid inputs"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        assert chart is not None
        assert len(chart['positions']) == 12
        assert len(chart['all_stars']) >= 80
        assert 'menh_name' in chart
        assert 'than_name' in chart
        assert 'cuc' in chart
    
    @pytest.mark.parametrize("hour", list(range(12)))
    def test_all_12_hours(self, hour):
        """Test chart generation for all 12 birth hours"""
        chart = generate_birth_chart(15, 6, 1990, hour, 'nam')
        assert len(chart['positions']) == 12
    
    @pytest.mark.parametrize("gender", ['nam', 'nu'])
    def test_both_genders(self, gender):
        """Test chart generation for both genders"""
        chart = generate_birth_chart(15, 6, 1990, 6, gender)
        assert len(chart['positions']) == 12
        assert chart['gender'] == gender
    
    def test_male_female_same_menh(self):
        """Male and female with same birth data should have same menh"""
        chart_male = generate_birth_chart(15, 6, 1990, 6, 'nam')
        chart_female = generate_birth_chart(15, 6, 1990, 6, 'nu')
        
        assert chart_male['menh_name'] == chart_female['menh_name']
        assert chart_male['cuc']['name'] == chart_female['cuc']['name']


class TestLunarInput:
    """Test lunar calendar input functionality"""
    
    def test_lunar_input_basic(self):
        """Test basic lunar date input"""
        chart = generate_birth_chart_lunar(15, 6, 1990, 6, 'nam', False)
        
        assert chart is not None
        assert len(chart['positions']) == 12
        assert 'lunar_date' in chart
    
    def test_lunar_input_leap_month(self):
        """Test lunar date with leap month"""
        chart = generate_birth_chart_lunar(15, 4, 1990, 6, 'nam', True)
        
        assert chart is not None
        assert chart['lunar_date']['leap'] == True


class TestTuHoa:
    """Test Tu Hoa (4 transformations) functionality"""
    
    def test_tu_hoa_exists(self):
        """Test that all 4 Hoa are present"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        tu_hoa = chart['tu_hoa']
        required = ['Hóa Lộc', 'Hóa Quyền', 'Hóa Khoa', 'Hóa Kỵ']
        
        for hoa in required:
            assert hoa in tu_hoa, f"{hoa} should be in tu_hoa"
    
    def test_tu_hoa_has_star(self):
        """Test that each Hoa has an associated star"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        for hoa_name, hoa_info in chart['tu_hoa'].items():
            assert 'star' in hoa_info
            assert hoa_info['star'] is not None


class TestStarPlacement:
    """Test star placement functionality"""
    
    def test_all_chinh_tinh_present(self):
        """Test that all 14 Chinh Tinh are placed"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        chinh_tinh = ['Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 'Thiên Đồng', 'Liêm Trinh',
                      'Thiên Phủ', 'Thái Âm', 'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương', 
                      'Thất Sát', 'Phá Quân']
        
        for star in chinh_tinh:
            assert star in chart['all_stars'], f"{star} should be in all_stars"
    
    def test_all_luc_cat_present(self):
        """Test that all 6 Luc Cat are placed"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        luc_cat = ['Tả Phụ', 'Hữu Bật', 'Văn Xương', 'Văn Khúc', 'Thiên Khôi', 'Thiên Việt']
        
        for star in luc_cat:
            assert star in chart['all_stars'], f"{star} should be in all_stars"
    
    def test_all_luc_sat_present(self):
        """Test that all 6 Luc Sat are placed"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        luc_sat = ['Kinh Dương', 'Đà La', 'Hỏa Tinh', 'Linh Tinh', 'Địa Không', 'Địa Kiếp']
        
        for star in luc_sat:
            assert star in chart['all_stars'], f"{star} should be in all_stars"
    
    def test_star_positions_valid(self):
        """Test that all star positions are valid (0-11)"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        for star, position in chart['all_stars'].items():
            assert 0 <= position <= 11, f"{star} has invalid position {position}"


class TestFortunePeriods:
    """Test fortune period calculations"""
    
    def test_fortune_periods_exist(self):
        """Test that fortune periods are calculated"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        periods = get_fortune_periods(chart, 2024)
        
        assert 'dai_han_all' in periods
        assert 'tieu_han' in periods
        assert 'luu_nien' in periods
    
    def test_age_calculation(self):
        """Test age calculation in fortune periods"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        periods = get_fortune_periods(chart, 2024)
        
        # Born 1994, checking 2024 = 31 tuổi mụ (Vietnamese age)
        assert periods['age'] == 31
    
    @pytest.mark.parametrize("year", [2020, 2024, 2030, 2050])
    def test_multiple_years(self, year):
        """Test fortune periods for multiple years"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        periods = get_fortune_periods(chart, year)
        
        assert periods['age'] > 0
        assert len(periods['dai_han_all']) > 0


class TestInterpretation:
    """Test interpretation module"""
    
    def test_interpretation_exists(self):
        """Test that interpretation is generated"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        interp = generate_overall_interpretation(chart)
        
        assert interp is not None
    
    def test_patterns_detected(self):
        """Test that patterns are detected"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        interp = generate_overall_interpretation(chart)
        
        assert 'patterns' in interp
        assert isinstance(interp['patterns'], list)
    
    def test_patterns_summary_exists(self):
        """Test that patterns summary is generated"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        interp = generate_overall_interpretation(chart)
        
        assert 'patterns_summary' in interp


class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_early_year(self):
        """Test early year (1920)"""
        chart = generate_birth_chart(1, 1, 1920, 0, 'nam')
        assert len(chart['positions']) == 12
    
    def test_leap_year_feb_29(self):
        """Test leap year February 29"""
        chart = generate_birth_chart(29, 2, 2000, 6, 'nam')
        assert len(chart['positions']) == 12
    
    def test_end_of_year(self):
        """Test end of year date"""
        chart = generate_birth_chart(31, 12, 1990, 11, 'nu')
        assert len(chart['positions']) == 12
    
    def test_first_day_of_year(self):
        """Test first day of year"""
        chart = generate_birth_chart(1, 1, 2000, 0, 'nam')
        assert len(chart['positions']) == 12


class TestDataIntegrity:
    """Test data integrity across calculations"""
    
    def test_12_positions_always(self):
        """Test that there are always exactly 12 positions"""
        for year in [1960, 1980, 2000, 2020]:
            chart = generate_birth_chart(15, 6, year, 6, 'nam')
            assert len(chart['positions']) == 12
    
    def test_menh_than_valid(self):
        """Test that menh and than positions are valid"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        assert 0 <= chart['menh_position'] <= 11
        assert 0 <= chart['than_position'] <= 11
    
    def test_cuc_valid(self):
        """Test that cuc is valid"""
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        valid_cuc_numbers = [2, 3, 4, 5, 6]  # Thuy, Moc, Kim, Tho, Hoa
        assert chart['cuc']['number'] in valid_cuc_numbers


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])

