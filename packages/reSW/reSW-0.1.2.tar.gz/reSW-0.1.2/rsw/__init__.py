#!/usr/bin/env python
# -*- coding: utf-8 -*-

# reStructuredWeb (rSW, reSW or rstW) -- static site generator.
# Copyright (c) 2022 ge https://nixnahcks.net/resw/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""reSW static site generator.

Usage: rsw init [--no-makefile] [<name>]
       rsw build [-c <file>]
       rsw print [-c <file>] [--default] [--json]
       rsw (-h | --help | -v | --version)

Commands:
  init          initialise new site.
  build         build site.
  print         print configuration.

Options:
  -c <file>, --config <file>    configuaration file.
  -j, --json                    JSON output.
  -d, --default                 print default config.
  -M, --no-makefile             do not create Makefile.
  -h, --help                    print this help message and exit.
  -v, --version                 print version and exit.

Copyright (C) 2022 ge <http://nixhacks.net/resw/>.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
"""

__version__ = '0.1.2'

import os
import sys
import shutil
import datetime
import logging

import toml
import jinja2
import colorlog
import docopt

from typing import List
from collections import namedtuple
from docutils.core import publish_parts
from docutils.core import publish_doctree
from docutils.writers import html5_polyglot

from docutils import nodes
from docutils.parsers.rst import directives
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# ------------------------------------------------------------- #
# Setup logger.                                                 #
# ------------------------------------------------------------- #

LOGFORMAT = '%(log_color)s%(levelname)-8s%(reset)s \
%(log_color)s%(message)s%(reset)s'
log = logging.getLogger('reStructuredWeb')
log.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(colorlog.ColoredFormatter(LOGFORMAT))
log.addHandler(handler)

# ------------------------------------------------------------- #
# Configuration.                                                #
# ------------------------------------------------------------- #

CONFIG_FILE = 'settings.toml'
DEFAULT_CONFIG = {
    'defaults': {
        'template': 'template.jinja2',
        'type': 'page',
    },
    'dirs': {
        'build_dir': 'build',
        'content_dir': 'content',
        'templates_dir': 'layouts',
        'static_dir': 'static',
    },
    'site': {
        'datetime_format': '%Y-%m-%d',
    },
    'pygments': {
        'theme': 'default',
    },
    'docutils': {},
}

def merge_dicts(a: dict, b: dict, path = None) -> dict:
    """Merge b into a. Return modified a.
    Ref: https://stackoverflow.com/a/7205107
    """
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dicts(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass  # same leaf value
            else:
                a[key] = b[key]  # replace existing key's values
        else:
            a[key] = b[key]
    return a

def load_config(config_file: str = CONFIG_FILE):
    """Load configuration file and fallback to default config."""
    try:
        with open(config_file, 'r') as file:
            config = toml.loads(file.read())
    except OSError as err:
        log.error("Cannot load configuration from '{}': {}".format(
            config_file, err))
        sys.exit(1)
    return merge_dicts(DEFAULT_CONFIG, config)

def load_config_wrapper(args: dict) -> dict:
    if args['--config']:
        config = load_config(config_file = args['--config'])
    else:
        config = load_config()
    return config

# ------------------------------------------------------------- #
# Parse docinfo from rST files.                                 #
# ------------------------------------------------------------- #

# Code below is copy-pasted from https://github.com/zeddee/parsedocinfo
# and modified a little bit. Zeddee, thank you!
# Original license SPDX identifier: Apache-2.0
# -- parsedocinfo BEGIN --

DocInfo = namedtuple("DocInfo", 'name body')

def _traverse_fields(field: List) -> DocInfo:
    field_name = field.getElementsByTagName("field_name")[0]
    field_body = field.getElementsByTagName("field_body")[0]
    return DocInfo(field_name.firstChild.nodeValue,
        " ".join(val.firstChild.nodeValue for val in field_body.childNodes))

def _traverse_docinfo(docinfo_list: List) -> List[DocInfo]:
    out = []
    for i in docinfo_list:
        for node in i.childNodes:
            if node.tagName == "field":
                out.append(_traverse_fields(node))
            else:
                out.append(DocInfo(node.tagName,
                    " ".join(val.nodeValue for val in node.childNodes)
                    )
                )
    return out

def parsedocinfo(data: str) -> dict:
    docinfo = publish_doctree(data).asdom().getElementsByTagName("docinfo")
    return dict(_traverse_docinfo(docinfo))

# -- parsedocinfo END --

# ------------------------------------------------------------- #
# Extra reStructuredText directives and roles                   #
# ------------------------------------------------------------- #

# DIRECTIVES

# Pygments reST `code-block` directive.
# Source: https://docutils.sourceforge.io/sandbox/code-block-directive/
# `code-block` BEGIN

pygments_formatter = HtmlFormatter()

def pygments_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):
    try:
        lexer = get_lexer_by_name(arguments[0])
    except ValueError:
        # no lexer found - use the text one instead of an exception
        lexer = get_lexer_by_name('text')
    parsed = highlight(u'\n'.join(content), lexer, pygments_formatter)
    return [nodes.raw('', parsed, format='html')]

pygments_directive.arguments = (1, 0, 1)
pygments_directive.content = 1
directives.register_directive('code-block', pygments_directive)

# `code-block` END

# ------------------------------------------------------------- #
# Jinja2 specific functions.                                    #
# ------------------------------------------------------------- #

def render_template(template: str, templates_dir = '.', **kwargs) -> str:
    """Render Jinja2 template from file. Usage::

        render_template('index.j2',
            templates_dir = './templates',
            title = 'My title')
    """
    env = jinja2.Environment(loader = jinja2.FileSystemLoader(templates_dir))
    return env.get_template(template).render(**kwargs)

# ------------------------------------------------------------- #
# Render HTML from reStructuredText.                            #
# ------------------------------------------------------------- #

def render_html_body(config: dict, text: str) -> str:
    """Return HTML body converted from reStructuredText.
    See:
        * help(docutils.core.publish_parts)
        * https://docutils.sourceforge.io/docs/user/config.html
    """
    html = publish_parts(source = text, writer = html5_polyglot.Writer(),
        settings_overrides = config['docutils']
    )
    return html['body']

# ------------------------------------------------------------- #
# File operations.                                              #
# ------------------------------------------------------------- #

def find_rst_files(directory: str) -> list:
    """Return the list of rST files from directory.
    Scan subdirectories too.
    """
    file_list = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            if os.path.splitext(name)[1] == '.rst':
                file_list.append(os.path.join(root, name))
    return file_list

def write_to_file(path: str, data: str):
    with open(path, 'w', encoding = 'utf-8') as file:
        file.write(data)

def copy_files(source_dir: str, destination_dir: str):
    shutil.copytree(source_dir, destination_dir,
        ignore = shutil.ignore_patterns('*.rst'),
        dirs_exist_ok = True)

# ------------------------------------------------------------- #
# Build site!                                                   #
# ------------------------------------------------------------- #

def aggregate_lists(config: dict, file_list: list) -> dict:
    posts = []
    pages = []
    for rst_file in file_list:
        with open(rst_file, 'r', encoding = 'utf-8') as rst:
            docinfo = parsedocinfo(rst.read())

        # Validate date format
        try:
            dt = datetime.datetime.strptime(docinfo['date'],
                config['site']['datetime_format'])
        except (KeyError, ValueError) as err:
            log.error('Wrong formatted or missing date in file' +
                '\'{}\': {}'.format(rst_file, err))

        # Add path ot file
        docinfo['path'] = '/' + os.path.relpath(
            os.path.splitext(rst_file)[0] + '.html',
            config['dirs']['content_dir'])
        try:
            if docinfo['type'] == 'post':
                posts.append(docinfo)
            else:
                pages.append(docinfo)
        except KeyError:
            if config['defaults']['type'] == 'post':
                posts.append(docinfo)
            else:
                pages.append(docinfo)

    # Sort posts by date (newest in top)
    posts.sort(key=lambda date: datetime.datetime.strptime(date['date'],
        config['site']['datetime_format']), reverse = True)

    return {'posts': posts, 'pages': pages}

def build(config: dict):
    """Build site."""
    # Prepare build directory
    os.makedirs(config['dirs']['build_dir'], exist_ok = True)

    log.info('Collecting data ...')
    rst_files = find_rst_files(config['dirs']['content_dir'])
    lists = aggregate_lists(config, rst_files)

    for rst_file in rst_files:
        with open(rst_file, 'r', encoding = 'utf-8') as rst:
            source = rst.read()

        log.info('Parsing docinfo: %s' % rst_file)
        page_docinfo = parsedocinfo(source)

        # Render HTML files
        html_file_path = os.path.join(config['dirs']['build_dir'],
            os.path.relpath(os.path.splitext(rst_file)[0] + '.html',
            config['dirs']['content_dir']))

        log.info('Rendering page: %s' % html_file_path)

        # Get page template from docinfo
        try:
            template = page_docinfo['template']
            if not os.path.exists(os.path.join(
                config['dirs']['templates_dir'], template)):
                log.error('{}: Template does not exist: {}'.format(
                    rst_file, template))
                sys.exit(1)
        except KeyError:
            template = config['defaults']['template']

        # Render HTML
        html_body = render_html_body(config, source)

        # Render template
        html_page = render_template(
            template,
            templates_dir = config['dirs']['templates_dir'],
            pygments_theme = config['pygments']['theme'],
            site = config['site'],
            page = page_docinfo,
            aggr = lists,
            html = html_body
        )

        # Save rendered page
        os.makedirs(os.path.dirname(html_file_path), exist_ok = True)
        write_to_file(html_file_path, html_page)

    # Copy additional files to build_dir
    log.info("Copying static files from '{}' and '{}' to '{}'".format(
        config['dirs']['static_dir'],
        config['dirs']['content_dir'],
        config['dirs']['build_dir']))

    copy_files(config['dirs']['static_dir'], config['dirs']['build_dir'])
    copy_files(config['dirs']['content_dir'], config['dirs']['build_dir'])

    log.info('Success')

# ------------------------------------------------------------- #
# Command Line Interface.                                       #
# ------------------------------------------------------------- #

def init(dirname: str = '.', no_makefile: bool = False):
    """Initialise new site."""
    # Make site dirs
    for dir in list(DEFAULT_CONFIG['dirs'].keys()):
        if dir == 'build_dir':
            pass
        else:
            os.makedirs(os.path.join(dirname,
                DEFAULT_CONFIG['dirs'][dir]), exist_ok = True)

    # Make Makefile
    if not no_makefile:
        # Get package dir `this_dir`
        this_dir, this_filename = os.path.split(__file__)
        makefile = render_template('Makefile.jinja2',
            templates_dir = this_dir,
            content_dir = DEFAULT_CONFIG['dirs']['content_dir'],
            static_dir = DEFAULT_CONFIG['dirs']['static_dir'],
            build_dir = DEFAULT_CONFIG['dirs']['build_dir'],
            config = CONFIG_FILE
        )
        write_to_file(os.path.join(dirname, 'Makefile'), makefile)

    # Make configuration file
    settings = toml.dumps(DEFAULT_CONFIG)
    write_to_file(os.path.join(dirname, CONFIG_FILE), settings)

    # Make .gitignore
    gitignore = 'build/'  # file content
    write_to_file(os.path.join(dirname, '.gitignore'), gitignore)

    log.info("Site initialised in '%s'" % dirname)

def print_config(config: dict, args: dict):
    if args['--json']:
        import json
        print(json.dumps(config, indent = 2))
    else:
        import pprint
        pprint.pprint(config)

def cli():
    args = docopt.docopt(__doc__, version = __version__)

    if args['init']:
        if args['<name>']:
            init(dirname = args['<name>'], no_makefile = args['--no-makefile'])
        else:
            init(dirname = os.getcwd(), no_makefile = args['--no-makefile'])
    elif args['build']:
        build(config = load_config_wrapper(args))
    elif args['print']:
        if args['--default']:
            print_config(DEFAULT_CONFIG, args)
        else:
            print_config(load_config_wrapper(args), args)
    else:
        pass

if __name__ == '__main__':
    cli()
