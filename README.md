# automaton

A tiny CLI tool to automatically remove duplicate files with similar names, inspired by [Automate the Boring Stuff](https://automatetheboringstuff.com/2e/chapter10/).

I frequently accidentally download the same file twice, or redownload something that I had downloaded a while ago. I also tend to copy files instead of moving them, as I don't want to risk losing any data. This all leads to many redundant copies of files, especially in my Downloads folder. Therefore, I made this tool to help remedy that.

## Usage

This is a command-line utility that requires Python 3 to be installed.

You can use it like so:
```bash
python3 main.py path/to/folder
```

In its uploaded state, I changed it so that it does not mass delete, instead just printing out which duplicates there are. If you run it and feel confident with it automatically removing files, then you can uncomment the last line of the file.