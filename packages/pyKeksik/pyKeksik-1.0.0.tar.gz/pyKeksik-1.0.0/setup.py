from setuptools import setup
setup(name='pyKeksik',
      version='1.0.0',
      url='https://github.com/Friendosie/pyKeksik',
      license='MIT',
      description='Неофициальная библиотека для работы с API https://keksik.io',
      packages=['pyKeksik'],
      long_description="""# pyKeksik
Библиотека для взаимодействия с API [Кексика](https://keksik.io)

[Официальная документация](https://keksik.io/api)
Библиотека была написана потому что было нечего делать, обновлять буду постоянно

# Примеры кода
```python
from pyKeksik import KeksikApi
keksik_api = KeksikApi(group_id, apikey)
# Список донатов
print(keksik_api.donates.get())
# Список краутфанденговых кампаний
print(keksik_api.campaigns.get())
# Список выплат
print(keksik_api.payments.get())
# Баланс
print(keksik_api.balance())
```
# В планах:
 > Реализовать прием callback
# Поддержать автора монеткой
 4890 4947 7180 1784
# Связь с автором
[ВК](https://vk.com/frinyacode)""",
      long_description_content_type='text/markdown',
      author='Friendosie',
      install_requires=['requests'],
      author_email='friendosie@gmail.com',
      zip_safe=False)