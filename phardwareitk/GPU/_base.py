from typing import Any

class BaseGPUD:
    """Abstract GPU backend interface"""

    def init(self, display: Any, window: Any):
        """Initialize GPU context for the specified window"""
        raise NotImplementedError
    
    def clear(self, r: int, g: int, b: int, a: int):
        """Clear screen to a color."""
        raise NotImplementedError

    def swap(self):
        """Swap framebuffers / present frame."""
        raise NotImplementedError

    def shutdown(self):
        """Release context and resources."""
        raise NotImplementedError

    def load_function(self, name: str):
        """Get a raw pointer to a GPU function (e.g. glDrawArrays)."""
        raise NotImplementedError