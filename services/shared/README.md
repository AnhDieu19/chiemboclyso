# Shared Library
# Common code used by all microservices in the tuvi-app platform

This package contains shared modules that multiple services depend on.
It should be installed as a local package in each service.

## Installation

```bash
# From any service directory
pip install -e ../shared
```

## Modules

| Module | Description |
|--------|-------------|
| `core/` | Core calculations: Cần Chi, Lunar conversion, Cục, Fortune periods, Ngũ Hành |
| `data/` | Lookup tables, constants, star position tables |
| `stars/` | 11 star placement algorithms |
| `chart/` | Birth chart builder (`generate_birth_chart`) |
| `interpretation/` | Chinh Tinh meanings, palace meanings, patterns |

## Usage in services

```python
from shared.core.lunar_converter import solar_to_lunar
from shared.chart.chart_builder import generate_birth_chart
from shared.data.can_chi import THIEN_CAN, DIA_CHI
from shared.stars.chinh_tinh_placer import place_chinh_tinh
```
