import time
import subprocess


def before_all(_):
    process(
        'exec',
        '-T',
        'test-service',
        '/workspace/start_service',
    )

    time.sleep(20)


def after_all(_):
    check_call('exec', '-T', 'test-service', '/workspace/stop_service')


def process(
        *args,
        env=None,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
):
    return __subprocess(
        method=subprocess.Popen,
        stdout=stdout,
        stderr=stderr,
        args=args,
        env=env,
    )


def check_call(
        *args,
        env=None,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
):
    return __subprocess(
        method=subprocess.check_call,
        stdout=stdout,
        stderr=stderr,
        args=args,
        env=env,
    )


def __subprocess(method, args=None, **kwargs):
    return method(
        [
            'docker',
            'compose',
            f'--project-name=behave-feature-test',
            '--file=docker-compose.yml',
            *(args or []),
        ],
        **kwargs,
    )
