from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import exists, join
import sh

class LibLZMARecipe(Recipe):
    name = 'liblzma'
    version = '5.2.2'
    url = 'http://tukaani.org/xz/xz-{version}.tar.gz'
    depends = ['python2']
    patches = ['bswap-local.diff']

    def should_build(self, arch):
        super(LibLZMARecipe, self).should_build(arch)
        return True

    def build_arch(self, arch):
        super(LibLZMARecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.Command('./configure'), '--host=' + arch.toolchain_prefix,
                               '--target=' + arch.toolchain_prefix,
                               '--prefix=' + self.ctx.get_python_install_dir(),
                               '--enable-shared', _env=env)
            shprint(sh.make, '-j5', 'all', _env=env)
            shutil.copyfile(join(self.get_build_dir(arch.arch), 'src', 'liblzma', '.libs', 'liblzma.so'),
                        join(self.ctx.get_libs_dir(arch.arch), 'liblzma.so'))


    def get_recipe_env(self, arch):
        env = super(LibLZMARecipe, self).get_recipe_env(arch)
        env['CFLAGS'] += ' -Os'
        return env

recipe = LibLZMARecipe()
