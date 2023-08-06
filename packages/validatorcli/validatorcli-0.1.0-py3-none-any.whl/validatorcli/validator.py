#!/usr/bin/env python
"""
    Call the validator API on a target.  See README for usage details.
"""
import argparse
from contextlib import contextmanager
from io import StringIO
import json
import logging
import os
from queue import Queue
import sys
import threading
import time


import diskcache
from termcolor import colored
from tabulate import tabulate
import timeout_decorator
from tqdm import tqdm


from validatorsdk.validator import Validate
# from validatorsdk import sdk_version
from validatorcli import __version__ as cli_version


LOG = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    stream=sys.stdout
)
LOG_STREAM = StringIO()
LOG_HANDLER = logging.StreamHandler(LOG_STREAM)
LOG.addHandler(LOG_HANDLER)


FILE_QUEUE= Queue()
JOB_QUEUE = Queue()
NUM_THREADS = int(os.getenv('THREADS', '2'))
RESULTS = {}
JOBS_LIST = []
REPORT_CARD = [
    ["File", "Evaluation", "Result"]
]
URL = os.getenv(
    'VALIDATOR_URL',
    'internal-GT-EN-LoadB-11OUT8RUBCZR8-1253716517.us-east-1.elb.amazonaws.com'
)
STATUS_MAP = {
    'success': colored('Pass', 'green'),
    'failed': colored('Failed', 'red'),
    'warning': colored('Warning', 'yellow'),
}
CACHE = diskcache.Cache('~/.validator')


def find_files(paths) -> list:
    """
        I return a list of files to validate.

        Args:
            path: path that we want to recursively search

        Returns:
            a list of files for validation
    """
    file_list = []
    for path in paths:
        orig = os.getcwd()
        if os.path.isdir(path):
            path = os.path.abspath(path)
            os.chdir(path)
        else:
            file_list += [path]
        for root, _, files in os.walk(path):
            if root.endswith('.git'):
                continue
            for filename in files:
                _, ext = os.path.splitext(filename)
                if ext in ['.json', '.yaml', '.yml', '.py', 'tf']:
                    fqfn = os.path.join(root, filename)
                    file_list += [fqfn]
        os.chdir(orig)
    return file_list


def is_warning(evaluation, name):
    """Determine if the evaluation issued any warnings.  The validator doesn't
    interpret warnings as failures, so it marks those evaluations as
    successful.  However, it would still be beneficial to show those as
    warnings.  This logic interprets the results to see if a warning was
    issued, and returns True, otherwise, False.

    Args:
        evaluation: name of the evaluation (pylint, cfn-lint, etc)
        name: name of the file that was validated

    Returns:
        bool: whether or not the evaluation issued a warning
    """
    result = RESULTS[name][evaluation]
    LOG.debug(json.dumps(result))
    if evaluation == 'cfn-nag':
        # cfn_nag doesn't set exit code to a non-zero value for warnings
        return '| WARN W' in result['output']
    if evaluation in ['pylint']:
        return False
        # these set exit code to a non-zero value for warnings
        # return result['state'] == 'success'

    return False


def print_header(evaluation, name) -> None:
    """
        I print a header to clearly show the boundry between evaluations.

        Args:
            evaluation: the evaluation which is being presented.
    """
    output = RESULTS[name][evaluation]['output']
    state = RESULTS[name][evaluation]['state']
    status = STATUS_MAP[state]

    # Remove Path
    pwd = os.getenv('PWD', '')
    if pwd:
        name = name.replace(f'{pwd}/', '')

    # Save Report Card
    REPORT_CARD.append([name, evaluation, status])

    # print output
    LOG.info(
        tabulate(
            [[evaluation, name, status]],
            tablefmt="grid"
        )
    )
    LOG.info('\n%s\n\n', output)


def print_results(args):
    """
        I print the results.

        Args:
            args: the cli args.
        Returns:
            boolean: true if all success false if problems were found.
    """
    state = True
    for name, record in RESULTS.items():
        # first pass, check for warnings
        for evaluation in record['evaluations']:
            if is_warning(evaluation, name):
                RESULTS[name][evaluation]['state'] = 'warning'

        if args.output == 'text':
            for evaluation in record['evaluations']:
                print_header(evaluation, name)

        # warnings are still considered success
        if record['state'] not in ['success', 'warning']:
            state = False

    # Print Report Card
    if args.output == 'text':
        LOG.info(colored('Report Card', 'blue'))
        LOG.info(tabulate(REPORT_CARD, tablefmt="grid"))

    # If somebody wants json lets give it.
    if args.output == 'json':
        LOG.info(json.dumps(RESULTS, indent=2))

    # write file if requeted to
    if args.save != '':
        with open(args.save, 'a', encoding='utf8') as file_hander:
            file_hander.writelines(LOG_STREAM.getvalue())

    if not state:
        return 1
    return 0


def get_version() -> str:
    """
        I return the context of what version is running.

        Returns:
            String representing the version running.
    """
    try:
        # return f'CLI: {cli_version} SDK: {sdk_version}'
        return f'CLI: {cli_version}'
    except:  # pylint: disable=bare-except
        return 'unknown'


def parse_args():
    """
        Parse command line args.

        Args:
            None
        Returns:
            argparse.Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='*')
    parser.add_argument(
        '--version',
        help='show version info and exit',
        action='version',
        version=get_version()
    )
    parser.add_argument(
        '--debug',
        help='turn on debug',
        required=False,
        action='store_true',
    )
    parser.add_argument('--purge',
        required=False,
        dest='purge',
        action='store_true',
        default=False,
        help="Purge Cache?"
    )
    parser.add_argument(
        '--noreport',
        help='skip the report',
        required=False,
        action='store_true',
    )
    parser.add_argument(
        '--output',
        help='toggle from text to json output',
        required=False,
        choices=['text', 'json'],
        default='text'
    )
    parser.add_argument(
        '-t', '--num-threads',
        help='number of threads',
        type=int,
        default=NUM_THREADS
    )
    parser.add_argument(
        '-s', '--save',
        help='save output to a file.',
        default='',
        required=False
    )
    parser.add_argument(
        '--jobs',
        help='Write a jobs file for async processing.',
        default='',
        required=False
    )
    parser.add_argument(
        '-l', '--load',
        help='Load the jobs from a processing file.',
        default='',
        required=False
    )
    parser.add_argument(
        '-j', '--job',
        help='Get a previous job_id.',
        default='',
        required=False
    )
    return parser.parse_args()


def queue_files(file_list) -> None:
    """
        Add files that were found to a queue.

        Args:
            file_list: list of files
    """
    LOG.debug('Queueing %d files', len(file_list))
    desc = 'Finding files'.rjust(15, ' ')
    for fqfn in tqdm(file_list, desc=desc, ascii=False):
        LOG.debug('File: %s', fqfn)
        FILE_QUEUE.put(fqfn)


def create_job() -> None:
    """
        This function is ran by one of many threads to read filenames from the
        file queue to create validation jobs.  The validation jobs are added into
        another queue so we can get the results in another worker.

        Args:
            None
    """
    while True:
        if FILE_QUEUE.empty():
            break
        fqfn = FILE_QUEUE.get()
        LOG.debug('Sending %s', fqfn)
        obj = Validate(filename=fqfn)
        obj.validate()
        JOBS_LIST.append(obj.job_id)
        JOB_QUEUE.put(obj)
        FILE_QUEUE.task_done()


def receive_job() -> None:
    """
        This function is ran by one of many threads to read validation jobs from
        the job queue.  Results are added to the RESULTS dict so they can be
        displayed in the report card.

        Args:
            None
    """
    while True:
        if JOB_QUEUE.empty():
            break
        obj = JOB_QUEUE.get()
        LOG.debug('Receiving %s', obj.name)
        RESULTS[obj.name] = obj.results()
        JOB_QUEUE.task_done()


def monitor(file_list, desc=None) -> None:
    """
        Monitor a queue's progress using a progress bar.  We monitor the change
        in the queue size and increment the progress bar based on that change.
        If it doesn't change during an iteration, the change amount is zero,
        meaning it doesn't change.

        Args:
            queue: queue.Queue object
            desc: description for the progress bar
    """
    desc = desc.rjust(15, ' ')
    progress = tqdm(file_list, desc=desc, ascii=False)
    last = 0
    while len(RESULTS) < len(file_list):
        time.sleep(0.1)
        change = len(RESULTS) - last
        progress.update(change)
        last = len(RESULTS)
    progress.close()


@contextmanager
def watch(queue, desc):
    """
        A context manager that will start another thread to watch over a queue.

        Args:
            queue: queue.Queue object
            desc: description for the progress bar

        Yields:
            thread
    """
    try:
        thread = threading.Thread(target=monitor, args=[queue, desc])
        thread.start()
        yield thread
    finally:
        thread.join()


@timeout_decorator.timeout(90)
def main() -> bool:
    """
        The main event!

        Args:
            None
        Returns:
            boolean: true if all success false if problems were found.
    """
    args = parse_args()

    # optional debug
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.purge:
        CACHE.clear()

    LOG.debug('Running in debug')
    LOG.debug('Running %d threads', args.num_threads)

    # fetch one previous job
    if args.job:
        obj = Validate(job_id=args.job)
        data = obj.results()
        RESULTS[data['fqfn']] = data

    # load the async jobs if need be
    elif args.load:
        with open(args.load, 'r', encoding='utf8') as file_hander:
            jobs_list = json.load(file_hander)
        for job_id in jobs_list:
            obj = Validate(job_id=job_id)
            data = obj.results()
            RESULTS[data['fqfn']] = data

    else:
        if not args.path:
            LOG.info('Nothing to validate')
            return 0
        # Create validation tasks for every job
        file_list = find_files(args.path)
        queue_files(file_list)

        # Create the jobs
        for _ in range(args.num_threads):
            threading.Thread(target=create_job).start()
        FILE_QUEUE.join()

        # write our jobs if asked to
        if args.jobs:
            with open(args.jobs, 'w', encoding='utf8') as file_handler:
                file_handler.write(json.dumps(JOBS_LIST))

        # Get job results
        with watch(file_list, 'Getting results'):
            for _ in range(args.num_threads):
                threading.Thread(target=receive_job).start()
            JOB_QUEUE.join()

    if args.noreport:
        return 0

    LOG.info('Generating report card')
    CACHE.close()
    return print_results(args)


if __name__ == '__main__':
    sys.exit(main())
