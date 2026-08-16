# Case 01: Four Selected Try-On Scenes / 四个指定场景换装案例

## User Request / 用户请求

```text
场景编号：3,14,25,27；图片数量：4；画幅比例：9:16
```

Inputs:

- Image 1: model reference photo
- Image 2: garment reference photo

Public publishing note:

- Do not include private model photos, private garment photos, or generated likeness outputs in a public repository unless you own the rights and have permission.
- This case records the reusable workflow and scene mapping only.

## Selected Scene Mapping / 场景映射

| Output | Candidate | Scene Slug | Scene Description |
|---:|---:|---|---|
| 1 | 03 | black-box-studio | Dark studio with controlled rim light and subtle reflective floor |
| 2 | 14 | neon-alley | Clean neon-lit alley with wet pavement and abstract colored reflections |
| 3 | 25 | rooftop-evening | City rooftop at blue hour with skyline bokeh and light wind |
| 4 | 27 | window-loft | Sunlit loft with tall windows, pale concrete floor, quiet morning light |

## Generation Settings / 生成设置

```json
{
  "language_mode": "zh",
  "image_count": 4,
  "aspect_ratio": "9:16",
  "selected_candidate_numbers": [3, 14, 25, 27],
  "output_policy": "one image-generation call per final image"
}
```

## Prompt Skeleton / 提示词骨架

```text
Use case: identity-preserve
Asset type: fashion virtual try-on batch image
Input images: Image 1 is the model reference; Image 2 is the garment reference.
Primary request: create one realistic fashion try-on image of the model wearing the supplied garment in [selected scene].
Subject: preserve the same model identity, face, body proportions, hair, skin tone, and natural presence from Image 1.
Garment: faithfully transfer the garment from Image 2, preserving silhouette, fabric, color, print, neckline, sleeves, hem, seams, fasteners, drape, texture, and fit.
Composition/framing: full-height 9:16 vertical fashion editorial composition with the garment clearly visible.
Lighting/mood: match lighting to the selected scene with realistic shadows and reflections.
Avoid: extra people, changed face, changed body shape, generic replacement clothing, invented logos, text, watermark, UI overlay, distorted hands, broken seams, oversexualized styling, plastic skin, painterly look.
```

## Expected Output Manifest / 预期输出清单

```json
{
  "outputs": [
    {
      "file": "tryon-01-black-box-studio.png",
      "candidate_number": 3,
      "scene_slug": "black-box-studio",
      "aspect_ratio": "9:16"
    },
    {
      "file": "tryon-02-neon-alley.png",
      "candidate_number": 14,
      "scene_slug": "neon-alley",
      "aspect_ratio": "9:16"
    },
    {
      "file": "tryon-03-rooftop-evening.png",
      "candidate_number": 25,
      "scene_slug": "rooftop-evening",
      "aspect_ratio": "9:16"
    },
    {
      "file": "tryon-04-window-loft.png",
      "candidate_number": 27,
      "scene_slug": "window-loft",
      "aspect_ratio": "9:16"
    }
  ]
}
```
