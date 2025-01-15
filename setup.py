from setuptools import setup, find_packages

setup(
    name="genome-analysis",
    version="0.1.0",
    description="Machine learning pipeline for genomic variant analysis",
    author="Jerry McDonald",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9,<3.10",
    install_requires=[
        # Core dependencies with specific versions to avoid conflicts
        "hail",
        "pandas>=2.2.0",
        "numpy>=1.26.0",
        "protobuf",  # Explicitly specify protobuf version
        "scipy>=1.11.0",
        "tensorflow==2.11.0",  # Using an older version that's compatible with protobuf
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
        "viz": [
            "bokeh>=3.3.0",
            "plotly>=5.24.0",
        ],
        "cloud": [
            "azure-storage-blob>=12.24.0",
            "boto3>=1.35.0",
        ]
    }
)