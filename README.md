# Faker #

Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.

Faker is heavily inspired by PHP's [Faker](http://github.com/fzaninotto/Faker), Perl's [Data::Faker](http://search.cpan.org/~jasonk/Data-Faker-0.07/), and by ruby's [Faker](http://faker.rubyforge.org/).

## Basic Usage

Use `faker.Factory.create()` to create and initialize a faker generator, which can generate data by accessing properties named after the type of data you want.

```python

from faker import Factory

faker = Factory.create()

faker.name()
# 'Lucy Cechtelar'

faker.address()
# "426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700"

faker.text()
# Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi 
# beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt
# amet quidem. Iusto deleniti cum autem ad quia aperiam.
# A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui 
# quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur
# voluptatem sit aliquam. Dolores voluptatum est.
# Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.
# Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati. 
# Et sint et. Ut ducimus quod nemo ab voluptatum.
```

Each call to method `faker.name()` yealds a different (random) result. This is because faker uses `__getattr__` magic, and forwards `faker.Genarator.method_name()' calls to `faker.Generator.format(method_name)`.

```python

for i in range(0,10):
  print faker.name()

	# Adaline Reichel
	# Dr. Santa Prosacco DVM
	# Noemy Vandervort V
	# Lexi O'Conner
	# Gracie Weber
	# Roscoe Johns
	# Emmett Lebsack
	# Keegan Thiel
	# Wellington Koelpin II
	# Ms. Karley Kiehn V
```


## License

Faker is released under the MIT Licence. See the bundled LICENSE file for details.


Credits
-------
- [FZaninotto][fzaninotto] / [Faker][faker]
- [Distribute][distribute]
- [Buildout][buildout]
- [modern-package-template][modern-package-template]

[fzaninotto]: https://github.com/fzaninotto  "F.Zaninotto"
[faker]: https://github.com/fzaninotto/Faker "Php faker"
[buildout]: http://www.buildout.org/
[distribute]:  http://pypi.python.org/pypi/distribute
[modern-package-template]: http://pypi.python.org/pypi/modern-package-template
