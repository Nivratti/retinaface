from setuptools import setup, find_packages

# pip install wheel           # 빌드 툴
# pip install setuptools     # 패키징 툴
# pip install twine            # 패키지 업로드 툴

packages = list(open('requirements.txt').readlines())
setup(
    name='retinaface_tf2',
    version='0.0.6',
    author='HEESEUNG KIM',
    author_email='boyanenivratti@gmail.com',
    description='face detector',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/Nivratti/retinaface_tf2',
    download_url='https://github.com/Nivratti/retinaface_tf2.git/archive/master.zip',
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    package_data={'':['*']},
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
