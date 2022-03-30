# Allure Workflow #


### What is this repository for? ###

* Allure Integration with selenium 4.0 (Python 3.10)


## Run Locally

Clone the project

Open terminal and go to clone directory

```bash
  cd < clone_dir_path >
```
Start virtual environment

```bash
  pipenv shell
```

Run test <b>with</b> allure report

```bash
  pytest --alluredir=reports
```
Run test <b>without</b> allure report

```bash
  pytest .
```

Open allure report

```bash
  allure serve reports
```

stop virtual environment

```bash
  deactivate
```

