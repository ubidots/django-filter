# Publish

```bash
> cat ~/.pypirc
[distutils]
index-servers =
    ubidots

[ubidots]
repository = http://169.53.160.59:8080
username = ubidots_dev
password = <password>
```

```
pip install -U setuptools twine build
python -m build
python -m twine upload --repository ubidots dist/*
```

# Remote Branch

```bash
git remote add rpkilby https://github.com/rpkilby/django-filter.git
git fetch rpkilby
git checkout rpkilby/filter-method-name
git merge main
```
