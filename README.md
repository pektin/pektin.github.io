# lets-jam.org

The website for the Jam programming language

## Requirements

The website currently uses the Sphinx documentation generator, along with the bootstrap theme. You will need to install all of the following:

 - Sphinx: http://sphinx-doc.org/
 - Boostrap: http://ryan-roemer.github.io/sphinx-bootstrap-theme/
 - make

### On Ubuntu
```
sudo apt-get install python-sphinx pip make
sudo pip install sphinx_bootstrap_theme
```

## Deployment

The `site` branch is the one used for active development. In order to perform a local build run `./build.py build`. The jam documentation will be fetched and the sphinx site built. With `./build deploy` the build contents will be moved to the `master` branch, which can then be comitted and pushed to update the website.
