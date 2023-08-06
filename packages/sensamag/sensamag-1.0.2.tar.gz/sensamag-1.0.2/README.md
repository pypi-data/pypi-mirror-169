[![DeepSource](https://deepsource.io/gh/freezerain/sensamag_utility.svg/?label=active+issues&show_trend=true&token=tqqs40FSee57xeO0zqak7Fs1)](https://deepsource.io/gh/freezerain/sensamag_utility/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/freezerain/sensamag_utility.svg/?label=resolved+issues&show_trend=true&token=tqqs40FSee57xeO0zqak7Fs1)](https://deepsource.io/gh/freezerain/sensamag_utility/?ref=repository-badge)

This package is used to update Sensamag database.

### Usage:
1. Install as standard pip package: `pip install sensamag`
2. Run any command with syntax: `sensamag <Optional connection params> <command> <command params>`
3. To see all available commands run: `sensamag --help`

### Examples:
1) To list all languages:`sensamag listlang`
2) Same but with different connection params: `sensamag --port 8080 --user IAmAUser listlang`
3) To add new language using helper: `sensamag addlang`
4) To add new language using oneliner: `sensamag addlang --name German --culture de-DE --priority 5`
5) To export data: `sensamag exportdb --path <path to folder to create *.csv>`

### CSV Schema:
To successfully import CSV data, headers should contain exact column names to be parsed.

Look up exact names with `sensamag csvschema`