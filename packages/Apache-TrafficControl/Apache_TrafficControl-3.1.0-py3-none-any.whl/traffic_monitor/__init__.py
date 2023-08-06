#!/usr/bin/env python3
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
.. _tmaccess:

.. program:: tmaccess

``tmaccess``
============
This module provides a set of functions meant to provide ease-of-use functionality for interacting
with the Traffic Monitor API. It provides scripts named :file:`tm{method}` where `method` is the
name of an HTTP method (in lowercase). Collectively they are referred to as :program:`tmaccess`
Implemented methods thus far are:

- delete
- head
- get
- options
- patch
- post
- put

Arguments and Flags
-------------------
Usage: :samp:`tm{method} [-kvhfp] [--tm-url URL] [--response-headers] [--request-headers] [--request-payload] PATH [DATA]`
.. option:: PATH

	This is the request path.

.. option:: DATA

	An optional positional argument that is a data payload to pass to the Traffic Monitor server in the
	request body. If this is the absolute or relative path to a file, the contents of the file will
	instead be read and used as the request payload.

.. option:: -h, --help

	Print usage information and exit

.. option:: -f, --full

	Output the full HTTP exchange including request method line, request headers, request body (if
	any), response status line, and response headers (as well as the response body, if any). This is
	equivalent to using :option:`--request-headers`, :option:`--request-payload`, and
	:option:`--response-headers` at the same time, and those options will have no effect if given.
	(Default: false)

.. option:: -k, --insecure

	Do not verify SSL certificates - typically useful for making requests to development or testing
	servers as they frequently have self-signed certificates. (Default: false)

.. option:: -p, --pretty

	Pretty-print any payloads that are output as formatted JSON. Has no effect on plaintext payloads.
	Uses tab characters for indentation. (Default: false)

.. option:: -v, --version

	Print version information and exit.

.. option:: --request-headers

	Output the request method line and any and all request headers. (Default: false)

.. option:: --request-payload

	Output the request body if any was sent. Will attempt to pretty-print the body as JSON if
	:option:`--pretty` is used. (Default: false)

.. option:: --response-headers

	Output the response status line and any and all response headers. (Default: false)

.. option:: --tm-url URL

	The :abbr:`FQDN (Fully Qualified Domain Name)` and optionally the port and scheme of the Traffic
	Ops server. This will override :envvar:`TM_URL`. The format is the same as for :envvar:`TM_URL`.
	(Default: uses the value of :envvar:`TM_URL`)

Environment Variables
---------------------
If defined, :program:`tmaccess` scripts will use the :envvar:`TM_URL` environment variable to
define their connection to the Traffic Monitor server. Typically, setting these is easier than
using the long option :option:`--tm-url` on every invocation.

Exit Codes
----------
The exit code of a :program:`tmaccess` script can sometimes be used by the caller to determine what
the result of calling the script was without needing to parse the output. The exit codes used are:

0
	The command executed successfully, and the result is on STDOUT.
1
	Typically this exit code means that an error was encountered when parsing positional command
	line arguments. However, this is also the exit code used by most Python interpreters to signal
	an unhandled exception.
2
	Signifies a runtime error that caused the request to fail - this is **not** generally indicative
	of an HTTP client or server error, but rather an underlying issue connecting to or
	Traffic Monitor. This is distinct from an exit code of ``32`` in that the *format* of the
	arguments was correct, but there was some problem with the *value*. For example, passing
	``https://test:`` to :option:`--tm-url` will cause an exit code of ``2``, not ``32``.
4
	An HTTP client error occurred. The HTTP stack will be printed to stdout as indicated by other
	options - meaning by default it will only print the response payload if one was given, but will
	respect options like e.g. :option:`--request-payload` as well as
	:option:`-p`/:option:`--pretty`.
5
	An HTTP server error occurred. The HTTP stack will be printed to stdout as indicated by other
	options - meaning by default it will only print the response payload if one was given, but will
	respect options like e.g. :option:`--request-payload` as well as
	:option:`-p`/:option:`--pretty`.
32
	This is the error code emitted by Python's :mod:`argparse` module when the passed arguments
	could not be parsed successfully.

.. note:: The way exit codes ``4`` and ``5`` are implemented is by returning the status code of the
	HTTP request divided by 100 whenever it is at least 400. This means that if the Traffic Monitor
	server ever started returning e.g. 700 status codes, the exit code of the script would be 7.


Module Reference
================

"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import json
import logging
import os
import sys
from typing import NamedTuple, Optional, Union
from urllib.parse import urlparse
import requests

# These are installed by the same package, so the versions will be the same.
# TODO: refactor the Python client to be a single package with component-specific modules
from trafficops.__version__ import __version__

from requests.exceptions import RequestException

l = logging.getLogger()
l.disabled = True
logging.basicConfig(level=logging.CRITICAL+1)

def output(
	resp,
	pretty: bool,
	request_header: bool,
	response_header: bool,
	request_payload: bool,
	indent: Union[int, str, None] = '\t'
) -> None:
	"""
	Prints the passed response object in a format consistent with the other parameters.

	:param r: The :mod:`requests` response object being printed
	:param pretty: If :const:`True`, attempt to pretty-print payloads as JSON
	:param request_header: If :const:`True`, print request line and request headers
	:param response_header: If :const:`True`, print response line and response headers
	:param request_payload: If :const:`True`, print the request payload
	:param indent: An optional number of spaces for pretty-printing indentation (default is the tab character)
	"""
	if request_header:
		print(resp.request.method, resp.request.path_url, "HTTP/1.1")
		for header, value in resp.request.headers.items():
			print("%s:" % header, value)
		print()

	if request_payload and resp.request.body:
		try:
			result = resp.request.body if not pretty else json.dumps(json.loads(resp.request.body))
		except ValueError:
			result = resp.request.body
		print(result, end="\n\n")

	if response_header:
		print("HTTP/1.1", resp.status_code, end="")
		print(" "+resp.reason if resp.reason else "")
		for header, value in resp.headers.items():
			print("%s:" % header, value)
		print()

	try:
		result = resp.text if not pretty else json.dumps(resp.json(), indent=indent)
	except ValueError:
		result = resp.text
	print(result)

# Bug in Python 3.9 handling for Pylint; doesn't detect NamedTuple as inheritable.
#pylint:disable=inherit-non-class
class Config(NamedTuple):
	"""
	Config represents configuration produced by parsing command-line arguments combined with any
	and all relevant environment variables.
	"""
	tm_url: str
	path: str
	data: Optional[bytes]
	request_payload: bool
	request_headers: bool
	response_headers: bool
	pretty: bool

def parse_arguments(program: str) -> Config:
	"""
	A common-use function that parses the command line arguments.

	:param program: The name of the program being run - used for usage informational output
	:returns: The Traffic Ops HTTP session object, the requested path, any data to be sent, an output
	          format specification, whether or not the path is raw, and whether or not output should
	          be prettified
	"""
	parser = ArgumentParser(
		prog=program,
		formatter_class=ArgumentDefaultsHelpFormatter,
		description="A helper program for interfacing with the Traffic Monitor API",
		epilog=(
			"Typically, one will want to connect and authenticate by defining the 'TM_URL' "
			"environment variable rather than the '--tm-url' command-line flag. That flag is only "
			"required when said environment variable is not defined.\n"
			"%(prog)s will exit with a success provided a response was received and the status "
			"code of said response was less than 400. The exit code will be 1 if command line "
			"arguments cannot be parsed or authentication with the Traffic Monitor server fails. "
			"In the event of some unknown error occurring when waiting for a response, the exit "
			"code will be 2. If the server responds with a status code indicating a client or "
			"server error, that status code will be (integer) divided by 100 to define the exit "
			"code."
		)
	)

	parser.add_argument(
		"--tm-url",
		type=str,
		help=(
			"The fully qualified domain name of the Traffic Monitor server. Overrides '$TM_URL'. "
			"The format for both the environment variable and the flag is "
			"'[scheme]hostname[:port]'. That is, ports should be specified here, and they need not "
			"start with 'http://' or 'https://'. HTTPS is the assumed protocol unless the scheme "
			"_is_ provided and is 'http://'."
		)
	)
	parser.add_argument("-k", "--insecure", action="store_true", help="Do not verify SSL certificates")
	parser.add_argument(
		"-f",
		"--full",
		action="store_true",
		help=(
			"Also output HTTP request/response lines and headers, and request payload. This is "
			"equivalent to using '--request-headers', '--response-headers' and "
			"'--request-payload' at the same time."
		)
	)
	parser.add_argument(
		"--request-headers",
		action="store_true",
		help="Output request method line and headers"
	)
	parser.add_argument(
		"--response-headers",
		action="store_true",
		help="Output response status line and headers"
	)
	parser.add_argument(
		"--request-payload",
		action="store_true",
		help="Output request payload (will try to pretty-print if '--pretty' is given)"
	)
	parser.add_argument(
		"-p",
		"--pretty",
		action="store_true",
		help=(
			'Pretty-print payloads as JSON. Note that this will make Content-Type headers "wrong", '
			"in general"
		)
	)
	parser.add_argument(
		"-v",
		"--version",
		action="version",
		help="Print version information and exit",
		version="%(prog)s v"+__version__
	)
	parser.add_argument("PATH", help="The path to the resource being requested")
	parser.add_argument(
		"DATA",
		help=(
			"An optional data string to pass with the request. If this is a filename, the contents "
			"of the file will be sent instead."
		),
		nargs='?'
	)


	args = parser.parse_args()

	try:
		tm_host = args.tm_url if args.tm_url else os.environ["TM_URL"]
	except KeyError as e:
		raise KeyError("Traffic Monitor hostname not set! Set the TM_URL environment variable or "
		               "use '--tm-url'.") from e

	original_tm_host = tm_host
	tm_host = urlparse(tm_host, scheme="https")
	use_ssl = tm_host.scheme.lower() == "https"
	tm_port = tm_host.port
	if tm_port is None:
		if use_ssl:
			tm_port = 443
		else:
			tm_port = 80

	tm_host = tm_host.hostname
	if not tm_host:
		raise KeyError(f"Invalid URL/host for Traffic Monitor: '{original_tm_host}'")

	tm_url = f"{'https://' if use_ssl else 'http://'}{tm_host}:{tm_port}"

	data = args.DATA
	if data and os.path.isfile(data):
		with open(data) as data_file:
			data = data_file.read()

	if isinstance(data, str):
		data = data.encode()

	return Config(
		tm_url,
		args.PATH,
		data,
		args.request_payload or args.full,
		args.request_headers or args.full,
		args.response_headers or args.full,
		args.pretty
	)

def request(method: str) -> int:
	"""
	All of the scripts wind up calling this function to handle their common functionality.

	:param method: The name of the request method to use (case-insensitive)
	:returns: The program's exit code
	"""
	try:
		cfg = parse_arguments("to%s" % method)
	except (PermissionError, KeyError, ConnectionError) as e:
		print(e, file=sys.stderr)
		return 1

	full_url = f"{cfg.tm_url.removesuffix('/')}/{cfg.path.removeprefix('/')}"

	try:
		if cfg.data is not None:
			resp = requests.request(method, full_url, data=cfg.data)
		else:
			resp = requests.request(method, full_url)
	except (RequestException, ValueError) as e:
		print("Error occurred: ", e, file=sys.stderr)
		return 2

	output(resp, cfg.pretty, cfg.request_headers, cfg.response_headers, cfg.request_payload)
	return 0 if resp.status_code < 400 else resp.status_code // 100

def get() -> int:
	"""
	Entry point for :program:`tmget`

	:returns: The program's exit code
	"""
	return request("get")

def put() -> int:
	"""
	Entry point for :program:`tmput`

	:returns: The program's exit code
	"""
	return request("put")

def post() -> int:
	"""
	Entry point for :program:`tmpost`

	:returns: The program's exit code
	"""
	return request("post")

def delete() -> int:
	"""
	Entry point for :program:`tmdelete`

	:returns: The program's exit code
	"""
	return request("delete")

def options() -> int:
	"""
	Entry point for :program:`tmoptions`

	:returns: The program's exit code
	"""
	return request("options")

def head() -> int:
	"""
	Entry point for :program:`tmhead`

	:returns: The program's exit code
	"""
	return request("head")

def patch() -> int:
	"""
	Entry point for :program:`tmpatch`

	:returns: The program's exit code
	"""
	return request("patch")
