from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/screen/screen.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coveragereport(ctx):
    ctx.run("coverage html", pty=True)
