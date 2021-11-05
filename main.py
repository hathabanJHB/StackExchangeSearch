from subprocess import Popen,PIPE


def get_error(cmd):
    args = cmd.split()
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out,err = proc.communicate()
    if err:
        return err.decode('utf-8').strip().split('\n')[-1]

    return "NO ERROR FOUND"