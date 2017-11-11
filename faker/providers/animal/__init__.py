# coding=utf-8
from __future__ import unicode_literals
from .. import BaseProvider

class Provider(BaseProvider):
# Source: https://en.wikipedia.org/wiki/List_of_animals_by_common_name
    animals = (
        'Aardvark', 'Aardwolf', 'African buffalo', 'African elephant', 'African leopard', 'African wild dog', 
        'Albatross', 'Alligator', 'Alpaca', 'American black bear', 'American buffalo (bison)', 'American robin', 
        'Amphibian', 'Anaconda', 'Angelfish', 'Anglerfish', 'Ant', 'Anteater', 'Antelope', 'Antlion', 'Ape', 'Aphid', 
        'Arabian leopard', 'Arctic fox', 'Arctic wolf', 'Armadillo', 'Arrow crab', 'Asian black bear', 'Asp', 'Donkey', 
        'Baboon', 'Badger', 'Bald eagle', 'Bandicoot', 'Barnacle', 'Barracuda', 'Basilisk', 'Bass', 'Bat', 
        'Beaked whale', 'Bear', 'Beaver', 'Bedbug', 'Bee', 'Beetle', 'Bird', 'Blackbird', 'Black panther', 'Black widow spider', 
        'Blue bird', 'Blue jay', 'Blue whale', 'Boa', 'Boar', 'Bobcat', 'Bobolink', 'Bonobo', 'Booby', 'Box jellyfish', 
        'Bovid', 'Buffalo', 'Brown bear', 'Bug', 'Bull', 'Butterfly', 'Buzzard', 'Camel', 'Canada goose', 'Canid', 'Cape buffalo', 
        'Capybara', 'Cardinal', 'Caribou', 'Carp', 'Cat', 'Catshark', 'Caterpillar', 'Catfish', 'Cattle', 'Centipede', 'Cephalopod', 
        'Chameleon', 'Cheetah', 'Chickadee', 'Chicken', 'Chimpanzee', 'Chinchilla', 'Chipmunk', 'Cicada', 'Clam', 'Clownfish', 
        'Cobra', 'Cockroach', 'Cod', 'Condor', 'Constrictor', 'Coral', 'Cougar', 'Cow', 'Coyote', 'Coypu', 'Crab', 'Crane', 
        'Crane fly', 'Crawdad', 'Crayfish', 'Cricket', 'Crocodile', 'Crow', 'Cuckoo', 'Damselfly', 'Deer', 'Dhole', 'Dingo', 
        'Dinosaur', 'Dodo', 'Dog', 'Dolphin', 'Donkey', 'Dormouse', 'Dove', 'Dragonfly', 'Dragon', 'Duck', 'Dung beetle', 'Eagle', 'Earthworm', 
        'Earwig', 'Echidna', 'Eel', 'Egret', 'Elephant', 'Elephant seal', 'Elk', 'Emu', 'Ermine', 'Falcon', 'Ferret', 'Fennec', 'Finch', 
        'Firefly', 'Fish', 'Flamingo', 'Flea', 'Fly', 'Flyingfish', 'Fowl', 'Fox', 'Frog', 'Fruit bat', 'Gamefowl', 'Galliform', 'Gazelle', 
        'Gecko', 'Gerbil', 'Giant panda', 'Giant squid', 'Gibbon', 'Gila monster', 'Giraffe', 'Goat', 'Golden eagle', 'Goldfish', 'Goose', 
        'Gopher', 'Gorilla', 'Grasshopper', 'Great blue heron', 'Great white shark', 'Grebe', 'Grizzly bear', 'Ground shark', 'Ground sloth', 
        'Grouse', 'Guan', 'Guanaco', 'Guineafowl', 'Guinea pig', 'Gull', 'Guppy', 'Haddock', 'Halibut', 'Hammerhead shark', 'Hamster', 'Hare', 'Harrier', 
        'Hawk', 'Hedgehog', 'Hermit crab', 'Heron', 'Herring', 'Hippopotamus', 'Hookworm', 'Hornet', 'Horse', 'Hoverfly', 'Hummingbird', 
        'Humpback whale', 'Hyena', 'Iguana', 'Ibis', 'Jackal', 'Jaguar', 'Jay', 'Jellyfish', 'Junglefowl', 'Jacana', 'Kangaroo', 'Kangaroo mouse', 
        'Kangaroo rat', 'Kingfisher', 'Kite', 'Kiwi', 'Koala', 'Koi', 'Komodo dragon', 'Krill', 'Ladybug', 'Lamprey', 'Landfowl', 'Land snail', 'Lapwing', 
        'Lark', 'Leech', 'Lemming', 'Lemur', 'Leopard', 'Leopon', 'Limpet', 'Lion', 'Lionfish', 'Lizard', 'Llama', 'Lobster', 'Locust', 'Loon', 'Louse', 
        'Lungfish', 'Lynx', 'Macaw', 'Mackerel', 'Magpie', 'Mallard', 'Mammal', 'Manatee', 'Mandrill', 'Manta ray', 'Marlin', 'Marmoset', 'Marmot', 
        'Marsupial', 'Marten', 'Mastodon', 'Meadowlark', 'Meerkat', 'Megamouth shark', 'Mink', 'Minnow', 'Mite', 'Mockingbird', 'Mole', 'Mollusk', 
        'Mongoose', 'Monitor lizard', 'Monkey', 'Moose', 'Mosquito', 'Moth', 'Mountain goat', 'Mouse', 'Mule', 'Muskox', 'Narwhal', 'Neanderthal', 
        'Needlefish', 'Newt', 'New World quail', 'Nighthawk', 'Nightingale', 'Nile crocodile', 'Numbat', 'Ocelot', 'Octopus', 'Okapi', 
        'Old World quail', 'Olingo', 'Opossum', 'Orangutan', 'Orca', 'Oribi', 'Ostrich', 'Otter', 'Owl', 'Owl-faced monkey', 'Ox', 'Panda', 
        'Panther', 'Panthera hybrid', 'Parakeet', 'Parrot', 'Parrotfish', 'Partridge', 'Peacock', 'Peafowl', 'Pelican', 'Penguin', 'Perch', 
        'Peregrine falcon', 'Pheasant', 'Pig', 'Pigeon', 'Pike', 'Pilot whale', 'Pinniped', 'Piranha', 'Planarian', 'Platypus', 'Polar bear', 'Pony', 
        'Porcupine', 'Porpoise', 'Possum', 'Prairie dog', 'Praying mantis', 'Primate', 'Ptarmigan', 'Puffin', 'Puma', 'Python', 'Quail', 'Quelea', 
        'Quetzal', 'Quokka', 'Rabbit', 'Raccoon', 'Rainbow trout', 'Rat', 'Rattlesnake', 'Raven', 'Ray', 'Red deer', 'Red fox', 'Red panda', 'Red squirrel', 
        'Reindeer', 'Reptile', 'Rhinoceros', 'Right whale', 'Roadrunner', 'Rodent', 'Rook', 'Rooster', 'Roundworm', 'Saber-toothed cat', 'Sailfish', 
        'Salamander', 'Salmon', 'Sawfish', 'Scale insect', 'Scallop', 'Scorpion', 'Seahorse', 'Sea lion', 'Sea slug', 'Sea snail', 'Serval', 'Shark', 
        'Sheep', 'Shrew', 'Shrimp', 'Silkworm', 'Silverfish', 'Skink', 'Skunk', 'Sloth', 'Slug', 'Smelt', 'Snail', 'Snake', 'Snipe', 'Snow leopard', 
        'Sockeye salmon', 'Sole', 'Sparrow', 'Sperm whale', 'Spider', 'Spider monkey', 'Spoonbill', 'Squid', 'Squirrel', 'Starfish', 'Star-nosed mole', 
        'Steelhead trout', 'Stingray', 'Stoat', 'Stork', 'Sturgeon', 'Sugar glider', 'Swallow', 'Swan', 'Swift', 'Swordfish', 'Swordtail', 'Tahr', 'Takin', 
        'Tapir', 'Tarantula', 'Tarsier', 'Tasmanian devil', 'Termite', 'Tern', 'Thrush', 'Tick', 'Tiger', 'Tiger shark', 'Tiglon', 'Titi', 'Toad', 'Tortoise', 
        'Toucan', 'Trapdoor spider', 'Tree frog', 'Trout', 'Tuna', 'Turkey', 'Turtle', 'Tyrannosaurus', 'Urial', 'Unicorn', 'Vampire bat', 'Vampire squid', 
        'Vaquita', 'Vicuña', 'Viper', 'Voalavoanala', 'Vole', 'Vulture', 'Wallaby', 'Walrus', 'Wasp', 'Warbler', 'Waterbuck', 'Water buffalo', 'Water chevrotain', 
        'Weasel', 'Whale', 'Whippet', 'Whitefish', 'White rhinoceros', 'Whooping crane', 'Wild boar', 'Wildcat', 'Wildebeest', 'Wildfowl', 'Wolf', 'Wolverine', 
        'Wombat', 'Wood lemming', 'Woodchuck', 'Woodpecker', 'Woolly dormouse', 'Woolly hare', 'Worm', 'Wren', 'Xerinae', 'X-ray fish', 'Yak', 'Yellow perch', 
        'Zebra', 'Zebra finch', 'Zebra shark', 'Zebu', 'Zorilla', 'Zanj sun squirrel', 'Zaphir\'s shrew', 'Zarudny\'s jird', 'Zarudny\'s rock shrew', 
        'Zebra duiker', 'Zempoaltepec deer mouse', 'Zempoaltépec vole', 'Zenker\'s fruit bat', 'Zuniga\'s dark rice rat'
    )

    def animal(self):
        return self.random_element(self.animals)