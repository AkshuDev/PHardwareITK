"""Base Class for GPU drivers"""

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
        raise NotImplementedError

    def viewport(self, w: int=800, h: int=600):
        """Changes/Makes the viewport"""
        raise NotImplementedError

    def create_shader(self, shader_type: str, source: str):
        """Creates a shader"""
        raise NotImplementedError

    def create_program(self, vertex_shader: Any, fragment_shader: Any):
        """Creates a program based on the shader's provided"""
        raise NotImplementedError

    def use_program(self, program: Any):
        """Uses a creates program"""
        raise NotImplementedError

    def create_buffer(self):
        """Creates a GPU Buffer"""
        raise NotImplementedError

    def bind_array_buffer(self, buf: Any):
        """Binds a Array buffer to the GPU"""
        raise NotImplementedError
    
    def buffer_data(self, data: Any, usage: Any):
        """Creats and initializes the buffer's data"""
        raise NotImplementedError

    def create_texture(self):
        """Creates a texture"""
        raise NotImplementedError

    def bind_texture(self, texture: Any, target: Any):
        """Binds the created texture to the GPU"""
        raise NotImplementedError

    def tex_image_2d(self, width: int, height: int, data: Any, target: Any, internal_format: Any, format_: Any, type_: Any):
        """Texture Image 2D"""
        raise NotImplementedError

    def create_framebuffer(self):
        """Creates a framebuffer"""
        raise NotImplementedError

    def bind_framebuffer(self, fbo: Any, target: Any):
        """Binds the created framebuffer to the GPU"""
        raise NotImplementedError
    
    def set_uniform_mat4(self, program: Any, name: str, mat: Any):
        """Set the value of a mat4 variable in a shader"""
        raise NotImplementedError
    
    def check_error(self):
        """Checks for error"""
        raise NotImplementedError