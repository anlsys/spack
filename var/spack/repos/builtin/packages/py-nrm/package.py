# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNrm(PythonPackage):
    """Python interface to the Argo Node Resource Manager,
    an infrastructure to allow applications to manage node resources
    on the fly."""

    homepage = "https://nrm.readthedocs.io"

    maintainers = ['perarnau']

    version('0.7',
            url='https://github.com/anlsys/nrm-python/archive/refs/heads/master.zip')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('nrm-core@0.7.0')
    depends_on('py-pyzmq', type=('build', 'run'))
    depends_on('py-tornado', type=('build', 'run'))
    depends_on('py-jsonschema', type=('build', 'run'))

    def setup_run_environment(self, env):
        env.prepend_path('LD_LIBRARY_PATH', self.spec['nrm-core'].prefix.lib)
