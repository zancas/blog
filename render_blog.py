import subprocess, os

def render_blog():
    # copy _base and _navlinks from main templates directory
    print os.getcwd()
    subprocess.check_call(['scp', '../leastauthority.com/lae_site/templates/_base.html', 'themes/lae/templates/_base.html'])
    subprocess.check_call(['scp', '../leastauthority.com/lae_site/templates/_navlinks.html', 'themes/lae/templates/_navlinks.html'])

    # run pelican
    subprocess.check_call(['pelican', '-v', '-s', 'conf.py'])


if __name__ == "__main__":
    render_blog()
