"""
Design Patterns Module for Chat Simulator
"""

from .builder import ChatSessionBuilder, ChatSession
from .decorator import (MessageDecorator, TimestampDecorator, 
                       BoldDecorator, ItalicDecorator, ColorDecorator,
                       StyledMessageFactory)

__all__ = [
    'ChatSessionBuilder',
    'ChatSession',
    'MessageDecorator',
    'TimestampDecorator',
    'BoldDecorator',
    'ItalicDecorator',
    'ColorDecorator',
    'StyledMessageFactory'
]