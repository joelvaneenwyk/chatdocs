"""Setup script for 'chatdocs' package."""

from setuptools import setup  # type: ignore[reportMissingModuleSource]  # pylint: disable=import-error

with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

PROJECT_NAME = "chatdocs"

setup(
    name=PROJECT_NAME,
    version="0.2.6",
    description="Chat with your documents offline using AI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ravindra Marella",
    author_email="mv.ravindra007@gmail.com",
    url=f"https://github.com/marella/{PROJECT_NAME}",
    license="MIT",
    packages=[PROJECT_NAME],
    package_data={PROJECT_NAME: ["data/chatdocs.yml", "data/index.html"]},
    entry_points={
        "console_scripts": [
            f"{PROJECT_NAME} = {PROJECT_NAME}.main:app",
        ],
    },
    install_requires=[
        "accelerate>=0.20.3",
        "chromadb>=0.3.0,<0.4.0",
        "ctransformers>=0.2.25,<0.3.0",
        "deepmerge>=1.1.0,<2.0.0",
        "InstructorEmbedding>=1.0.1,<2.0.0",
        "langchain>=0.0.181",
        "pydantic>=1.9,<2.0",
        "pyyaml>=6.0",
        "quart>=0.18.3,<0.19.0",
        "sentence-transformers>=2.2.2,<3.0.0",
        "tqdm>=4.64.1,<5.0.0",
        "transformers>=4.32.0",
        "typer>=0.9.0",
        "typing-extensions>=4.4.0,<5.0.0",
        # Document Loaders
        "extract-msg>=0.41.0,<0.42.0",
        "pandoc>=2.3,<3.0.0",
        "pypandoc>=1.11,<2.0.0",
        "pdfminer.six==20221105",
        "unstructured>=0.6.0,<0.7.0",
        # Temporary fix for `rich`, `numpy` version conflicts.
        "argilla==1.8.0",
    ],
    extras_require={
        "gptq": [
            "auto-gptq>=0.4.2,<0.5.0",
            "optimum>=1.12.0",
        ],
        "tests": [
            "pytest",
        ],
    },
    zip_safe=False,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=f"{PROJECT_NAME} ctransformers transformers langchain chroma ai llm",
)
