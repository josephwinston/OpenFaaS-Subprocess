import logging
import subprocess

def runCommand(aCommand,
               verbose=False):
    """
    Run a command. The command needs to be a list of the form ['ls', '-1'] 
    """

    if verbose:
        print('Planning to run', aCommand)

    try:
        completed = subprocess.run(aCommand,
                                   check=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

    except subprocess.CalledProcessError as err:
        if verbose:
            sys.stderr.write(('ERROR: %s\n') % (err))
            if err.stderr is not None:
                sys.stderr.write(('%s\n') % (err.stderr.decode('utf-8')))

        logging.warning(('ERROR: %s\n') % (err))
        if err.stderr is not None:
            logging.warning(('%s\n') % (err.stderr.decode('utf-8')))

    else:
        if verbose:
            print('returncode:', completed.returncode)

        if len(completed.stdout) > 0:
            print('Have {} bytes in stdout:\n{}'.format(len(completed.stdout),
                                                        completed.stdout.decode('utf-8')))

            logging.info('Have {} bytes in stdout:\n{}'.format(len(completed.stdout),
                                                               completed.stdout.decode('utf-8')))

        if len(completed.stderr) > 0:
            print('Have {} bytes in stderr:\n{}'.format(len(completed.stderr),
                                                        completed.stderr.decode('utf-8')))

            logging.info('Have {} bytes in stdout:\n{}'.format(len(completed.stdout),
                                                               completed.stdout.decode('utf-8')))

    return

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    subprocess.run(['ls', '-l', '/'], check=True)

    runCommand(['ls', '-1', '/'], True)
    
    return req
