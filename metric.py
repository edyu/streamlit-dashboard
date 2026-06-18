from dataclasses import dataclass
from typing import Callable

@dataclass
class Metric:
    title: str
    func: Callable
    type: str
