# Plum Econet api wrapper

This package aims to simplify using Plum Econet api available via local network.

Based on and tested with local router connected to HKS Lazar SmartFire pellet furnace.

# Basic usage

```python
import asyncio
from plum_econet import Smartfire

async def main():
    smartfire = Smartfire("<host>", "username", "password")
    await smartfire.setup()
    await smartfire.update()
    print(f"Current temperature {smartfire.central_heating.temperature}")
    print(f"Target temperature {smartfire.central_heating.target_temperature}")
    await smartfire.central_heating.set_target_temperature(30)
    await asyncio.sleep(5)
    await smartfire.update()
    print(f"Target temperature {smartfire.central_heating.target_temperature}")

if __name__ == "__main__":
    asyncio.run(main())
```
