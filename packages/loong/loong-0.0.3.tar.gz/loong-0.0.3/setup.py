# import setuptools



# setuptools.setup(
#     name="example_package_dabocai",
#     version="0.0.1",
#     author="Example Author dabocai",
#     author_email="author@example.com",

#     description="A small example package",
#     long_description="long_description=",
#     long_description_content_type="text/markdown",
#     url="https://github.com/pypa/sampleproject",
#     packages=['dabocai'],

#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3.0',
# )


from time import time
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="loong",
    version="0.0.3",
    author="dabocai",
    author_email="longzh@qq.com",
    description="A test package",
    long_description=long_description,
    long_description_content_type="text/markdown",

 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
        package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
)