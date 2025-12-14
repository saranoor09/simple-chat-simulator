# =============================
# Builder Pattern
# =============================
from datetime import datetime

class ChatSession:
    def __init__(self):
        self.user = "Guest"
        self.theme = "default"
        self.enable_timestamps = True
        self.enable_notifications = True
        self.created_at = datetime.now()
    
    def __str__(self):
        return f"ChatSession(user={self.user}, theme={self.theme}, timestamps={self.enable_timestamps})"

class ChatSessionBuilder:
    def __init__(self):
        self.session = ChatSession()
    
    def set_user(self, username):
        """Set the username for the chat session"""
        self.session.user = username
        return self  # Return self for method chaining
    
    def set_theme(self, theme_name):
        """Set the theme (dark, light, pink, etc.)"""
        self.session.theme = theme_name
        return self
    
    def enable_timestamps(self, enable=True):
        """Enable or disable timestamps"""
        self.session.enable_timestamps = enable
        return self
    
    def enable_notifications(self, enable=True):
        """Enable or disable notifications"""
        self.session.enable_notifications = enable
        return self
    
    def build(self):
        """Return the final ChatSession object"""
        return self.session