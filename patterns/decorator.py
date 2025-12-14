# =============================
# Decorator Pattern for Message Styling
# =============================
from datetime import datetime

class MessageDecorator:
    """Base decorator class"""
    def __init__(self, message):
        self._message = message
    
    def get_text(self):
        return self._message.get_text()

class TimestampDecorator(MessageDecorator):
    """Adds timestamp to message"""
    def get_text(self):
        ts = datetime.now().strftime("[%H:%M] ")
        return ts + self._message.get_text()

class BoldDecorator(MessageDecorator):
    """Makes message bold (using Discord-style formatting)"""
    def get_text(self):
        return f"**{self._message.get_text()}**"

class ColorDecorator(MessageDecorator):
    """Adds color formatting"""
    def __init__(self, message, color_code):
        super().__init__(message)
        self.color_code = color_code
    
    def get_text(self):
        # Discord-style color formatting
        return f"```ansi\n\u001b[{self.color_code}m{self._message.get_text()}\u001b[0m\n```"

class ItalicDecorator(MessageDecorator):
    """Makes message italic"""
    def get_text(self):
        return f"*{self._message.get_text()}*"

class StyledMessageFactory:
    """Helper class to create decorated messages easily"""
    @staticmethod
    def create_styled_message(base_message, styles=[]):
        """
        Create a decorated message with specified styles
        styles: list of decorator names like ['timestamp', 'bold']
        """
        message = base_message
        
        for style in styles:
            if style == "timestamp":
                message = TimestampDecorator(message)
            elif style == "bold":
                message = BoldDecorator(message)
            elif style == "italic":
                message = ItalicDecorator(message)
            elif style.startswith("color"):
                # color:31 for red, color:32 for green, etc.
                color_code = style.split(":")[1] if ":" in style else "31"
                message = ColorDecorator(message, color_code)
        
        return message