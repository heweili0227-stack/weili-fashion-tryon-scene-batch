# Weili Fashion Try-On Scene Batch

Selectable AI fashion try-on skill for Codex. It turns a model photo plus a garment photo into 1, 4, or 9 styled try-on images after presenting 30 scene options for the user to choose from.

中文：这是一个用于 Codex 的服装换装 skill。用户上传模特照片和服装照片后，先展示 30 个候选场景，再由用户选择场景编号、出图数量和画幅比例，最终生成服装上身图。

## Features / 功能

- Preserve model identity, face, hair, body proportions, and pose family.
- Faithfully transfer garment silhouette, material, color, neckline, sleeves, hem, buttons, seams, and fit.
- Present 30 selectable scenes before generation.
- Output count choices: 1, 4, or 9 images.
- Aspect ratio choices: 3:4, 9:16, or 1:1.
- Supports English, Chinese, bilingual, and auto language modes.

## Install / 安装

Copy this folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R weili-fashion-tryon-scene-batch ~/.codex/skills/
```

Then invoke:

```text
$weili-fashion-tryon-scene-batch
```

## Example / 案例

Example user choice:

```text
场景编号：3,14,25,27；图片数量：4；画幅比例：9:16
```

The skill maps those choices to four scene prompts:

- 03 black-box-studio: dark studio with controlled rim light and subtle reflective floor
- 14 neon-alley: clean neon-lit alley with wet pavement and abstract colored reflections
- 25 rooftop-evening: city rooftop at blue hour with skyline bokeh and light wind
- 27 window-loft: sunlit loft with tall windows, pale concrete floor, quiet morning light

See `examples/case-01-selected-scenes.md` for a complete bilingual case write-up.

Note: the public example intentionally omits private model and garment photos. Add only images you own or have permission to publish.

## Repository Structure / 目录结构

```text
weili-fashion-tryon-scene-batch/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── examples/
│   └── case-01-selected-scenes.md
├── references/
│   ├── prompting.md
│   └── scene-bank.json
└── scripts/
    └── select_scenes.py
```
