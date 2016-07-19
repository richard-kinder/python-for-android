from pythonforandroid.toolchain import CompiledComponentsPythonRecipe, shprint, shutil, current_directory, info
from os.path import exists, join
import sh

class BackportsDotLZMARecipe(CompiledComponentsPythonRecipe):
    name = 'backports.lzma'
    version = '0.0.6'
    url = 'https://pypi.io/packages/source/b/backports.lzma/backports.lzma-{version}.tar.gz'
    depends = ['python2', 'liblzma']
    site_packages_name = 'backports.lzma'


    def prebuild_arch(self, arch):
        info('XXX here is prebuild_arch pre')
        super(BackportsDotLZMARecipe, self).prebuild_arch(arch)
        info('XXX here is prebuild_arch')

    def get_recipe_env(self, arch):
        env = super(BackportsDotLZMARecipe, self).get_recipe_env(arch)
        info("Recipe arch doing here")
        r = self.get_recipe('liblzma', self.ctx)
        liblzma_dir = "%s/src/liblzma/api/" % r.get_build_dir(arch.arch)
        liblzma_static_dir = "%s/src/liblzma/.libs/" % r.get_build_dir(arch.arch)
        info("liblzma build dir is %s " % liblzma_dir)
        env['CFLAGS'] += ' -I' + liblzma_dir
        env['LDFLAGS'] += ' -L' + liblzma_static_dir
        return env

recipe = BackportsDotLZMARecipe()
