import argparse


def job(args):
    pass


def jobs(args):

    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers()

    jobs_parser = sub_parsers.add_parser('jobs')
    jobs_parser.set_defaults(func=jobs)

    job_parser = sub_parsers.add_parser('job')
    job_parser.add_argument('--metrics', help='The path to the json file containing the metrics to display on the metrics tab')
    job_parser.add_argument('--charts', nargs='*', help='A list of file paths to the charts to dispay on the charts tab')
    job_parser.set_defaults(func=job)

    args = parser.parse_args()
    args.func(args)
