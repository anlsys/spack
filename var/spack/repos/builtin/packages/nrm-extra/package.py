# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class NrmExtra(Package):
    """Node Resource Manager. Contains external sensors and actuator for NRM."""

    homepage = "https://nrm.readthedocs.io/en/latest/"
    git = "https://github.com/anlsys/nrm-extra.git"
    version("master", branch="master")

    depends_on('libnrm@0.7.0', type=('build', 'run'))
