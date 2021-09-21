import ray
import asyncio

ray.init()

@ray.remote
class AsyncActor(object):
    async def computation(self, num):
        print(f'Actor waiting for {num} sec')
        for x in range(num):
            await asyncio.sleep(1)
            print(f'Actor slept for {x+1} sec')
        return num

actor = AsyncActor.remote()

r1, r2, r3 = ray.get([actor.computation.remote(3),
        actor.computation.remote(5), actor.computation.remote(2)])

print(r1, r2, r3)
