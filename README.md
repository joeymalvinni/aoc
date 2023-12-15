# 🎄 Advent of Code Solutions
These are my Advent of Code submissions. Each file is a revisited solution, written sometime after I've had time to revisit each problem.

# Tools

## AOC Input Downloader

To better download the long input strings for each day, I made a Rust utility program to download the inputs for me. It was made using the asynchronous runtime `tokio` alongside `clap` to parse command line arguments. 

### Usage

| Argument     | Alias       |  Description |
| -----------  | ----------- | ----------- |
| `--year`     |  `-y`       | Downloads the input file for the given year. If no day is given alongside the specified year, it defaults to downloading day 1 year `${YEAR}`.      |
| `--day`      |  `-d`       | Downloads the input for the specicified day in the current year.       |
| `--output`   |  `-o`       | Saves the input to the specified output file.       |


## Custom Aliased Commands

To run my solutions, I aliased custom `aoc` and `aot` commands, which run the first Python file found in the current working directory with both test and real input. This works by piping `< in` and `< test` into the `python3` command, which allows you to use `open(0).read()` to access the file.
<br>

Changes to `~/.bash_profile`:
```bash
alias aoc='echo -n "$(tput setaf 6)" && python3 "$(fd -e py | head -n 1)" < test && echo -n  "$(tput sgr0)" && python3 "$(fd -e py | head -n 1)" < in'
alias aot='python3 "$(fd -e py | head -n 1)" < test'
```
<br>

![aoc command running day 11 solution](/host/AOC.png)

| Command     | Description |
| ----------- | ----------- |
| `aoc`       | Run the first Python program found in the current working directory with the test input and real input. The output of the programming running on test input is output in cyan.       |
| `aot`       | Only runs the first Python program found on the test input.        |

<br>

## Userscripts

Additionally, I use a [custom userscript](/host/userscript.js) for copying code blocks, which is a modified version of [tjjfvi's custom userscript](https://github.com/tjjfvi/aoc-2021/blob/main/host/userscript.js).

![copy code block image](/host/copy.png) 

