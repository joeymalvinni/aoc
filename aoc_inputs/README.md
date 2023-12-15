# Advent of Code Input Downloader
### ⚠️ Make sure you update the `SESSION` constant in [main.rs](https://github.com/joeymalvinni/aoc/blob/991d4b82d13e35ac6622d8b8f3e82632d60405d8/aoc_inputs/src/main.rs#L8) to be your `session` cookie on the [advent of code website](https://adventofcode.com).

To better download the long input strings for each day, I made a Rust utility program to download the inputs for me. It was made using the asynchronous runtime `tokio` alongside `clap` to parse command line arguments. 

### Usage

| Argument     | Alias       |  Description |
| -----------  | ----------- | ----------- |
| `--year`     |  `-y`       | Downloads the input file for the given year. If no day is given alongside the specified year, it defaults to downloading day 1 year `${YEAR}`.      |
| `--day`      |  `-d`       | Downloads the input for the specicified day in the current year.       |
| `--output`   |  `-o`       | Saves the input to the specified output file.       |
