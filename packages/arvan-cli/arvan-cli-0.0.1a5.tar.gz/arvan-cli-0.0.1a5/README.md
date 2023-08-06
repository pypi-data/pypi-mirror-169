# arvan-cli
A Command Line Tool to Work with ArvanCloud

**This project is under development and not ready to use**

## Current status
- [x] Authentication storage
- [x] List all of the servers
- [x] Turn on and shutdown all of the servers
- [ ] Butify servers list
- [ ] Turn on and shutdown server by name

[Official API Documentation](https://www.arvancloud.com/docs/api/iaas/1.0)

## Installation
```bash
$ pip install arvan-cli
```

## Usage
```bash
$ arvan --help
Usage: arvan [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  authenticate  Add API key
  ls            List all servers
  shutdown      Shutdown server(s)
  turn-on       Turn on server(s)
```

## Build
In order to build the project, you must have `make` and a version of `python` greater than `3.6` installed on your machine known as `python` in your `PATH`.

```bash
$ make install
```

The above command will build and install the project in a virtual environment in the `.venv` directory. You can activate the virtual environment and use the project with `arvan` command.

For more information use `make help`.
