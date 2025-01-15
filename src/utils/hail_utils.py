import os
import tempfile
from urllib.parse import urlparse, urlunparse
import hail as hl

def get_local_tmpdir():
    """Create and return a proper temporary directory path for Hail"""
    tmp_path = tempfile.gettempdir()
    if os.name == 'nt':  # Windows
        tmp_url = f'file:///{tmp_path.replace(os.sep, "/")}'
    else:  # Unix-like systems
        tmp_url = f'file://{tmp_path}'
    r = urlparse(tmp_url)
    if not r.scheme:
        r = r._replace(scheme='file')
    return urlunparse(r)

def initialize_hail(reference="GRCh38"):
    """Initialize Hail if not already initialized"""
    try:
        # Check if Hail is already initialized
        if hl.eval(hl.literal(1)) == 1:
            print("Hail is already initialized")
            return
    except Exception:
        # If Hail is not initialized or there's an error, initialize it
        local_tmpdir = get_local_tmpdir()
        print(f"Initializing Hail with temporary directory: {local_tmpdir}")
        
        hl.init(
            default_reference=reference,
            local_tmpdir=local_tmpdir
        )
        print("Hail initialized successfully")
