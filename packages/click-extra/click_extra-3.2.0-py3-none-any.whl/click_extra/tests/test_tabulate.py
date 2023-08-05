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

import pytest

# We use vanilla click primitives here to demonstrate the full-compatibility.
from click import echo, pass_context
from pytest_cases import fixture, parametrize

from ..tabulate import TabularOutputFormatter, table_format_option
from .conftest import command_decorators


@pytest.mark.parametrize("cmd_decorator, cmd_type", command_decorators(with_types=True))
def test_unrecognized_format(invoke, cmd_decorator, cmd_type):
    @cmd_decorator
    @table_format_option()
    def tabulate_cli1():
        echo("It works!")

    result = invoke(tabulate_cli1, "--table-format", "random")
    assert result.exit_code == 2
    assert not result.output

    group_help = " COMMAND [ARGS]..." if "group" in cmd_type else ""
    extra_suggest = (
        "Try 'tabulate-cli1 --help' for help.\n" if "extra" not in cmd_type else ""
    )
    assert result.stderr == (
        f"Usage: tabulate-cli1 [OPTIONS]{group_help}\n"
        f"{extra_suggest}\n"
        "Error: Invalid value for '-t' / '--table-format': "
        "'random' is not one of 'csv', 'csv-tab', 'double_grid', 'double_outline', "
        "'fancy_grid', 'github', 'grid', 'html', 'jira', 'latex', 'latex_booktabs', "
        "'mediawiki', 'minimal', 'moinmoin', 'orgtbl', 'outline', 'pipe', 'plain', "
        "'psql', 'rounded_grid', 'rounded_outline', 'rst', 'simple', 'simple_grid', "
        "'simple_outline', 'textile', 'tsv', 'vertical'.\n"
    )


csv_table = """
day,temperature
1,87
2,80
3,79
"""

csv_tab_table = """
day	temperature
1	87
2	80
3	79
"""

double_grid_table = """
╔═════╦═════════════╗
║ day ║ temperature ║
╠═════╬═════════════╣
║   1 ║          87 ║
╠═════╬═════════════╣
║   2 ║          80 ║
╠═════╬═════════════╣
║   3 ║          79 ║
╚═════╩═════════════╝
"""

double_outline_table = """
╔═════╦═════════════╗
║ day ║ temperature ║
╠═════╬═════════════╣
║   1 ║          87 ║
║   2 ║          80 ║
║   3 ║          79 ║
╚═════╩═════════════╝
"""

fancy_grid_table = """
╒═════╤═════════════╕
│ day │ temperature │
╞═════╪═════════════╡
│   1 │          87 │
├─────┼─────────────┤
│   2 │          80 │
├─────┼─────────────┤
│   3 │          79 │
╘═════╧═════════════╛
"""

github_table = """
| day | temperature |
|-----|-------------|
|   1 |          87 |
|   2 |          80 |
|   3 |          79 |
"""

grid_table = """
+-----+-------------+
| day | temperature |
+=====+=============+
|   1 |          87 |
+-----+-------------+
|   2 |          80 |
+-----+-------------+
|   3 |          79 |
+-----+-------------+
"""

html_table = """
<table>
<thead>
<tr><th>day</th><th>temperature</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>87</td></tr>
<tr><td>2</td><td>80</td></tr>
<tr><td>3</td><td>79</td></tr>
</tbody>
</table>
"""

jira_table = """
|| day || temperature ||
| 1 | 87 |
| 2 | 80 |
| 3 | 79 |
"""

latex_table = """
\\begin{tabular}{ll}
\\hline
 day & temperature \\\\
\\hline
 1 & 87 \\\\
 2 & 80 \\\\
 3 & 79 \\\\
\\hline
\\end{tabular}
"""

latex_booktabs_table = """
\\begin{tabular}{ll}
\\toprule
 day & temperature \\\\
\\midrule
 1 & 87 \\\\
 2 & 80 \\\\
 3 & 79 \\\\
\\bottomrule
\\end{tabular}
"""

mediawiki_table = """
{| class="wikitable" style="text-align: left;"
|+ <!-- caption -->
|-
! day !! temperature
|-
| 1 || 87
|-
| 2 || 80
|-
| 3 || 79
|}
"""

minimal_table = """
1  87
2  80
3  79
"""

moinmoin_table = """
|| ''' day ''' || ''' temperature ''' ||
||  1  ||  87  ||
||  2  ||  80  ||
||  3  ||  79  ||
"""

orgtbl_table = """
| day | temperature |
|-----+-------------|
|   1 |          87 |
|   2 |          80 |
|   3 |          79 |
"""

outline_table = """
+-----+-------------+
| day | temperature |
+=====+=============+
|   1 |          87 |
|   2 |          80 |
|   3 |          79 |
+-----+-------------+
"""

pipe_table = """
| day | temperature |
|----:|------------:|
|   1 |          87 |
|   2 |          80 |
|   3 |          79 |
"""

plain_table = """
day  temperature
  1           87
  2           80
  3           79
"""

psql_table = """
+-----+-------------+
| day | temperature |
|-----+-------------|
|   1 |          87 |
|   2 |          80 |
|   3 |          79 |
+-----+-------------+
"""

rounded_grid_table = """
╭─────┬─────────────╮
│ day │ temperature │
├─────┼─────────────┤
│   1 │          87 │
├─────┼─────────────┤
│   2 │          80 │
├─────┼─────────────┤
│   3 │          79 │
╰─────┴─────────────╯
"""

rounded_outline_table = """
╭─────┬─────────────╮
│ day │ temperature │
├─────┼─────────────┤
│   1 │          87 │
│   2 │          80 │
│   3 │          79 │
╰─────┴─────────────╯
"""

rst_table = """
===  ===========
day  temperature
===  ===========
  1           87
  2           80
  3           79
===  ===========
"""

simple_grid_table = """
┌─────┬─────────────┐
│ day │ temperature │
├─────┼─────────────┤
│   1 │          87 │
├─────┼─────────────┤
│   2 │          80 │
├─────┼─────────────┤
│   3 │          79 │
└─────┴─────────────┘
"""

simple_table = """
day  temperature
---  -----------
  1           87
  2           80
  3           79
"""

simple_outline_table = """
┌─────┬─────────────┐
│ day │ temperature │
├─────┼─────────────┤
│   1 │          87 │
│   2 │          80 │
│   3 │          79 │
└─────┴─────────────┘
"""

textile_table = """
|_.  day |_. temperature |
| 1  | 87 |
| 2  | 80 |
| 3  | 79 |
"""

tsv_table = """
day	temperature
1	87
2	80
3	79
"""

vertical_table = """
***************************[ 1. row ]***************************
day         | 1
temperature | 87
***************************[ 2. row ]***************************
day         | 2
temperature | 80
***************************[ 3. row ]***************************
day         | 3
temperature | 79
"""


expected_renderings = {
    "csv": csv_table,
    "csv-tab": csv_tab_table,
    "double_grid": double_grid_table,
    "double_outline": double_outline_table,
    "fancy_grid": fancy_grid_table,
    "github": github_table,
    "grid": grid_table,
    "html": html_table,
    "jira": jira_table,
    "latex": latex_table,
    "latex_booktabs": latex_booktabs_table,
    "mediawiki": mediawiki_table,
    "minimal": minimal_table,
    "moinmoin": moinmoin_table,
    "orgtbl": orgtbl_table,
    "outline": outline_table,
    "pipe": pipe_table,
    "plain": plain_table,
    "psql": psql_table,
    "rounded_grid": rounded_grid_table,
    "rounded_outline": rounded_outline_table,
    "rst": rst_table,
    "simple_grid": simple_grid_table,
    "simple": simple_table,
    "simple_outline": simple_outline_table,
    "textile": textile_table,
    "tsv": tsv_table,
    "vertical": vertical_table,
}


def test_recognized_modes():
    """Check all rendering modes proposed by the table module are accounted for and
    there is no duplicates."""
    assert len(TabularOutputFormatter._output_formats) == len(
        set(expected_renderings.keys())
    )
    assert set(TabularOutputFormatter._output_formats) == set(
        expected_renderings.keys()
    )


@fixture
@parametrize("cmd_decorator", command_decorators(no_groups=True))
def table_cli(cmd_decorator):
    @cmd_decorator
    @table_format_option()
    @pass_context
    def tabulate_cli2(ctx):
        echo(f"ctx.table_formatter.format_name = {ctx.table_formatter.format_name}")
        data = ((1, 87), (2, 80), (3, 79))
        headers = ("day", "temperature")
        ctx.print_table(data, headers)

    return tabulate_cli2


def test_default_rendering(invoke, table_cli):
    """Check default rendering is ``rounded_outline``."""
    result = invoke(table_cli)
    assert result.exit_code == 0
    assert result.output == (
        "ctx.table_formatter.format_name = rounded_outline" + rounded_outline_table
    )
    assert not result.stderr


@pytest.mark.parametrize(
    "format_name,expected",
    (pytest.param(k, v, id=k) for k, v in expected_renderings.items()),
)
def test_all_table_rendering(invoke, table_cli, format_name, expected):
    result = invoke(table_cli, "--table-format", format_name)
    assert result.exit_code == 0
    assert result.stdout == (
        f"ctx.table_formatter.format_name = {format_name}\n{expected.strip()}\n"
    )
    assert not result.stderr
