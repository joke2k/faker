import timeit

import faker


def bench(use_weighting, use_internal_caches, message):
    print(f"{message} : use_weighting = {use_weighting} use_internal_caches = {use_internal_caches}")
    f = faker.Faker(use_weighting=use_weighting, use_internal_caches=use_internal_caches)

    print(timeit.timeit(lambda: f.first_name(), number=100000))


def all_bench():
    global USE_WEIGHTING, use_internal_caches
    bench(use_weighting=True, use_internal_caches=False, message="Warmup")
    bench(use_weighting=True, use_internal_caches=False, message="Status Quo")
    bench(use_weighting=True, use_internal_caches=True, message="Caching Only")
    bench(use_weighting=False, use_internal_caches=False, message="Skip Weighting Only")
    bench(use_weighting=False, use_internal_caches=True, message="Both Optimizations")
    bench(use_weighting=True, use_internal_caches=False, message="Status Quo Again")


all_bench()
