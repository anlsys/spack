# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Nrm(Package):
    """Node Resource Manager. Contains documentation and examples."""

    homepage = "https://nrm.readthedocs.io/en/latest/"
    git = "https://github.com/anlsys/nrm-docs.git"
    version("main", branch="main")

    depends_on('py-nrm', type=('build', 'run'))
    depends_on('nrm-core', type=('build', 'run'))
