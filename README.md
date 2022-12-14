REPEATER
========

Repeater Entry Provides Extremely Accurate and True Estimates of Range
----------------------------------------------------------------------

The repeater database to end all repeater databases. 

Amateur Radio operators often use repeaters to allow multiple people
with small, low power radios to communicate over a larger area than they
would otherwise be able to.

To use these repeaters, ham radio operators need to know certain details,
such as name, frequency, location, and access details. They then program
these settings in their radios and are able to use the repeater.

This database is meant to replace the existing databases like repeaterbook
and others, because their data is often incomplete, insufficient,
outdated, or just flat-out wrong. Moreover, many of these existing
databases are focused on making money by collecting data that users
submit and then trying to claim copyright on that data. Repeater owners
don't have a good or easy way to update databases with details about their repeaters.

This project is all about fixing that.

Goals/Values:
-------------
1. Provide information for Amateur Radio (and possible other) operators
to conveniently find known-good information about the radio resources
near them.
2. This information is provided without cost, copyright, or other
restrictions. It will remain open and shareable, in keeping with various
ham radio and hacker cultural traditions.
3. The database should hold all known information about a node. If you
find that you have information about a node and no way to enter it,
please open an issue, or better yet, a pull request adding the format. 
However, for now, network information should not be included.
4. Quality of data trumps all (because that's the weak part of the existing databases).



Deployments
-----------
This repo will automatically deploy the `main` branch to https://repeater.m17project.org



Development Instructions / HACKING
----------------------------------
This is easiest to work with in docker. To see what the make commands are
doing, check out the `makefile` for the directory you run the command
in. See also [makefiletutorial.com](https://makefiletutorial.com/) and
the [makefile docs](https://www.gnu.org/software/make/manual/make.html).

`make img` and `make dev` in the root directory here with this README
will make a local docker image of the project and start it up with local
files under `./app/` mapped into the container under `/app/`. `./app/`
has another makefile which offers some quick options for interacting with
django, such as a development server using djangos built-in runserver (`make`),
and another using gunicorn which is a little closer to how it runs
in production (`make gunicorn`).

This docker setup means you can edit the source as you wish, and all the
django tools and such are confined to the container. In the container
shell.

The general way you'd go about making changes is as follows:

Fork this repo on Github, clone down your fork, check out a branch to
work on, make changes to that local copy, commit those changes, push the
changes to your fork on github, and open a pull request to the main repo
under the M17Project organization.

As a general rule: If you get stuck or confused, spend fifteen solid
minutes trying hard, and then reach out on the M17 discord channel in the #repeaterdb 
room: https://discord.gg/h9SFBJBzx8

Don't suffer for hours, people would love to help!
