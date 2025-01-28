from setuptools import setup, find_packages

setup(
    name='DEIM',
    version='0.1.0',
    packages=['.engine', '.engine.core'],
    install_requires=[
        # Add your project's dependencies here
        # 'some_package>=1.0.0',
        #torch>=2.0.1,
        #torchvision>=0.15.2,
        'faster-coco-eval>=1.6.5',
        'PyYAML',
        'tensorboard',
        'scipy',
        'calflops',
        'transformers'
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts here
            # 'deim=deim.cli:main',
        ],
    },
    author='Shihua Huang',
    author_email='www.shihuahuang.cn/',
    description='A brief description of your project',
    #long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='DEIM: DETR with Improved Matching for Fast Convergence',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)