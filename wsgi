[buildout]
parts += app

[app]
recipe = collective.recipe.template
url = https://all-the-plones.aclark.net/app.ini
output = ${buildout:directory}/app.ini


[plone]
eggs +=
    PasteScript
    WebError
    repoze.retry
    repoze.tm2
    repoze.vhm
scripts += paster
