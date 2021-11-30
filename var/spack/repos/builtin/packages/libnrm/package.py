# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libnrm(AutotoolsPackage):
    """Libnrm, the application instrumentation library for the Node
    Resource Manager(NRM)."""

    homepage = "https://nrm.readthedocs.io/en/latest/"
    url = "https://github.com/anlsys/libnrm/archive/refs/tags/v0.7.0.tar.gz"
    version('0.7.0', sha256='48be63ef90271050d27f03bf3006a71b49e668d2e2a80abd4c2ed02b49ac4204')

    tags = ['e4s']

    depends_on('m4', type='build')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('pkgconfig', type='build')

    depends_on('libzmq')
    depends_on('mpich')
