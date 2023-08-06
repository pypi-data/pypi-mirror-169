from array import array
from asyncio.log import logger
from runfalconbuildtools.file_utils import add_execution_permission_to_file, delete_file, create_file, file_exists, get_runfalcon_tmp_file
from runfalconbuildtools.logger import Logger
import subprocess
import tempfile

class CommandLineExecutor:

    logger:Logger = Logger('CommandLineExecutor')

    return_code:int = 0
    stdout:str = None
    stderr:str = None

    def execute(self, command:str, command_args:array = None, shell:bool = False):
        
        cmd = [command]
        if command_args != None:
            cmd = cmd + command_args

        result = None
        try:
            result = subprocess.check_output(cmd, shell=shell)
            self.return_code = 0
            self.stdout = result
            self.stderr = None
        except Exception as e:
            self.logger.error('Invoking process', e)
            self.return_code = -1
            self.stdout = result
            self.stderr = '{err}\n'.format( err = str(e))

    def get_tmp_script_file_name() -> str:
        tempfile.TemporaryFile

    def execute_script(self, script:str, delete:bool = True):
        tmp_file = get_runfalcon_tmp_file('sh')
        create_file(tmp_file, script)
        add_execution_permission_to_file(tmp_file)
        self.execute(tmp_file, shell=True)
        if self.return_code != 0:
            raise Exception('Error {code} ocurred when executing\nOut:\n{out}\nError:\n{error}\nscript:\n{script}' \
                .format(code = self.return_code, out = self.stdout, error = self.stderr, script = script))

        if delete:
            delete_file(tmp_file)
