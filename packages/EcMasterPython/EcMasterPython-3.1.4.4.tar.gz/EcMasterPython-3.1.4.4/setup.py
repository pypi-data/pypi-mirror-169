import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EcMasterPython",
    version="3.1.4.04",
    author="acontis technologies GmbH",
    author_email="ecsupport@acontis.com",
    description="The Python Wrapper provides a Python interface to use acontis EtherCAT Master (EC-Master), acontis EtherCAT Simulator (EC-Simulator) and RAS Client/Server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.acontis.com/",
    project_urls={
        "Programming Interface": "https://public.acontis.com/manuals/EC-Master/3.1/html/ec-master-python/index.html",
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Cython",
        "Programming Language :: C",
        "Programming Language :: C++",
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
    ],
    keywords="Acontis EtherCAT Master Simulator Library",
    packages=setuptools.find_packages(),    
    python_requires=">=3.7",
    include_package_data=True,
    license="proprietary and confidential",
    package_data= {
        "EcMasterPython": [
          "Examples/EcMasterDemoPython/*.*",
          "Sources/EcWrapperPython/*.*",
        ],
    },
)