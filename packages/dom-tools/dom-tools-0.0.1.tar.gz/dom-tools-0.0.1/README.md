# tools

## Table of Contents

- [tools](#tools)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Requirements](#requirements)
  - [Setup](#setup)
  - [CLI](#cli)
    - [Validate](#validate)
    - [Test](#test)
    - [jdql](#jdql)
    - [backup](#backup)
    - [ls](#ls)
    - [start](#start)
    - [stop](#stop)
    - [add](#add)
    - [remove](#remove)
    - [view](#view)
    - [tail](#tail)
  - [Connection Monitor](#connection-monitor)
    - [Getting Started](#getting-started)
  - [Feeze Monitor](#feeze-monitor)
    - [Getting Started](#getting-started-1)
  - [Component Diagram](#component-diagram)
  - [Testing](#testing)

## Description

Collection of tools, scripts, tests, and a CLI for administering DOM deployments.

## Requirements

Python requirements are found in the `requirements.txt` file.
[YAML::Perl module](https://metacpan.org/pod/YAML::Perl)

## Setup

1. `pip -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Add `dom.py` to PATH

## CLI

This CLI is meant to be a way to centralize the many DOM administrative tasks the DOM operations team does on a regular basis.

### Validate

Reads the configuation file. For all missions, fns, and rmi referenced in the config, reads those ServerConfig.pl, FNS.pl, and RMI.pl and confirms all config files referenced exist.

#### Example

`dom validate`

### Test

Tests running DOM services, such as mission catalogs, fns, and rmi by running DOM jcat commands.

#### Examples

`dom test` tests all missions, fns, and rmi found in the default config file.
`dom test cat psy` tests the psy mission.
`dom test rmi V10.14B1` tests the V10.14B1 rmi.
`dom test fns psy` tests the psy fns server.

### jdql

Runs a jdql command while optionally making a backup of the schema before the command is run.

#### Example

`dom jdql -m psy 'show status;'` runs the jdql show status command without backing up the schema.
`dom jdql -m psy -b 'show status;'` dumps a backup of the complete psy schema, then runs the show status command.

### backup

Backs up a specified schema

### ls

displays the status of all or a specified DOM service

#### Example

- `dom ls`
- `dom ls rmi`
- `dom ls cat`
- `dom ls fns`
- `dom ls sys`

#### Example

`dom ls` displays the status of all mission servers, fns, and rmi on the localhost
`dom ls cat psy` displays the status of all psy servers
`dom ls rmi V10.14B1` displays the status of the V10.14B1 rmi server
`dom ls fns psy` displays the status of the psy fns server

### start

Starts a DOM service

#### Example

`dom start cat psy` starts all psy servers
`dom start cat psy main` starts just the psy main server
`dom start rmi V10.14B1` starts the V10.14B1 RMI server
`dom start fns psy` starts the psy fns server

### stop

stops a DOM service

#### Example

`dom stop cat psy` stops all psy servers
`dom stop cat psy main` stops just the psy main server
`dom stop rmi V10.14B1` stops the V10.14B1 RMI server
`dom stop fns psy` stops the psy fns server


### add

adds a component (catalog, fns, rmi, user, group) to a DOM service.

#### Example

`dom add cat` launches an interactive tool to create a new mission catalog server
`dom add cat psy` launches an interactive tool to create a new server in the psy mission
`dom add rmi` launches an interactive tool to create a new rmi
`dom add fns` launches an interactive tool to create a new fns
`dom add user -m psy -n etrapp -g 'psy_test,psy_team'` adds the user `etrapp` to psy with membership in `psy_test` and `psy_team`
### remove

removes a component (catalog, fns, rmi, user, group) to a DOM service.

#### Example

`dom remove cat` launches an interactive tool to create a new mission catalog server
`dom remove cat psy` launches an interactive tool to create a new server in the psy mission
`dom remove rmi` launches an interactive tool to create a new rmi
`dom remove fns` launches an interactive tool to create a new fns
`dom remove user -m psy -n etrapp` removes the user `etrapp` from psy
`dom remove user -m psy -n etrapp -g 'psy_test,psy_team'` removes the user `etrapp` from psy groups `psy_test` and `psy_team`

### view

opens a specific dom config or log file in a text editor like vim

#### Example

- `dom view cat psy main config` opens psy's main `ServerConfig.pl` file in vim
- `dom view cat psy main log` opens psy's main log file in vim

### tail

tails a specific dom config or log file

#### Example

- `dom tail cat psy main config` tails psy's main `ServerConfig.pl` file
- `dom tail cat psy main log` tails psy's main log file
- `dom tail --follow cat psy main log` tails and follows psy's main log file

## Connection Monitor

This is a monitoring script that was used in Spring of 2022 to continuously monitor the number of connections being maintained with each DOM server at any given time. The maximum of number of connections should be 50. After that and DOM should start closing them. It continuously logs this information to a log file.

### Getting Started

`python3 tools/connection-mon/connection-mon.py &`

## Feeze Monitor

This is a monitoring script that was used in Spring of 2022 to continuously monitor DOM servers for a freezing issue they were experiencing. It does this my running the `domCheckAllServers.sh` utility over and over and when that call times out, it will send an email to an address configured in `tools/freeze-mon/freeze-mon.py`

### Getting Started

1. Update email in `tools/connection-mon/connection-mon.py`
2. `python3 tools/connection-mon/connection-mon.py &`

## Component Diagram

![component-diagram](/docs/component-diagram.png)
## Testing

It's important to note that there are at least two different types of tests in this module:

`tests/` contains all the tools for testing the rest of the tools and cli included in this module. There are the modules smoke tests. These test things like the modules ability to parse DOM config files, startup DOM services, and access process information on DOM. These are generally client tests.

`cli/testdom` contains code for testing the DOM services themselves. Generally, these are server tests.
