"""Local ComfyUI package initializer.

This file ensures the local `comfy` directory is treated as a package so
Python will import the repository code instead of a similarly named
installed package from site-packages.
"""

# Expose package version if present
try:
    from . import __version__  # type: ignore
except Exception:
    pass

__all__ = []
