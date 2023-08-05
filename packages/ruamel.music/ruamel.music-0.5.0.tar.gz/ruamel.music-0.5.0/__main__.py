# coding: utf-8
# flake8: noqa
# cligen: 0.2.0, dd: 2022-09-25


import argparse
import importlib
import ruamel.std.pathlib
import sys
import typing

from . import __version__


class HelpFormatter(argparse.RawDescriptionHelpFormatter):
    def __init__(self, *args: typing.Any, **kw: typing.Any):
        kw['max_help_position'] = 40
        super().__init__(*args, **kw)

    def _fill_text(self, text: str, width: int, indent: str) -> str:
        import textwrap

        paragraphs = []
        for paragraph in text.splitlines():
            paragraphs.append(textwrap.fill(paragraph, width,
                             initial_indent=indent,
                             subsequent_indent=indent))
        return '\n'.join(paragraphs)


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args: typing.Any, **kw: typing.Any):
        kw['formatter_class'] = HelpFormatter
        super().__init__(*args, **kw)


class DefaultVal(str):
    def __init__(self, val: typing.Any):
        self.val = val

    def __str__(self) -> str:
        return str(self.val)


class CountAction(argparse.Action):
    """argparse action for counting up and down

    standard argparse action='count', only increments with +1, this action uses
    the value of self.const if provided, and +1 if not provided

    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action=CountAction, const=1,
            nargs=0)
    parser.add_argument('--quiet', '-q', action=CountAction, dest='verbose',
            const=-1, nargs=0)
    """

    def __call__(
        self,
        parser: typing.Any,
        namespace: argparse.Namespace,
        values: typing.Union[str, typing.Sequence[str], None],
        option_string: typing.Optional[str] = None,
    ) -> None:
        if self.const is None:
            self.const = 1
        try:
            val = getattr(namespace, self.dest) + self.const
        except TypeError:  # probably None
            val = self.const
        setattr(namespace, self.dest, val)


def main(cmdarg: typing.Optional[typing.List[str]]=None) -> int:
    cmdarg = sys.argv if cmdarg is None else cmdarg
    parsers = []
    parsers.append(ArgumentParser())
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), dest='_gl_verbose', metavar='VERBOSE', nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', nargs=0, default=0, action=CountAction, dest='verbose', const=-1)
    parsers[-1].add_argument('--dryrun', default=None, dest='_gl_dryrun', action='store_true')
    parsers[-1].add_argument('--version', action='store_true', help='show program\'s version number and exit')
    subp = parsers[-1].add_subparsers()
    px = subp.add_parser('convert', help='convert music file')
    px.set_defaults(subparser_func='convert')
    parsers.append(px)
    parsers[-1].add_argument('--cue', help='split args according to cue file and convert')
    parsers[-1].add_argument('--no-cue-check', action='store_true', help='do not check if there is a matching cue file')
    parsers[-1].add_argument('--force', action='store_true', help='force conversion even if target exists')
    parsers[-1].add_argument('--re-tag', '--retag', action='store_true', help='copy tags to existing files')
    parsers[-1].add_argument('--max-size', default=32, type=int, help='max file size to convert (default: %(default)sMb)')
    parsers[-1].add_argument('args', nargs='+', help='music files to convert')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('check', help='check if primary secondary conversion is necessary')
    px.set_defaults(subparser_func='check')
    parsers.append(px)
    parsers[-1].add_argument('--convert', action='store_true', help='convert files checked to be older/missing')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('find', help='find some music file in primary or secondary format')
    px.set_defaults(subparser_func='find')
    parsers.append(px)
    parsers[-1].add_argument('--artist', action='store_true', help='only show artist level')
    parsers[-1].add_argument('--album', action='store_true', help='only show album level')
    parsers[-1].add_argument('args', nargs='+', help='list of elements of filename to be found')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('sort', help='sort tmp directory to the primary and secondary format')
    px.set_defaults(subparser_func='sort')
    parsers.append(px)
    parsers[-1].add_argument('--convert', action='store_true', help='generate secondary format from primary')
    parsers[-1].add_argument('--test', action='store_true')
    parsers[-1].add_argument('--startwith', help='only sort if starting with path')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('flatten', help='flatten pictures into music directory (for picard to move along)')
    px.set_defaults(subparser_func='flatten')
    parsers.append(px)
    parsers[-1].add_argument('args', nargs='*', help='list of directories to recursively parse (default: . )')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('analyse', help='analyse a directory tree, to find music')
    px.set_defaults(subparser_func='analyse')
    parsers.append(px)
    parsers[-1].add_argument('args', nargs='*', help='list of directories to recursively parse (default: . )')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('cleanup', help='cleanup empty directories, old path formats, etc.')
    px.set_defaults(subparser_func='cleanup')
    parsers.append(px)
    parsers[-1].add_argument('--dedup', action='store_true', help='check and remove old paths in primary and secondary storage')
    parsers[-1].add_argument('--year', action='store_true', help='move albums to original year')
    parsers[-1].add_argument('--gen', action='store_true', help='generate year related metadata file')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('meta', help='show tag metadata')
    px.set_defaults(subparser_func='meta')
    parsers.append(px)
    parsers[-1].add_argument('args', nargs='+', type=ruamel.std.pathlib.Path, help='music files to process')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('image', help='copy image from to')
    px.set_defaults(subparser_func='image')
    parsers.append(px)
    parsers[-1].add_argument('--from', type=ruamel.std.pathlib.Path, help='music file to read image from')
    parsers[-1].add_argument('--to', type=ruamel.std.pathlib.Path, help='music file to write to')
    parsers[-1].add_argument('--all', action='store_true')
    parsers[-1].add_argument('--mp3', action='store_true')
    parsers[-1].add_argument('--check', type=ruamel.std.pathlib.Path, nargs='+', help='check dirs for cover art')
    parsers[-1].add_argument('--get', type=ruamel.std.pathlib.Path, nargs='+', help='get file cover art')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    px = subp.add_parser('html', help='generate html from .music.yaml')
    px.set_defaults(subparser_func='html')
    parsers.append(px)
    parsers[-1].add_argument('--force', action='store_true', help='force conversion even if up-to-date')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction, const=1)
    parsers[-1].add_argument('--quiet', '-q', default=0, nargs=0, action=CountAction, dest='verbose', const=-1)
    parsers.pop()
    if '--version' in cmdarg[1:]:
        if '-v' in cmdarg[1:] or '--verbose' in cmdarg[1:]:
            return list_versions(pkg_name='ruamel.music', version=None, pkgs=['mutagen', 'musicbrainzngs', 'ruamel.yaml', 'ruamel.doc.html', 'ruamel.std.pathlib'])
        print(__version__)
        return 0
    if '--help-all' in cmdarg[1:]:
        try:
            parsers[0].parse_args(['--help'])
        except SystemExit:
            pass
        for sc in parsers[1:]:
            print('-' * 72)
            try:
                parsers[0].parse_args([sc.prog.split()[1], '--help'])
            except SystemExit:
                pass
        sys.exit(0)
    args = parsers[0].parse_args(args=cmdarg[1:])
    for gl in ['verbose', 'dryrun']:
        glv = getattr(args, '_gl_' + gl, None)
        if isinstance(getattr(args, gl, None), (DefaultVal, type(None))) and glv is not None:
            setattr(args, gl, glv)
        delattr(args, '_gl_' + gl)
        if isinstance(getattr(args, gl, None), DefaultVal):
            setattr(args, gl, getattr(args, gl).val)
    cls = getattr(importlib.import_module('xxx.xxx'), 'XXX')
    obj = cls(args)
    funcname = getattr(args, 'subparser_func', None)
    if funcname is None:
        parsers[0].parse_args(['--help'])
    fun = getattr(obj, funcname + '_subcommand', None)
    if fun is None:
        fun = getattr(obj, funcname)
    ret_val = fun()
    if ret_val is None:
        return 0
    if isinstance(ret_val, int):
        return ret_val
    return -1

def list_versions(pkg_name: str, version: typing.Union[str, None], pkgs: typing.Sequence[str]) -> int:
    version_data = [
        ('Python', '{v.major}.{v.minor}.{v.micro}'.format(v=sys.version_info)),
        (pkg_name, __version__ if version is None else version),
    ]
    for pkg in pkgs:
        try:
            version_data.append(
                (pkg,  getattr(importlib.import_module(pkg), '__version__', '--'))
            )
        except ModuleNotFoundError:
            version_data.append((pkg, 'NA'))
        except KeyError:
            pass
    longest = max([len(x[0]) for x in version_data]) + 1
    for pkg, ver in version_data:
        print('{:{}s} {}'.format(pkg + ':', longest, ver))
    return 0


if __name__ == '__main__':
    sys.exit(main())
