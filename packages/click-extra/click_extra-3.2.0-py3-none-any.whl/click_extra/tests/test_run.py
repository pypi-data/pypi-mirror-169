# Copyright Kevin Deldycke <kevin@deldycke.com> and contributors.
# All Rights Reserved.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

"""Test all runner utilities as well as all the test and pytest helpers."""

import os
from pathlib import Path

import click
from click import echo, pass_context, secho, style, utils
from cloup import Style
from pytest_cases import fixture, parametrize

from ..logging import logger
from ..platform import is_windows
from ..run import env_copy
from .conftest import command_decorators, skip_windows_colors


def test_real_fs():
    """Check a simple test is not caught into the CLI runner fixture which is
    encapsulating all filesystem access into temporary directory structure."""
    assert str(Path(__file__)).startswith(str(Path.cwd()))


def test_temporary_fs(runner):
    """Check the CLI runner fixture properly encapsulated the filesystem in temporary
    directory."""
    assert not str(Path(__file__)).startswith(str(Path.cwd()))


def test_env_copy():
    env_var = "MPM_DUMMY_ENV_VAR_93725"
    assert env_var not in os.environ

    no_env = env_copy()
    assert no_env is None

    extended_env = env_copy({env_var: "yo"})
    assert env_var in extended_env
    assert extended_env[env_var] == "yo"
    assert env_var not in os.environ


@click.command
@pass_context
def run_cli1(ctx):
    """https://github.com/pallets/click/issues/2111."""

    echo(Style(fg="green")("echo()"))
    echo(Style(fg="green")("echo(color=None)"), color=None)
    echo(Style(fg="red")("echo(color=True) bypass invoke.color = False"), color=True)
    echo(Style(fg="green")("echo(color=False)"), color=False)

    secho("secho()", fg="green")
    secho("secho(color=None)", fg="green", color=None)
    secho("secho(color=True) bypass invoke.color = False", fg="red", color=True)
    secho("secho(color=False)", fg="green", color=False)

    logger.warning("Is the logger colored?")

    print(style("print() bypass Click.", fg="blue"))

    echo(f"Context.color = {ctx.color!r}")
    echo(f"click.utils.should_strip_ansi = {utils.should_strip_ansi()!r}")


@fixture
@parametrize("cmd_decorator", command_decorators(no_groups=True))
def color_cli(cmd_decorator):
    @cmd_decorator
    @pass_context
    def run_cli2(ctx):
        """https://github.com/pallets/click/issues/2111."""

        echo(Style(fg="green")("echo()"))
        echo(Style(fg="green")("echo(color=None)"), color=None)
        echo(
            Style(fg="red")("echo(color=True) bypass invoke.color = False"), color=True
        )
        echo(Style(fg="green")("echo(color=False)"), color=False)

        secho("secho()", fg="green")
        secho("secho(color=None)", fg="green", color=None)
        secho("secho(color=True) bypass invoke.color = False", fg="red", color=True)
        secho("secho(color=False)", fg="green", color=False)

        logger.warning("Is the logger colored?")

        print(style("print() bypass Click.", fg="blue"))

        echo(f"Context.color = {ctx.color!r}")
        echo(f"click.utils.should_strip_ansi = {utils.should_strip_ansi()!r}")

    return run_cli2


def check_default_colored_rendering(result):
    assert result.exit_code == 0
    assert result.output.startswith(
        "\x1b[32mecho()\x1b[0m\n"
        "\x1b[32mecho(color=None)\x1b[0m\n"
        "\x1b[31mecho(color=True) bypass invoke.color = False\x1b[0m\n"
        "echo(color=False)\n"
        "\x1b[32msecho()\x1b[0m\n"
        "\x1b[32msecho(color=None)\x1b[0m\n"
        "\x1b[31msecho(color=True) bypass invoke.color = False\x1b[0m\n"
        "secho(color=False)\n"
        "\x1b[34mprint() bypass Click.\x1b[0m\n"
    )
    assert result.stderr == "\x1b[33mwarning: \x1b[0mIs the logger colored?\n"


def check_default_uncolored_rendering(result):
    assert result.exit_code == 0
    assert result.output.startswith(
        "echo()\n"
        "echo(color=None)\n"
        "\x1b[31mecho(color=True) bypass invoke.color = False\x1b[0m\n"
        "echo(color=False)\n"
        "secho()\n"
        "secho(color=None)\n"
        "\x1b[31msecho(color=True) bypass invoke.color = False\x1b[0m\n"
        "secho(color=False)\n"
        "\x1b[34mprint() bypass Click.\x1b[0m\n"
    )
    assert result.stderr == "warning: Is the logger colored?\n"


def check_forced_uncolored_rendering(result):
    assert result.exit_code == 0
    assert result.output.startswith(
        "echo()\n"
        "echo(color=None)\n"
        "echo(color=True) bypass invoke.color = False\n"
        "echo(color=False)\n"
        "secho()\n"
        "secho(color=None)\n"
        "secho(color=True) bypass invoke.color = False\n"
        "secho(color=False)\n"
        "print() bypass Click.\n"
    )
    assert result.stderr == "warning: Is the logger colored?\n"


@skip_windows_colors
def test_invoke_optional_color(invoke):
    result = invoke(run_cli1, color=None)
    check_default_uncolored_rendering(result)
    assert result.output.endswith(
        "Context.color = None\nclick.utils.should_strip_ansi = True\n"
    )


@skip_windows_colors
def test_invoke_default_color(invoke):
    result = invoke(run_cli1)
    check_default_uncolored_rendering(result)
    assert result.output.endswith(
        "Context.color = None\nclick.utils.should_strip_ansi = True\n"
    )


@skip_windows_colors
def test_invoke_forced_color_stripping(invoke):
    result = invoke(run_cli1, color=False)
    check_forced_uncolored_rendering(result)
    assert result.output.endswith(
        "Context.color = None\nclick.utils.should_strip_ansi = True\n"
    )


@skip_windows_colors
def test_invoke_color_keep(invoke):
    """On windows Click ends up deciding it is not running in an interactive terminal
    and forces the stripping of all colors."""
    result = invoke(run_cli1, color=True)
    if is_windows():
        check_default_uncolored_rendering(result)
    else:
        check_default_colored_rendering(result)
    assert result.output.endswith(
        "Context.color = None\nclick.utils.should_strip_ansi = False\n"
    )


@skip_windows_colors
def test_invoke_color_forced(invoke):
    # Test colours are preserved while invoking, and forced to be rendered
    # on Windows.
    result = invoke(run_cli1, color="forced")
    check_default_colored_rendering(result)
    assert result.output.endswith(
        "Context.color = True\nclick.utils.should_strip_ansi = False\n"
    )
