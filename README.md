# Proof Of Concept #


### What is this repository for? ###

* Allure Integration with selenium 4.0 (Python 3.8)

## Setup Python and local environment
Install Homebrew
```bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Install pip and python@3.8 
```bash
Brew install pipenv
brew install python@3.8
Pipenv -v
```
Go to root directory of project
```bash
Pipenv install –python python3
```
___

## Run Locally

Clone the project

```bash
  git clone https://developerharsh@bitbucket.org/developerharsh/allurepoc.git
```

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

___

### Naming Convention for Automation Framework

| Type | Public | Internal |
| :--- | :--- | :--- |
| Packages | `lower_with_under` |  |
| Modules | `lower_with_under` | `_lower_with_under` |
| Classes | `CapWords` | `_CapWords` |
| Exceptions | `CapWords` |  |
| Functions | `lower_with_under()` | `_lower_with_under()` |
| Global/Class Constants | `CAPS_WITH_UNDER` | `_CAPS_WITH_UNDER` |
| Global/Class Variables | `lower_with_under` | `_lower_with_under` |
| Instance Variables | `lower_with_under` | `_lower_with_under` |
| Method Names | `lower_with_under()` | `_lower_with_under()` |
| Function/Method Parameters | `lower_with_under` |  |
| Local Variables | `lower_with_under` |  |

