[buildout]
parts += app

[app]
recipe = collective.recipe.template
url = https://all-the-plones.aclark.net/wsgi.ini
output = ${buildout:directory}/wsgi.ini

[plone]
eggs +=
    PasteScript
    WebError
    repoze.retry
    repoze.tm2
    repoze.vhm
scripts += paster
