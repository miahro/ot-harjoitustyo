"""invoke tehtävät"""
from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)

@task
def generate_questions(ctx):
    ctx.run("python3 src/generate_questions.py", pty=True)


@task
def coveragereport(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)


@task
def initializedb(ctx):
    ctx.run("python3 src/dbinit.py", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task 
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
