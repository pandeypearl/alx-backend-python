# 0x02. Python - Async Comprehension

Introduction to Python Asynchronous Comprehensions covering the following concepts:

   + How to write an asynchronous generator
   + How to use async comprehensions
   + How to type-annotate generators

## Tasks

### 0. Async Generator
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

file: [0-async_generator.py](0-async_generator.py)

test file: [tests/0-main.py](tests/0-main.py)


### 1. Async Comprehensions
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

file: [1-async_comprehension.py](1-async_comprehension.py)

test file: [tests/1-main.py](tests/1-main.py)


### 2. Run time for four parallel comprehensions
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

file: [2-measure_runtime.py](2-measure_runtime.py)

test file: [tests/2-main.py](tests/2-main.py)
