import subprocess

def render_blog():
    # copy _base and _navlinks from main templates directory
    subprocess.check_call(['scp', '../leastauthority.com/lae_site/templates/_base.html', 'themes/lae/templates/_base.html'])
    subprocess.check_call(['scp', '../leastauthority.com/lae_site/templates/_navlinks.html', 'themes/lae/templates/_navlinks.html'])
    subprocess.check_call(['scp', '../leastauthority.com/content/static/css/style.css', 'themes/lae/static/style.css'])

    # run pelican
    subprocess.check_call(['pelican', '-v', '-s', 'conf.py'])


if __name__ == "__main__":
    render_blog()
