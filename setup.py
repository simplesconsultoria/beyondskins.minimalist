from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='beyondskins.minimalist',
      version=version,
      description="Beyondskins Minimalist",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone, Diazo, Theme, Simples Consultoria,',
      author='Andre Nogueira',
      author_email='andre@simplesconsultoria.com.br',
      url='https://github.com/simplesconsultoria/beyondskins.minimalist',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['beyondskins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
