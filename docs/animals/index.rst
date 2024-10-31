Animals Provider
================

The Animals provider offers comprehensive and accurate animals data,covering an extensive range of species. It includes info like the common name and the scientific name. This data can be useful for applications requiring realistic representations of biological diversity, educational tools, wildlife databases, or any project that needs accurate animal species data.

**Installation**

Install with pip:

.. code-block:: python

    >>> pip install faker-animals

Add as a provider to your Faker instance:

.. code-block:: python

    >>> from faker import Faker
    >>> from faker_animals import AnimalsProvider
    >>> fake = Faker()
    >>> fake.add_provider(AnimalsProvider)


**Usage examples**

**Animal**

.. code-block:: python

    >>> fake.animal()
    {
        'common_name': 'Kangaroo',
        'scientific_name': 'Macropodidae',
        'class': 'mammals'
    }

**Animal Common Name**

.. code-block:: python

    >>> fake.animal_name()
    'Brown Bear'


**Animal Scientific Name**

.. code-block:: python

    >>> fake.animal_name_scientific()
    'Ursus arctos'


**Bird**

.. code-block:: python

    >>> fake.bird()
    {
      'common_name': 'African Grey Parrot',
      'scientific_name': 'Psittacus erithacus',
      'class': 'birds'
    }


**Mammal**

.. code-block:: python

    >>> fake.mammal()
    {
      'common_name': 'Alaskan Husky',
      'scientific_name': 'Canis lupus',
      'class': 'mammals'
    }


**Fish**

.. code-block:: python

    >>> fake.fish()
    {
      'common_name': 'White Catfish',
      'scientific_name': 'A. catus',
      'class': 'fish'
    }


**Reptile**

.. code-block:: python

    >>> fake.reptile()
    {
      'common_name': 'Black Mamba',
      'scientific_name': 'D. polylepis',
      'class': 'reptiles'
    }


**Amphibian**

.. code-block:: python

    >>> fake.amphibian()
    {
      'common_name': 'Green Frog',
      'scientific_name': 'Lithobates clamitans',
      'class': 'amphibians'
    }

