# coding: utf-8

_package_data = dict(
    full_package_name='ruamel.music',
    version_info=(0, 5, 0),
    __version__='0.5.0',
    version_timestamp='2022-09-25 12:37:15',
    author='Anthon van der Neut',
    author_email='a.van.der.neut@ruamel.eu',
    description='handling of music files: conversion, playing',
    toxver=['3.8'],
    entry_points='music=ruamel.music.__main__:main',
    install_requires=[
        'mutagen',
        'musicbrainzngs',
        'ruamel.yaml',
        'ruamel.doc.html',
        'ruamel.std.pathlib',
    ],
    license='Copyright Ruamel bvba 2013-2022',
    print_allowed=True,
    python_requires='>=3',
)


version_info = _package_data['version_info']
__version__ = _package_data['__version__']

_cligen_data = """\
# all tags start with an uppercase char and can often be shortened to three and/or one
# characters. If a tag has multiple uppercase letter, only using the uppercase letters is a
# valid shortening
# Tags used:
# !Commandlineinterface, !Cli,
# !Option, !Opt, !O
  # - !Option [all, !Action store_true, !Help build sdist and wheels for all platforms]
# !PreSubparserOption, !PSO
# !Alias for a subparser
# - !DefaultSubparser  # make this (one) subparser default
# !Help, !H
# !HelpWidth 40    # width of the left side column width option details
# !Argument, !Arg
  # - !Arg [files, nargs: '*', !H files to process]
# !Module   # make subparser function calls imported from module
# !Instance # module.Class: assume subparser method calls on instance of Class imported from module
# !Main     # function to call/class to instantiate, no subparsers
# !Action # either one of the actions in cligen subdir _action (by stem of the file) or e.g. "store_action"
# !Config YAML/INI/PON  read defaults from config file
# !AddDefaults ' (default: %(default)s)'
# !Prolog (sub-)parser prolog/description text (for multiline use | ), used as subparser !Help if not set
# !Epilog (sub-)parser epilog text (for multiline use | )
# !NQS used on arguments, makes sure the scalar is non-quoted e.g for instance/method/function
#      call arguments, when cligen knows about what argument a keyword takes, this is not needed
!Cli 0:
- !Opt [verbose, v, !Help increase verbosity level, !Action count, const: 1, nargs: 0, default: 0]
- !Opt [quiet, q, !Action count, dest: verbose, const: -1, nargs: 0]
- !PSO [dryrun, !Action store_true]
- !Instance xxx.xxx.XXX
- convert:
  - !Opt [cue, !Help split args according to cue file and convert]
  - !Opt [no-cue-check, !Action store_true, !Help do not check if there is a matching cue file]
  - !Opt [force, !Action store_true, !Help force conversion even if target exists]
  - !Opt [re-tag, retag, !Action store_true, !Help copy tags to existing files]
  - !Opt [max-size, type: int, default: 32, !Help 'max file size to convert (default: %(default)sMb)']
  - !Arg [args, nargs: +, !Help music files to convert]
  - !Help convert music file
- check:
  - !Opt [convert, !Action store_true, !Help convert files checked to be older/missing]
  - !Help check if primary secondary conversion is necessary
- find:
  - !Opt [artist, !Action store_true, !Help only show artist level]
  - !Opt [album, !Action store_true, !Help only show album level]
  - !Arg [args, nargs: +, !Help list of elements of filename to be found]
  - !Help find some music file in primary or secondary format
- sort:
  - !Opt [convert, !Action store_true, !Help generate secondary format from primary]
  - !Opt [test, !Action store_true]
  - !Opt [startwith, !Help only sort if starting with path]
  - !Help sort tmp directory to the primary and secondary format
- flatten:
  - !Arg [args, nargs: '*', !Help 'list of directories to recursively parse (default: . )']
  - !Help flatten pictures into music directory (for picard to move along)
- analyse:
  - !Arg [args, nargs: '*', !Help 'list of directories to recursively parse (default: . )']
  - !Help analyse a directory tree, to find music
- cleanup:
  - !Opt [dedup, !Action store_true, !Help check and remove old paths in primary and secondary storage]
  - !Opt [year, !Action store_true, !Help move albums to original year]
  - !Opt [gen, !Action store_true, !Help generate year related metadata file]
  - !Help cleanup empty directories, old path formats, etc.
- meta:
  - !Arg [args, nargs: +, type: ruamel.std.pathlib.Path, !Help music files to process]
  - !Help show tag metadata
- image:
  - !Opt [from, type: ruamel.std.pathlib.Path, !Help music file to read image from]
  - !Opt [to, type: ruamel.std.pathlib.Path, !Help music file to write to]
  - !Opt [all, !Action store_true]
  - !Opt [mp3, !Action store_true]
  - !Opt [check, type: ruamel.std.pathlib.Path, nargs: +, !Help check dirs for cover art]
  - !Opt [get, type: ruamel.std.pathlib.Path, nargs: +, !Help get file cover art]
  - !Help copy image from to
- html:
  - !Opt [force, !Action store_true, !Help force conversion even if up-to-date]
  - !Help generate html from .music.yaml
"""  # NOQA
