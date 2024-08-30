# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar
import locale
# Transforma o retorno do código, na linguagem específica
locale.setlocale(locale.LC_ALL, 'pt_BR')
print(calendar.calendar(2022))

# Exibi todas os idiomas
for lang in locale.windows_locale.values():
    print(lang)

# Exibi todos os idiomas e formatos
for lang in locale.locale_alias.values():
    print(lang)