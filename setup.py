from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='openai-cheat-sheet',
    version='0.1',
    packages=['evals_registry.completion_fns'],
    license='MIT',
    description='Detailed notebooks to showcase the following capabilities of OpenAI',
    long_description=open('README.md').read(),
    install_requires=requirements,
    python_requires='>=3.12.1'
)
