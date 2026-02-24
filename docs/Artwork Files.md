# Artwork Files

Artwork data is recorded in yml format as shown below.

```
sample_artwork:
  1234.5.6:
    type: painting
    origin: place
    location: place
    quality: 25
    artist: guy_of_place
  1250:
    location: other_place
```

---

## All allowed arguments with explanations

| Argument | Value type | Required | Explanation | 
|------|----------|----------|----------|
| type | artwork type | yes | Type of the artwork |
| origin | location ID | yes | The location where the artwork was created |
| location | location ID | yes | The location where the artwork is |
| quality | integer | yes | The quality of the artwork, ranges from 0-100 |
| artist | character ID | no | The character who created the artwork |

---
