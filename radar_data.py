#!/usr/bin/python

import yaml


t = """\
Compatibility:
    segment: a
    Infrastructure: [Docker, Apptainer, SingularityCE, CMAKE]
    Prototype: []
    Analysis: [resqui]
FAIRness:
    segment: b
    Infrastructure: [ zenodo, Hermes Workflows, howfairis, F-UJI, DVC, SOMEF, cffinit, CC-License Chooser, Somesy, CodeMeta Generator]
    Prototype: [ REUSE, Fair Python CookieCutter]
    Analysis: [ resqui, SQAaas, eOSSR, Fair-Aware tool, Five Recommendations for FAIR Software ]
Flexibility:
    segment: c
    Infrastructure: [ SingularityCE, Nix, Docker, Apptainer]
    Prototype: [ pypi ]
    Analysis: [ resqui ]
Functional Suitability:
    segment: d
    Infrastructure: [ ]
    Prototype: [ ]
    Analysis: [ resqui ]
Interaction Capability:
    segment: e
    Infrastructure: [ tox, Jupyter ]
    Prototype: [ mkDocs ]
    Analysis: [ resqui ]
Maintainability:
    segment: f
    Infrastructure: [ sphinx,cmake,Hermes Workflows, Kubernetes,Jupyter, Jenkins, GNU Guix, tox,Travis CI,javadoc,Junit, SonarQube, Git, SCANOSS,Dependabot]
    Prototype: [ poetry, black, pypi, CppUnit]
    Analysis: [ resqui, Checkstyle, Hadolint, valgrind, pre-commit, gcov, ruff, Qlty,doxygen,pytest, flake8, pylint ]
Performance Efficiency:
    segment: g
    Infrastructure: [ ]
    Prototype: [ ]
    Analysis: [ resqui, valgrind, score-p ]
Reliability:
    segment: h
    Infrastructure: [ JUnit, tox, Docker, GNU Guix, Gitlab CICD, Jenkins, SonarQube, Kubernetes, Apptainer, Travis CI, Nix]
    Prototype: [ CppUnit, Github Actions]
    Analysis: [ resqui, valgrind, pytest ]
Safety:
    segment: i
    Infrastructure: [ ]
    Prototype: [ ]
    Analysis: [ resqui ]
Security:
    segment: j
    Infrastructure: [ SonarQube, SCANOSS, Nix, Dependabot]
    Prototype: [ ]
    Analysis: [ resqui, bandit, Gitleaks, Hadolint,bearer ]
Sustainability:
    segment: k
    Infrastructure: [ GNU Guix,Docker,zenodo,javadoc,Gitlab CICD, DVC,Apptainer,tox,Software Heritage,Kubertnetes,Hermes Workflows ]
    Prototype: [ Zenodo github Integration, Github Actions,poetry]
    Analysis: [ resqui,Github Copilot,Choose a License,pre-commit,Gitleaks,gcov,valgrind ]
"""

x = yaml.load(t,yaml.Loader)
import pprint
pprint.pprint(x)
for key,definition in x.items():
    # print(key, definition["segment"])
    # pprint.pprint(definition)
    for i, v in enumerate(["Analysis", "Prototype", "Infrastructure"]):
        for w in definition[v]:
            print( "  { "+ f'id:"{definition["segment"]}{i+1}", label:"{w}"'+" },") 



