from dataclasses import dataclass, field
from typing import List

@dataclass
class Question:
    id: str
    text: str
    category: str  # engagement, manager, growth, compensation, culture
    scale: int = 5

DEFAULT_QUESTIONS = [
    Question("q1", "Я рекомендую компанию как место работы", "engagement"),
    Question("q2", "Мой руководитель поддерживает моё развитие", "manager"),
    Question("q3", "У меня есть возможности для роста", "growth"),
    Question("q4", "Моя компенсация справедлива", "compensation"),
    Question("q5", "Я чувствую себя частью команды", "culture"),
    Question("q6", "Я знаю, как мой вклад влияет на цели компании", "engagement"),
    Question("q7", "Я могу балансировать работу и личную жизнь", "culture"),
    Question("q8", "Обратная связь даётся регулярно", "manager"),
]
