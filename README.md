# lets-jam.org

The website for the Jam programming language.

## Requirements

The website currently uses the Sphinx documentation generator, along with the
bootstrap theme. You will need to install all of the following:

- [Sphinx](http://sphinx-doc.org/)
- [Sphinx Boostrap](http://ryan-roemer.github.io/sphinx-bootstrap-theme/)

### On Ubuntu

```bash
sudo apt-get install python3-sphinx python3-pip make
sudo pip3 install sphinx_bootstrap_theme
```

## Building

Building is done using the `build.py` build script. By default `build.py` will
fetch a temporary clone of [Jam](https://github.com/pektin/jam) for the
documentation. If you have a local copy use the `--repo` or `-r` arguments to
use the local copy instead. `build.py` has 3 commands:

* `build` makes a local build.
* `deploy` makes a local build in the `master` branch to be pushed to github in
  order to deploy the site.
* `clean` removes the local build data.

For more help run:

```bash
./build.py --help
```
