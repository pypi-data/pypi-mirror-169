# An API REST client for Prompted.art

This is a simple API client to send your generated art to prompted.art.

```
from prompted_art_api.client import PromptedArtAPI

client = PromptedArtAPI(
    api_key="334d39db1f0d43859419bf5039a49a1b206062e5"
)
data = {
    "prompt": "test from colab",
    "source": "midjourney",
    "url": "https://cdn.discordapp.com/attachments/1005626976016531567/1005858741767372873/-n_9_-i_-S_3792373097_ts-1659885810_idx-4.png",
}
result = client.create_prompt(data=data)
```
