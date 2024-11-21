from setuptools import setup, find_packages

setup(
    name='whisper_transcriber',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai-whisper>=20240124',
        'torch>=2.2.0',
        'numpy>=1.24.0',
        'soundfile>=0.12.1',
        'ffmpeg-python>=0.2.0'
    ],
    extras_require={
        'dev': ['pytest>=8.0.0']
    },
    entry_points={
        'console_scripts': [
            'whisper-transcribe=whisper_transcriber.transcriber:main',
        ],
    },
    python_requires='>=3.11',
)
