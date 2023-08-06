#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
cli: the CLI client for GLIMPS detect.

This client aims to use GLIMPS detect API inside a shell.
`send` is the default command ; you can omit it to simplify uses.
Show `--help` to see how to use it.

>>> python3 -m gdetect --help
Usage: python -m gdetect [OPTIONS] COMMAND [ARGS]...

Options:
  --url TEXT    url to GLIMPS Detect API
  --token TEXT  authentication token
  --insecure    disable HTTPS check
  --no-cache    submit file even if a result already exists
  --help        Show this message and exit.

Commands:
  send*    send file to API.
  get      get result for given uuid.
  waitfor  send a file and wait for the result.
  search   get result for given sha256.
"""

import os

import click
import rich
from click_default_group import DefaultGroup
from rich.console import Console

from gdetect import exceptions, log
from gdetect.api import Client
from gdetect.exceptions import GDetectError

# initialize rich Console for pretty print
console = Console()


@click.group(cls=DefaultGroup, default="send", default_if_no_args=True)
@click.option("--url", default=os.getenv("API_URL"), help="url to GLIMPS Detect API")
@click.option("--token", default=os.getenv("API_TOKEN"), help="authentication token")
@click.option("--insecure", is_flag=True, help="bypass HTTPS check")
@click.option(
    "--no-cache",
    "nocache",
    is_flag=True,
    help="submit file even if a result already exists",
)
@click.pass_context
def gdetect(ctx, url, token, insecure, nocache):
    """CLI for GLIMPS detect"""
    ctx.ensure_object(dict)

    ctx.obj["logger"] = log.get_logger()
    ctx.obj["logger"].disabled = True
    if insecure:
        console.print("untrusted: SSL verification disabled", style="bold red")
    ctx.obj["client"] = Client(url, token)
    ctx.obj["client"].verify = not insecure
    ctx.obj["no_cache"] = nocache


@gdetect.command("send")
@click.pass_context
@click.argument("filename")
@click.option("-t", "--tag", multiple=True, help="tags to assign to the file.")
@click.option("-d", "--description", help="description of the file.")
def send(ctx, filename, tag, description):
    """send file to API."""
    try:
        uuid = ctx.obj["client"].push(
            filename,
            bypass_cache=ctx.obj["no_cache"],
            tags=tag,
            description=description,
        )
        console.print(uuid)

    except GDetectError:
        print_response_error_msg(ctx.obj["client"].response.message)


@gdetect.command("get")
@click.argument("uuid")
@click.option("--retrieve-urls", is_flag=True, default=False, help="retrieve urls")
@click.pass_context
def get(ctx, uuid, retrieve_urls):
    """get result for given uuid."""
    try:
        result = ctx.obj["client"].get_by_uuid(uuid)
        rich.print_json(data=result)
        if retrieve_urls:
            print_urls()

    except GDetectError:
        print_response_error_msg(ctx.obj["client"].response.message)


@gdetect.command("search")
@click.argument("sha256")
@click.option("--retrieve-urls", is_flag=True, help="retrieve urls")
@click.pass_context
def search(ctx, sha256, retrieve_urls):
    """search a file with given sha256."""
    try:
        result = ctx.obj["client"].get_by_sha256(sha256)
        rich.print_json(data=result)
        if retrieve_urls:
            print_urls()
    except GDetectError:
        print_response_error_msg(ctx.obj["client"].response.message)


@gdetect.command("waitfor")
@click.pass_context
@click.argument("filename")
@click.option("--timeout", default=180, help="set a timeout in seconds")
@click.option("-t", "--tag", multiple=True, help="tags to assign to the file.")
@click.option("-d", "--description", help="description of the file.")
@click.option("--retrieve-urls", is_flag=True, help="retrieve urls")
def waitfor(ctx, filename, timeout, tag, description, retrieve_urls):
    """send a file and wait for the result."""
    try:
        result = ctx.obj["client"].waitfor(
            filename,
            bypass_cache=ctx.obj["no_cache"],
            timeout=timeout,
            tags=tag,
            description=description,
        )
        rich.print_json(data=result)
        if retrieve_urls:
            print_urls()
    except GDetectError:
        print_response_error_msg(ctx.obj["client"].response.message)


def print_response_error_msg(msg):
    """print error messages inside console"""
    console.print(f"An error occurs: {msg}", style="bold red")


@click.pass_context
def print_urls(ctx):
    """Print url for token and analyse view"""
    try:
        url_token_view = ctx.obj["client"].extract_url_token_view()
        console.print("TOKEN VIEW URL: ", url_token_view)
    except (exceptions.MissingToken, exceptions.MissingResponse):
        pass

    try:
        url_expert_analyse = ctx.obj["client"].extract_expert_url()
        console.print("ANALYSE VIEW URL: ", url_expert_analyse)
    except (exceptions.MissingSID, exceptions.MissingResponse):
        pass


if __name__ == "__main__":
    gdetect()
