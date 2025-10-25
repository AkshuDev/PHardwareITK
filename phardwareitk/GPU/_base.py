from typing import Any

class BaseGPUD:
    """Abstract GPU backend interface"""

    def init(self, display: Any, window: Any, create_and_attach_ctx: bool=False):
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

    def create_context(self, display: Any, window: Any):
        """Returns the Created context in form of PIonContext"""
        raise NotImplementedError
    
    def destroy_context(self):
        """Destroys the created context"""