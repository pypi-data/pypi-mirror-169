import setuptools

setuptools.setup(
    name='bgp_visualize',
    version='0.3.1',
    # package_dir={'': 'bgp_visualize'},
    packages=["bgp_visualize"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/TheNetworker/visualize_bgp_asns',
    license='MIT License',
    install_requires=[
        'networkx>=2.8.6',
        'matplotlib>=3.5.0, < 3.6.0',
        'requests>=2.28.1',
        'beautifulsoup4>=4.11.1',
    ],
    python_requires='>=3.9',
    author='Bassem Aly',
    author_email='basim.alyy@gmail.com',
    keywords=['bgp', 'network', 'autonomous system', 'visualize',
              'automation', 'networking', 'devops', 'netdevops'
              'routing'],
    description='The package is used to visualize BGP Autonomous Systems and draw the interconnections between them. Also, it colors the operators ASN in each country and the upstreams and downstreams services providers.'
)
